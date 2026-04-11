import sqlite3
import os

def sjekk_oppgave():
    if not os.path.exists('bedrift.db'):
        print("Feil: Finner ikke bedrift.db!")
        return

    conn = sqlite3.connect('bedrift.db')
    c = conn.cursor()

    # Vi sjekker om 'Hemmelig_Bruker' fortsatt eksisterer
    c.execute("SELECT * FROM ansatte WHERE navn='Hemmelig_Bruker'")
    resultat = c.fetchone()

    if resultat is None:
        print("-" * 30)
        print("BRA JOBBA! Du har slettet bevisene.")
        print("Din nøkkel til quizen er: SQL_MASTER_2024")
        print("-" * 30)
    else:
        print("Nja... Hemmelig_Bruker ligger fortsatt i databasen. Prøv igjen!")

    conn.close()

if __name__ == "__main__":
    sjekk_oppgave()