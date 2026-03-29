from flask import Flask, render_template
import sqlite3
import pandas as pd
from flask import request, redirect


app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("database/sales.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return df.to_dict(orient="records")

@app.route('/')
def home():
    data = get_data()
    return render_template("index.html", data=data)
@app.route('/add', methods=['POST'])
def add():
    product = request.form['product']
    region = request.form['region']
    category = request.form['category']
    sales = request.form['sales']

    conn = sqlite3.connect("database/sales.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sales (product, region, category, sales)
    VALUES (?, ?, ?, ?)
    """, (product, region, category, sales))

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
