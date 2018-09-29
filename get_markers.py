import sqlite3

conn = sqlite3.connect("data-eeg.db")
db = conn.cursor()

# for rowid, names in db.execute('SELECT "index", PostMarker FROM eeg'):
#     for name in names.split('|'):
#         print(rowid, name)
for row, markers in db.execute(
        """SELECT "index", PostMarker FROM abm_eeg WHERE PostMarker NOTNULL  AND 
        PostMarker NOT LIKE '%Setup%'"""):
    for marker in markers.split('|'):
        print(row, marker)
