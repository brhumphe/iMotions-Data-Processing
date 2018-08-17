DROP TABLE IF EXISTS Participants
;

CREATE TABLE Participants
(
    Name      INTEGER
        CONSTRAINT Participants_eeg_Name_fk
        REFERENCES eeg (Name),
    Age       INTEGER,
    Gender    TEXT,
    StudyName TEXT
)
;

CREATE INDEX Participants_Name_index
    ON Participants (Name)
;

INSERT INTO Participants
    SELECT DISTINCT
        Name
        , Age
        , Gender
        , StudyName
    FROM eeg
    ORDER BY Name