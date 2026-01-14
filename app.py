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
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'


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

        existing_user = db.get_user_by_username(username)
        if existing_user is not None:
            error = "Benutzername existiert bereits."
        else:
            db.insert_user(username, password)

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
    
    # 1. Wir schauen, ob oben in der URL ein Suchbegriff steht (z.B. ?q=Müller)
    search_query = request.args.get('q')

    if search_query:
        # 2. WENN gesucht wurde: Suche in Vorname ODER Nachname
        # Die %-Zeichen bedeuten: "Egal was davor oder dahinter steht"
        sql = "SELECT * FROM professors WHERE surname LIKE ? OR name LIKE ?"
        term = f"%{search_query}%" # Macht aus "Müller" -> "%Müller%"
        professors = db_con.execute(sql, (term, term)).fetchall()
    else:
        # 3. WENN NICHT gesucht wurde: Zeige einfach alle an
        professors = db_con.execute('SELECT * FROM professors').fetchall()
    
    # Wir geben den Suchbegriff (search_query) wieder mit zurück, 
    # damit er im Eingabefeld stehen bleibt.
    return render_template('dozenten_suche.html', professors=professors, search_query=search_query)


# In app.py

@app.route('/dozenten/<int:id>')
@login_required
def dozenten_profil(id):
    db_con = db.get_db_con()
    
    # 1. Den Professor mit genau dieser ID suchen
    professor = db_con.execute(
        'SELECT * FROM professors WHERE id = ?', 
        (id,)
    ).fetchone()

    # 2. Sicherheits-Check: Falls die ID nicht existiert (z.B. User tippt ID 999)
    if professor is None:
        return "Dozent nicht gefunden", 404

    # 3. WICHTIG: Das Ergebnis als 'prof' an das HTML-Template schicken
    return render_template('dozenten_profil.html', prof=professor)


@app.route('/kurse')
@login_required
def kurs_uebersicht():
    return render_template('kurs_uebersicht.html')


@app.route('/kurse/<int:id>')
@login_required
def kurs_profil(id):
    return render_template('kurs_profil.html')



# App Startüunktion

if __name__ == '__main__':
    app.run(debug=True)
