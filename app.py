from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route("/")
def index():
    conn = get_db_connection()
    interviews = conn.execute("SELECT * FROM interviews").fetchall()
    conn.close()
    return render_template("index.html", interviews=interviews)

# Add interview route
@app.route("/add", methods=("GET", "POST"))
def add():
    if request.method == "POST":
        candidate_name = request.form["candidate_name"]
        company_name = request.form["company_name"]
        application_date = request.form["application_date"]
        status = request.form["status"]
        notes = request.form["notes"]

        conn = get_db_connection()
        conn.execute(
            "INSERT INTO interviews (candidate_name, company_name, application_date, status, notes) VALUES (?, ?, ?, ?, ?)",
            (candidate_name, company_name, application_date, status, notes),
        )
        conn.commit()
        conn.close()
        return redirect("/")
    return render_template("add_interview.html")

# Edit interview route
@app.route("/edit/<int:id>", methods=("GET", "POST"))
def edit(id):
    conn = get_db_connection()
    interview = conn.execute("SELECT * FROM interviews WHERE id = ?", (id,)).fetchone()

    if request.method == "POST":
        candidate_name = request.form["candidate_name"]
        company_name = request.form["company_name"]
        application_date = request.form["application_date"]
        status = request.form["status"]
        notes = request.form["notes"]

        conn.execute(
            "UPDATE interviews SET candidate_name = ?, company_name = ?, application_date = ?, status = ?, notes = ? WHERE id = ?",
            (candidate_name, company_name, application_date, status, notes, id),
        )
        conn.commit()
        conn.close()
        return redirect("/")
    conn.close()
    return render_template("edit_interview.html", interview=interview)

# Delete interview route
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM interviews WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

