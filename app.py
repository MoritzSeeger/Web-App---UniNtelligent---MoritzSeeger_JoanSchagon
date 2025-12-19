import os
from flask import Flask, render_template, redirect, url_for, session, request
import db

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='secret_key_just_for_dev_environment',
    DATABASE=os.path.join(app.instance_path, 'todos.sqlite')
)
app.cli.add_command(db.init_db)
app.cli.add_command(db.insert_db)
app.teardown_appcontext(db.close_db_con)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert/sample')
def run_insert_sample():
    db.insert_sample()
    return 'Database flushed and populated with some sample data.'


@app.route('/login', methods=['GET', 'POST']) # Muss noch als Startpunkt der Website gesetzt werden
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
            print("Login erfolgreich")

    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST']) # Muss noch in Login eingebaut werden, sodass man nur von dort aus zur registrierung kommt
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # existiert Nutzer schon?
        existing_user = db.get_user_by_username(username)
        if existing_user is not None:
            error = "Benutzername existiert bereits."
        else:
            # Nutzer in DB einfüügen
            db.insert_user(username, password)

            
            user = db.get_user(username, password)
            session['user_id'] = user['id']
            flash("Registrierung erfolgreich! Du bist nun eingeloggt.")
            return redirect(url_for('index'))

    return render_template('register.html', error=error)

@app.route('/dozenten')                             
def dozenten_suche():
    return render_template('dozenten_suche.html')

@app.route('/dozenten/<int:id>')
def dozenten_profil():
    return render_template('dozenten_profil.html')

@app.route('/kurse')
def kurs_uebersicht():
    return render_template('kursübersicht.html')

@app.route('/kurse/<int:id>')
def kurs_profil():
    return render_template('kurs_profil.html')

if __name__ == '__main__':
    app.run(debug=True)
