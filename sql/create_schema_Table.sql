-- 1. AUFRÄUMEN: Alte Tabellen löschen, falls sie existieren
DROP TABLE IF EXISTS degree_courses;
DROP TABLE IF EXISTS course_professors;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS degrees;
DROP TABLE IF EXISTS professors;
DROP TABLE IF EXISTS users;

-- 2. USERS: Speichert nur noch die Zugangsdaten
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'Student' -- 'Student' oder 'Admin'
);

-- 3. PROFESSORS: Die Dozenten mit ihren fixen Eigenschaften
CREATE TABLE professors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT,
    title TEXT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    
    -- Bewertungskriterien (Skala 1-10), definiert in models.py
    teaching_style INTEGER NOT NULL CHECK(teaching_style BETWEEN 1 AND 10),
    selfstudy INTEGER NOT NULL CHECK(selfstudy BETWEEN 1 AND 10),
    character INTEGER NOT NULL CHECK(character BETWEEN 1 AND 10),
    digital INTEGER NOT NULL CHECK(digital BETWEEN 1 AND 10),
    ai_usage INTEGER NOT NULL CHECK(ai_usage BETWEEN 1 AND 10),
    
    -- Betreut Abschlussarbeiten? (0 = Nein, 1 = Ja)
    theses_is_supervisor BOOLEAN NOT NULL DEFAULT 0
);

-- 4. DEGREES: Die Studiengänge (z.B. Wirtschaftsinformatik)
CREATE TABLE degrees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    semester_amount INTEGER NOT NULL,
    corny_quote TEXT -- Der "dumme Spruch" aus models.py
);

-- 5. COURSES: Die Kurse (Inhalte & Art der Veranstaltung)
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT, -- Worum geht es in dem Kurs?
    difficulty INTEGER CHECK(difficulty BETWEEN 1 AND 10), --
    
    -- NEU: Theorie vs. Praxis (1 = Nur Theorie, 10 = Nur Praxis)
    practice_orientation INTEGER CHECK(practice_orientation BETWEEN 1 AND 10),
    
    -- NEU: Art der Veranstaltung (z.B. 'Vorlesung', 'Seminar', 'Projekt')
    course_type TEXT NOT NULL DEFAULT 'Vorlesung'
);

-- 6. VERKNÜPFUNG: Studiengänge <-> Kurse
-- Ein Studiengang hat viele Kurse, ein Kurs ist in vielen Studiengängen
CREATE TABLE degree_courses (
    degree_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (degree_id, course_id),
    FOREIGN KEY (degree_id) REFERENCES degrees (id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
);

-- 7. VERKNÜPFUNG: Dozenten <-> Kurse
-- Ein Prof hält viele Kurse, ein Kurs wird von vielen Profs gehalten
CREATE TABLE course_professors (
    professor_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (professor_id, course_id),
    FOREIGN KEY (professor_id) REFERENCES professors (id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
);