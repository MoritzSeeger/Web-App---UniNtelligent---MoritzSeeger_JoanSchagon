# insert_test.py
import sqlite3
import os

# Pfad zur Datenbank
db_path = os.path.join('instance', 'todos.sqlite')

# Verbindung zur Datenbank herstellen
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# SQL-Datei einlesen und ausführen
sql_file = os.path.join('sql', 'test.sql')  # deine Datei mit INSERT-Befehlen
with open(sql_file, 'r', encoding='utf-8') as f:
    sql_script = f.read()
    cur.executescript(sql_script)

# Änderungen speichern und DB schließen
conn.commit()
conn.close()

print("Testdaten wurden erfolgreich eingefügt!")
