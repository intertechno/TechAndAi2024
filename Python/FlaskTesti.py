from datetime import datetime
from flask import Flask, json
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World! Moi Flask!</h1>"

@app.route("/kellonaika")
def palauta_kellonaika():
    return str(datetime.now())

@app.route("/asiakkaat")
def hae_sql_asiakkaat():
    con = sqlite3.connect("Northwind.db")
    try:
        cur = con.cursor()
        sql = "SELECT * FROM Customers"
        res = cur.execute(sql)
        tulokset = res.fetchall()
    finally:
        cur.close()
        con.close()
    return json.jsonify(tulokset)
