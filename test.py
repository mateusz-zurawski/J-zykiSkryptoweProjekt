import sqlite3
con = sqlite3.connect('database.db')
cur = con.cursor()

files = []
for row in cur.execute('SELECT file_name FROM ways group by file_name'):
        files.append(row[0])
        print(row)
print(files)
