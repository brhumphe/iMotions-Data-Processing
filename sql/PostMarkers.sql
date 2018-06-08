DROP TABLE IF EXISTS PostMarkers
;

CREATE TABLE PostMarkers
(
    "index"    INTEGER
        CONSTRAINT PostMarkers_eeg_index_fk
        REFERENCES eeg ("index"),
    PostMarker TEXT,
    Condition  INTEGER
)
;

INSERT INTO PostMarkers

-- 'Coding(F1)'
    SELECT
        "index"
        , 'Coding(F1)' AS PostMarker
        , 1            AS Condition
    FROM eeg
    WHERE PostMarker LIKE 'Coding(F1)'
    UNION


    -- 'Coding(F1)|First 30(F6)'
    SELECT
        "index"
        , 'Coding(F1)|First 30(F6)' PostMarker
        , 2 AS                      Condition
    FROM eeg
    WHERE PostMarker IN
          ('Coding(F1)|First 30(F6)',
           'Coding(F1)|First 30(F6)|First 30(F6)|First 30(F6)')
    UNION


    --     Coding(F1)|Last 15(F7)
    SELECT
        "index"
        , 'Coding(F1)|Last 15(F7)' AS PostMarker
        , 2                        AS Condition
    FROM eeg
    WHERE PostMarker IN ('Coding(F1)|Extra 15(F7)',
                         'Coding(F1)|Last 15(F7)',
                         'Coding(F1)|Last 15(F7)|Last 15(F7)|Last 15(F7)')
    UNION


    -- First 30(F6)
    SELECT
        "index"
        , 'First 30(F6)' AS PostMarker
        , 2              AS Condition
    FROM eeg
    WHERE PostMarker IN ('First 30(F6)',
                         'First 30(F6)|First 30(F6)|First 30(F6)')
    UNION


    -- Last 15(F7)
    SELECT
        "index"
        , 'Last 15(F7)' AS PostMarker
        , 2             AS Condition
    FROM eeg
    WHERE eeg.PostMarker IN ('Last 15(F7)',
                             'Extra 15(F7)',
                             'Last 15(F7)|Last 15(F7)')
    UNION


    -- Outside Website(F3)
    SELECT
        "index"
        , 'Outside Website(F3)' AS PostMarker
        , 1                     AS Condition
    FROM eeg
    WHERE eeg.PostMarker IN ('Outside Website(F3)')
    UNION


    -- Outside Website(F3)|First 30(F6)
    SELECT
        "index"
        , 'Outside Website(F3)|First 30(F6)' AS PostMarker
        , 2                                  AS Condition
    FROM eeg
    WHERE eeg.PostMarker IN ('Outside Website(F3)|First 30(F6)',
                             'Outside Website(F3)|First 30(F6)|First 30(F6)|First 30(F6)')
    UNION


    -- Outside Website(F3)|Last 15(F7)
    SELECT
        "index"
        , 'Outside Website(F3)|Last 15(F7)' AS PostMarker
        , 2                                 AS Condition
    FROM eeg
    WHERE eeg.PostMarker IN ('Outside Website(F3)|Last 15(F7)',
                             'Outside Website(F3)|Last 15(F7)|Last 15(F7)|Last 15(F7)')
    UNION


    -- Reading(F2)
    SELECT
        "index"
        , 'Reading(F2)' AS PostMarker
        , 1             AS Condition
    FROM eeg
    WHERE PostMarker IN ('Reading(F2)')
    UNION


    -- Reading(F2)|Last 15(F7)
    SELECT
        "index"
        , 'Reading(F2)|Last 15(F7)' AS PostMarker
        , 2                         AS Condition
    FROM eeg
    WHERE eeg.PostMarker IN
          ('Reading(F2)|Last 15(F7)',
           'Reading(F2)|Last 15(F7)|Last 15(F7)',
           'Reading(F2)|Last 15(F7)|Last 15(F7)|Last 15(F7)',
           'Reading(F2)|Extra 15(F7)')
    UNION


    -- Reading(F2)|First 30(F6)
    SELECT
        "index"
        , 'Reading(F2)|First 30(F6)' AS PostMarker
        , 2                          AS Condition
    FROM eeg
    WHERE PostMarker IN ('Reading(F2)|First 30(F6)',
                         'Reading(F2)|First 30(F6)|First 30(F6)|First 30(F6)')
    UNION


    -- Reading(F2)|Outside Website(F3)
    SELECT
        "index"
        , 'Reading(F2)|Outside Website(F3)' AS PostMarker
        , 1                                 AS Condition
    FROM eeg
    WHERE PostMarker IN ('Reading(F2)|Outside Website(F3)')