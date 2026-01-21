import os
from functools import wraps
from flask import Flask, render_template, redirect, url_for, session, request, flash
import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)

app.cli.add_command(db.init_db)
app.teardown_appcontext(db.close_db_con)





# EIngeloggte Nutzer können direkt auf die Seite zugreifen, ohne Login oder Registrierung

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view



# Routen

@app.route('/')
@login_required
def index():
    return render_template('index.html')


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        teaching_style = int(request.form["teaching_style"]) 
        self_study     = int(request.form["self_study"])
        character_style= int(request.form["character_style"])
        digital        = int(request.form["digital"])
        ai_usage       = int(request.form["ai_usage"])

        existing_user = db.get_user_by_username(username)
        if existing_user is not None:
            error = "Benutzername existiert bereits."
        else:
            db.insert_user(username, password, teaching_style, self_study, character_style, digital, ai_usage)

            user = db.get_user(username, password)
            session['user_id'] = user['id']
            flash("Registrierung erfolgreich! Du bist nun eingeloggt.")
            return redirect(url_for('index'))

    return render_template('register.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# In app.py

@app.route('/dozenten')
@login_required
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
        # Hier stand vorher nur 'SELECT * FROM professors'
        sql = "SELECT * FROM professors ORDER BY surname ASC, name ASC"
        professors = db_con.execute(sql).fetchall()
    
    return render_template('dozenten_suche.html', professors=professors, search_query=search_query)



@app.route('/dozenten/<int:id>')
@login_required
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


@app.route('/kurse/<int:kurs_id>')
def kurs_profil(kurs_id):
    db_con = db.get_db_con()
    kurs = db_con.execute("SELECT * FROM courses WHERE id = ?", (kurs_id,)).fetchone()
    
    if kurs is None:
        return "Kurs nicht gefunden", 404
        
    return f"<h1>Profil für Kurs: {kurs['name']}</h1><p>{kurs['description']}</p>" 


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

@app.route('/traits')
def save_traits():
    db_path = os.path.join()