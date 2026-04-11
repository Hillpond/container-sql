import sqlite3

conn = sqlite3.connect('bedrift.db')
c = conn.cursor()

# Lag en tabell
c.execute('''CREATE TABLE ansatte (id INTEGER PRIMARY KEY, navn TEXT, rolle TEXT, lonn INTEGER)''')

# Legg inn data
ansatte = [
    (1, 'Ole', 'Utvikler', 500000),
    (2, 'Lise', 'Prosjektleder', 600000),
    (3, 'Hemmelig_Bruker', 'Admin', 999999)
]

c.executemany('INSERT INTO ansatte VALUES (?,?,?,?)', ansatte)

conn.commit()
conn.close()
print("Database opprettet!")