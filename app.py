from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

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
