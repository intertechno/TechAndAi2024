import sqlite3

con = sqlite3.connect("Northwind.db")
cur = con.cursor()

sql = "SELECT * FROM Customers"
res = cur.execute(sql)
tulokset = res.fetchall()
con.close()

print(tulokset)
