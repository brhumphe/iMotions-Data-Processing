DROP TABLE IF EXISTS Participants
;

CREATE TABLE Participants
(
    Name      INTEGER
        CONSTRAINT Participants_eeg_Name_fk
        REFERENCES eeg (Name),
    Age       INTEGER,
    Gender    TEXT,
    Condition INTEGER
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
        , CASE WHEN Name LIKE '1%'
        THEN 1
          ELSE 2
          END AS Condition
    FROM eeg
    ORDER BY Name