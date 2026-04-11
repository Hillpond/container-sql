from flask import Flask, render_template, request, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "superhemmelig_nøkkel"  # For å vise meldinger (flashing)
DB_NAME = 'bedrift.db'


def init_db():
    """Oppretter databasen på nytt hver gang vi starter appen (valgfritt)"""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('CREATE TABLE ansatte (id INTEGER PRIMARY KEY, navn TEXT, rolle TEXT, lonn INTEGER)')
    ansatte = [
        (1, 'Ole', 'Utvikler', 500000),
        (2, 'Lise', 'Prosjektleder', 600000),
        (3, 'Hemmelig_Bruker', 'Admin', 999999)
    ]
    c.executemany('INSERT INTO ansatte VALUES (?,?,?,?)', ansatte)
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    status_melding = ""
    sql_query = ""
    tabell_data = []

    if request.method == 'POST':
        sql_query = request.form.get('sql_query')

        try:
            conn = sqlite3.connect(DB_NAME)
            c = conn.cursor()

            # Kjør brukerens SQL
            c.execute(sql_query)
            conn.commit()

            # Sjekk om 'Hemmelig_Bruker' er borte (Validering)
            c.execute("SELECT * FROM ansatte WHERE navn='Hemmelig_Bruker'")
            if c.fetchone() is None:
                status_melding = "BRA JOBBA! Du har slettet bevisene. Nøkkel: SQL_MASTER_2024"
            else:
                status_melding = "Nja... Hemmelig_Bruker ligger fortsatt i databasen. Prøv igjen!"

            # Hent ut tabellen for å vise fremgangen
            c.execute("SELECT * FROM ansatte")
            tabell_data = c.fetchall()
            conn.close()

        except Exception as e:
            status_melding = f"Feil i SQL: {e}"

    return render_template('index.html', melding=status_melding, data=tabell_data, query=sql_query)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)