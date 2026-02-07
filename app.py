import os
from functools import wraps
from flask import Flask, render_template, redirect, url_for, session, request, flash, g
import db
from match_logic import compute_matching_scores, get_professors_df, get_user_df

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)

app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)



# Routen
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/matches") #[3] - ChatGPT: Used to fix broken session ID logic
def matches():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    

    user_df = get_user_df(user_id)

    user = user_df.iloc[0]

    prof_df = get_professors_df()
    
    ranked = compute_matching_scores(user, prof_df)

    matches_list = ranked.to_dict(orient="records")
    return render_template("matches.html", matches=matches_list)



@app.route('/insert/sample')
def insert_sample_data():
    # 1. Den Befehl ausführen
    db.insert_sample()
    
    # 2. Erfolgsmeldung anzeigen
    return "✅ Erfolg! Datenbank wurde befüllt."


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.get_user(username, password)
        if user is None:
            error = "Benutzername oder Passwort falsch"
        else:
            session['user_id'] = user['id']
            return redirect(url_for('index'))

    return render_template('login.html', error=error)


@app.route('/register', methods=['GET', 'POST']) # [1] ChatGPT - Sliders without JavaScript
def register():
    error = None

    def clamp_int(v, lo=1, hi=10, default=1):
        try:
            n = int(v)
        except (TypeError, ValueError):
            return default
        return max(lo, min(hi, n))

    # Defaults for GET (and also used if POST is missing anything)
    slider_defaults = {
        "teaching_style": 1,
        "self_study": 1,
        "character_style": 1,
        "digital": 1,
        "ai_usage": 1,
    }

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        # Read + clamp slider values (prevents crashes + enforces 1..10)
        teaching_style  = clamp_int(request.form.get("teaching_style"), default=slider_defaults["teaching_style"])
        self_study      = clamp_int(request.form.get("self_study"), default=slider_defaults["self_study"])
        character_style = clamp_int(request.form.get("character_style"), default=slider_defaults["character_style"])
        digital         = clamp_int(request.form.get("digital"), default=slider_defaults["digital"])
        ai_usage        = clamp_int(request.form.get("ai_usage"), default=slider_defaults["ai_usage"])

        # Minimal validation
        if not username or not password:
            error = "Bitte Benutzername und Passwort ausfüllen."
        else:
            existing_user = db.get_user_by_username(username)
            if existing_user is not None:
                error = "Benutzername existiert bereits."
            else:
                db.insert_user(username, password, teaching_style, self_study, character_style, digital, ai_usage)

                user = db.get_user(username, password)
                session['user_id'] = user['id']
                flash("Registrierung erfolgreich! Du bist nun eingeloggt.")
                return redirect(url_for('index'))

        # If we reached here, there was an error: re-render with the chosen values
        return render_template(
            'register.html',
            error=error,
            username=username,
            teaching_style=teaching_style,
            self_study=self_study,
            character_style=character_style,
            digital=digital,
            ai_usage=ai_usage,
        )

    # GET request
    return render_template('register.html', error=error, **slider_defaults)



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# In app.py

@app.route('/dozenten')
def dozenten_suche():
    db_con = db.get_db_con()
    
    search_query = request.args.get('q')

    if search_query:
        # Wir sortieren erst nach Nachname, und bei gleichen Nachnamen nach Vorname
        sql = """
            SELECT * FROM professors 
            WHERE surname LIKE ? OR name LIKE ? 
            ORDER BY surname ASC, name ASC
        """
        term = f"%{search_query}%"
        professors = db_con.execute(sql, (term, term)).fetchall()
    else:
        # ansonsten alle
        sql = "SELECT * FROM professors ORDER BY surname ASC, name ASC"
        professors = db_con.execute(sql).fetchall()
    
    return render_template('dozenten_suche.html', professors=professors, search_query=search_query)



@app.route('/dozenten/<int:id>')      #dynamische route mit id
def dozenten_profil(id):
    db_con = db.get_db_con()
    
    professor = db_con.execute(
        'SELECT * FROM professors WHERE id = ?', 
        (id,)
    ).fetchone()

    if professor is None:
        return "Dozent nicht gefunden", 404

    return render_template('dozenten_profil.html', prof=professor)


@app.route('/kurse')
def kurs_uebersicht():
    db_con = db.get_db_con()
    
    # Wir holen alle Kurse aus der Datenbank
    sql = "SELECT * FROM courses ORDER BY name ASC"
    kurse_data = db_con.execute(sql).fetchall()
    
    # Wir übergeben die Daten an das Template
    return render_template('kurs_uebersicht.html', kurse=kurse_data)


#@app.route('/kurse/<int:kurs_id>')
#def kurs_profil(kurs_id):
#    db_con = db.get_db_con()
#    kurs = db_con.execute("SELECT * FROM courses WHERE id = ?", (kurs_id,)).fetchone()
    
#    if kurs is None:
#        return "Kurs nicht gefunden", 404        
#    return f"<h1>Profil für Kurs: {kurs['name']}</h1><p>{kurs['description']}</p>" 

@app.route('/kurse/<int:kurs_id>')
def kurs_profil(kurs_id):
    db_con = db.get_db_con()
    
    # 1. Den Kurs selbst holen
    kurs = db_con.execute("SELECT * FROM courses WHERE id = ?", (kurs_id,)).fetchone()
    
    if kurs is None:
        return "Kurs nicht gefunden", 404

    # 2. Studiengänge laden (für die Liste "Teil von Studiengängen")
    degrees = db_con.execute("""
        SELECT d.name 
        FROM degrees d
        JOIN degree_courses dc ON d.id = dc.degree_id
        WHERE dc.course_id = ?
    """, (kurs_id,)).fetchall()

    # 3. Dozenten laden (für die Liste "Gelehrt von")
    profs = db_con.execute("""
        SELECT p.id, p.title, p.name, p.surname
        FROM professors p
        JOIN course_professors cp ON p.id = cp.professor_id
        WHERE cp.course_id = ?
    """, (kurs_id,)).fetchall()
        
    return render_template('kurs_profil.html', course=kurs, degrees=degrees, profs=profs)


import os
import sqlite3

@app.route('/debug-db')   # Debug mithilfe von KI erstellt
def debug_db():
    # 1. Wo sucht Flask die Datenbank?
    db_path = os.path.join(app.instance_path, 'todos.sqlite')
    
    status = f"📂 Datenbank-Pfad ist: {db_path}<br>"
    
    if os.path.exists(db_path):
        status += "✅ Datei existiert.<br>"
        # Größe prüfen
        size = os.path.getsize(db_path)
        status += f"⚖️ Dateigröße: {size} Bytes (0 Bytes = Leer!)<br>"
    else:
        status += "❌ Datei existiert NICHT! (Pfad-Problem)<br>"

    # 2. Wir versuchen manuell zu zählen
    try:
        con = sqlite3.connect(db_path)
        cursor = con.cursor()
        count = cursor.execute("SELECT count(*) FROM professors").fetchone()[0]
        status += f"📊 Anzahl Dozenten in DB: <b>{count}</b>"
        con.close()
    except Exception as e:
        status += f"❌ Fehler beim Lesen: {e}"

    return status
# App Startüunktion

if __name__ == '__main__':
    app.run(debug=True)


