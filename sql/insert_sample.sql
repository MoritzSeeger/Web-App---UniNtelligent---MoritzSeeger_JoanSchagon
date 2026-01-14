INSERT INTO professors (id, title, surname, name, description, teaching_style, selfstudy, character, digital, ai_usage, theses_is_supervisor) 
VALUES 
(1, 'Prof. Dr.', 'Müller', 'Thomas', 'Liebt Python und KI.', 8, 4, 9, 10, 10, 1),
(2, 'Dr.', 'Schmidt', 'Helga', 'Sehr genau, viel Theorie.', 2, 9, 4, 3, 1, 1),
(3, 'M.Sc.', 'Jansen', 'Lars', 'Praxisnah aus der Wirtschaft.', 9, 2, 10, 8, 8, 0);

INSERT INTO degrees (id, name, semester_amount, corny_quote) 
VALUES 
(1, 'Wirtschaftsinformatik', 7, 'IT meets Business - und Kaffee.'),
(2, 'BWL', 6, 'Wer nichts wird, wird Wirt... oder Betriebswirt.');

INSERT INTO courses (id, name, description, difficulty, practice_orientation, course_type) 
VALUES 
(1, 'Grundlagen der Programmierung', 'Einführung in Python.', 7, 9, 'Vorlesung'),
(2, 'Rechnungswesen', 'Buchführung und Bilanzen.', 5, 2, 'Vorlesung'),
(3, 'Web-Entwicklung Projekt', 'Wir bauen eine App.', 8, 10, 'Projekt');

INSERT INTO degree_courses (degree_id, course_id) VALUES (1, 1), (1, 2), (1, 3), (2, 2);
INSERT INTO course_professors (professor_id, course_id) VALUES (1, 1), (1, 3), (2, 2), (3, 3);