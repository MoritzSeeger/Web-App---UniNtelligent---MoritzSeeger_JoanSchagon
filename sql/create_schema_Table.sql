DROP TABLE IF EXISTS degree_courses;
DROP TABLE IF EXISTS course_professors;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS degrees;
DROP TABLE IF EXISTS professors;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    teaching_style INTEGER NOT NULL CHECK(teaching_style BETWEEN 1 AND 10),
    self_study INTEGER NOT NULL CHECK(self_study BETWEEN 1 AND 10),
    character_style INTEGER NOT NULL CHECK(character_style BETWEEN 1 AND 10),
    digital INTEGER NOT NULL CHECK(digital BETWEEN 1 AND 10),
    ai_usage INTEGER NOT NULL CHECK(ai_usage BETWEEN 1 AND 10),
    role TEXT NOT NULL DEFAULT 'Student'
);

CREATE TABLE professors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_path TEXT,
    title TEXT,
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    teaching_style INTEGER NOT NULL CHECK(teaching_style BETWEEN 1 AND 10),
    self_study INTEGER NOT NULL CHECK(self_study BETWEEN 1 AND 10),
    character_style INTEGER NOT NULL CHECK(character_style BETWEEN 1 AND 10),
    digital INTEGER NOT NULL CHECK(digital BETWEEN 1 AND 10),
    ai_usage INTEGER NOT NULL CHECK(ai_usage BETWEEN 1 AND 10),    
    theses_is_supervisor BOOLEAN NOT NULL DEFAULT 0  -- VLt entfernen ( nicht relevant )
);

CREATE TABLE degrees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    semester_amount INTEGER NOT NULL,
    corny_quote TEXT --DUmmer lustiger Spruch
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT, 
    difficulty INTEGER CHECK(difficulty BETWEEN 1 AND 10), --
    
    -- Theorie vs. Praxis (1 = Nur Theorie, 10 = Nur Praxis)
    practice_orientation INTEGER CHECK(practice_orientation BETWEEN 1 AND 10),
    
    -- Art der Veranstaltung (z.B. 'Vorlesung', 'Seminar', 'Projekt')
    course_type TEXT NOT NULL DEFAULT 'Vorlesung'
);

-- Ein Studiengang hat viele Kurse, ein Kurs ist in vielen Studiengängen
CREATE TABLE degree_courses (
    degree_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (degree_id, course_id),
    FOREIGN KEY (degree_id) REFERENCES degrees (id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
);

-- Ein Prof hält viele Kurse, ein Kurs wird von vielen Profs gehalten
CREATE TABLE course_professors (
    professor_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    PRIMARY KEY (professor_id, course_id),
    FOREIGN KEY (professor_id) REFERENCES professors (id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses (id) ON DELETE CASCADE
);