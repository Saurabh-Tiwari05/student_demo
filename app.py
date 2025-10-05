from flask import Flask, render_template, request, redirect
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Function to connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT")
    )

# Home route with student registration form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        age = request.form["age"]

        # Insert data into database
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, email, age) VALUES (%s, %s, %s)",
            (name, email, age)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
