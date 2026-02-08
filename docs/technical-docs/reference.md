---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Navigation & Core (app.py)

### `index()`

**Route:** `/`

**Methods:** GET

**Purpose:** Lädt die Startseite der Anwendung.

**Sample output:**

Lädt Template

### `register()`

**Route:** `/register`

**Methods:** `GET, POST`

**Purpose:** Erstellt ein neues Benutzerkonto und speichert die individuellen Lern-Präferenzen (teaching_style, ai_usage, etc.) für das spätere Matching.

**Sample output:**

Registrierung erfolgreich! Du bist nun eingeloggt.

### `login()`

**Route:** `/login`

**Methods:** `GET, POST`

**Purpose:** Authentifiziert den Benutzer anhand von Benutzername und Passwort und startet die Session.

**Sample output:**

NONE (Leitet bei Erfolg zur Index-Seite weiter)


### `dozenten_suche()`

**Route:** `/dozenten`

**Methods:** `GET`

**Purpose:** Ermöglicht die Suche nach Dozenten über einen Query-String ?q=, der gegen Vor- und Nachnamen in der Datenbank geprüft wird.

**Sample output:**

Rendert dozenten_suche.html mit den gefilterten Ergebnissen.

### `dozenten_profil(id)`

**Route:** `/dozenten/<int:id>`

**Methods:** `GET`

**Purpose:** Ruft die Details eines spezifischen Dozenten anhand seiner ID aus der Datenbank ab.

**Sample output:**

Rendert dozenten_profil.html mit den Daten des Professors.


### `kurs_uebersicht()`

**Route:** `/kurse`

**Methods:** `GET`

**Purpose:** Ruft alle verfügbaren Kurse aus der Datenbank ab und sortiert sie alphabetisch.

**Sample output:**

Rendert kurs_uebersicht.html mit der Liste aller Kurse.


### `kurs_profil(kurs_id)`

**Route:** `/kurse/<int:kurs_id>`

**Methods:** `GET`

**Purpose:** Zeigt alle Details eines spezifischen Kurses an, inklusive der zugeordneten Studiengänge und Dozenten.

**Sample output:**

Rendert kurs_profil.html mit Kurs-Details, Degrees und Dozenten-Liste.

## Debugging
### `debug_db()`

**Route:** `/debug-db

**Methods:** `GET`

**Purpose:** Überprüft den physischen Speicherort der SQLite-Datei sowie die Integrität der Daten (Anzahl der Dozenten).

**Sample output:**

Browser shows: `📂 Datenbank-Pfad ist: ... ✅ Datei existiert. ⚖️ Dateigröße: ... Bytes 📊 Anzahl Dozenten in DB: 117`

---

## Database Management (db.py)

### `get_db_con(pragma_foreign_keys=True)`

**Route:** `N/A (Interne Funktion)`

**Methods:** /

**Purpose:** Stellt eine Verbindung zur SQLite-Datenbank her, konfiguriert das row_factory für den Zugriff auf Spalten über Namen und aktiviert standardmäßig Foreign Key Constraints.

**Sample output:**

/

### `init_db()`

**Route:** `/insert/sample`

**Methods:** GET

**Purpose:** Erstellt den instance-Ordner und initialisiert die Datenbankstruktur durch Ausführung des SQL-Schemas create_schema_Table.sql.

**Sample output:**

✅ Erfolg! Datenbank wurde befüllt.

### `insert_sample()`

**Route:** `N/A (Wird von /insert/sample aufgerufen)`

**Methods:** /

**Purpose:** Liest das SQL-Skript insert_sample.sql ein und befüllt die Datenbank mit Testdatensätzen.

**Sample output:**

/

### `get_user(username, password)`

**Route:** `/`

**Methods:** /

**Purpose:** Sucht in der Datenbank nach einem Benutzer mit der exakten Kombination aus Benutzername und Passwort.

**Sample output:**

Gibt ein sqlite3.Row-Objekt des Benutzers zurück oder None, wenn keine Übereinstimmung gefunden wurde.

### `get_user_by_username(username)`

**Route:** `/`

**Methods:** /

**Purpose:** Prüft, ob ein spezifischer Benutzername bereits in der users-Tabelle existiert.

**Sample output:**

Gibt die Benutzerdaten zurück, falls der Name bereits vergeben ist.

### `insert_user(username, password, teaching_style, self_study, character_style, digital, ai_usage)`

**Route:** `wird von /register gefunden`

**Methods:** /

**Purpose:** Fügt einen neuen Studenten in die Datenbank ein, wobei die individuellen Präferenzen für den Matching-Algorithmus sowie die Standardrolle 'Student' gespeichert

**Sample output:**

/


---

## Matching & Discovery

### `matches()`

**Route:** `/matches`

**Methods:** `GET`

**Purpose:** Berechnet basierend auf den im Profil hinterlegten Werten des Nutzers ein Ranking aller Dozenten unter Verwendung der match_logic.py (Ranking nach eigenen Präfferenzen, welcher DOzent Stiltechnisch am besten zum eigenen Stil passt).

**Sample output:**

Rendert das Template matches.html mit einer sortierten Liste der passendsten Dozenten.





---


## Quellen
Quellen mit Links: [Quellen_nur_links - WebApp.pdf](https://github.com/user-attachments/files/25163272/Quellen_nur_links.-.WebApp.pdf)
Quellen als PDF mit gesamten Chatverlauf: [Quellen_gesamter_Verlauf - WebApp.pdf](https://github.com/user-attachments/files/25163275/Quellen_gesamter_Verlauf.-.WebApp.pdf)

