import sqlite3

print("Aloitetaan SQLite-tietokannan käsittely.")
con = sqlite3.connect("Henkilöt.db")

cur = con.cursor()
cur.execute("CREATE TABLE henkilo(nimi, osoite, maa)")
print("Tietokantataulu luotu.")

cur.execute("""
    INSERT INTO henkilo VALUES
        ('Erkki Esimerkki', 'Kotikatu 12 B', 'Suomi'),
        ('Antti Asiakas', 'Mäntykuja 33 C 2', 'Suomi')
""")
print("Henkilöitä lisättty.")

con.commit()
con.close()
print("Commit-komento suoritettu.")

print("SQLite-tietokannan käsittely on päättynyt.")
