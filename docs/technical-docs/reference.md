---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

{: .attention }
> This page collects internal functions, routes with their functions, and APIs (if any).
> 
> See [Uber](https://developer.uber.com/docs/drivers/references/api) or [PayPal](https://developer.paypal.com/api/rest/) for exemplary high-quality API reference documentation.
>
> You may delete this `attention` box.

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

### `init_db()`

**Route:** `/insert/sample`

**Methods:** GET

**Purpose:** Erstellt den instance-Ordner und initialisiert die Datenbankstruktur durch Ausführung des SQL-Schemas create_schema_Table.sql.

**Sample output:**

✅ Erfolg! Datenbank wurde befüllt.
---

## Matching & Discovery

### `matches()`

**Route:** `/matches`

**Methods:** `GET`

**Purpose:** Berechnet basierend auf den im Profil hinterlegten Werten des Nutzers ein Ranking aller Dozenten unter Verwendung der match_logic.py (Ranking nach eigenen Präfferenzen, welcher DOzent Stiltechnisch am besten zum eigenen Stil passt).

**Sample output:**

Rendert das Template matches.html mit einer sortierten Liste der passendsten Dozenten.


### `matches()`

**Route:** `/matches`

**Methods:** `GET`

**Purpose:** Berechnet basierend auf den im Profil hinterlegten Werten des Nutzers ein Ranking aller Dozenten unter Verwendung der match_logic.py (Ranking nach eigenen Präfferenzen, welcher DOzent Stiltechnisch am besten zum eigenen Stil passt).

**Sample output:**

Rendert das Template matches.html mit einer sortierten Liste der passendsten Dozenten.





---
