
CREATE TABLE UniversityDegree (
    UniversityDegreeID INT PRIMARY KEY
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    Description VARCHAR(255),
    Difficulty INT
);

CREATE TABLE Professor (
    ProfessorID INT PRIMARY KEY,
    image_path VARCHAR(255),
    Title VARCHAR(100),
    Surname VARCHAR(100),
    Name VARCHAR(100),
    TeachingStyle_1_n INT
);

CREATE TABLE StudentUser (
    Usernumber INT PRIMARY KEY,
    UniversityDegreeID INT,
    Email VARCHAR(255),
    Surname VARCHAR(100),
    Name VARCHAR(100),
    LearningStyle_1_n INT,
    CONSTRAINT FK_Student_Degree FOREIGN KEY (UniversityDegreeID) 
        REFERENCES UniversityDegree(UniversityDegreeID)
);

CREATE TABLE ContainsCourse (
    UniversityDegreeID INT,
    CourseID INT,
    IsRequired BOOLEAN,
    PRIMARY KEY (UniversityDegreeID, CourseID), 
    CONSTRAINT FK_Contains_Degree FOREIGN KEY (UniversityDegreeID) 
        REFERENCES UniversityDegree(UniversityDegreeID),
    CONSTRAINT FK_Contains_Course FOREIGN KEY (CourseID) 
        REFERENCES Course(CourseID)
);


CREATE TABLE Class (

    ProfessorID INT,
    CourseID INT,
    Time DATETIME,
    IsTaughtBy BOOLEAN,
    CONSTRAINT FK_Class_Professor FOREIGN KEY (ProfessorID) 
        REFERENCES Professor(ProfessorID),
    CONSTRAINT FK_Class_Course FOREIGN KEY (CourseID) 
        REFERENCES Course(CourseID)
);


CREATE TABLE Matches (
    ProfessorID INT,
    Usernumber INT,
    LearningStyle_1_n INT,
    TeachingStyle_1_n INT,
    MatchingScore_1_n INT,
    MatchingScoreOverall FLOAT,
    PRIMARY KEY (ProfessorID, Usernumber), 
    CONSTRAINT FK_Match_Professor FOREIGN KEY (ProfessorID) 
        REFERENCES Professor(ProfessorID),
    CONSTRAINT FK_Match_Student FOREIGN KEY (Usernumber) 
        REFERENCES StudentUser(Usernumber)
);
