from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_menu = request.form.get("menu")
    input_year = request.form.get("year")
    input_guests = request.form.get("guests")
    input_donation = request.form.get("donation")
    return render_template("hello.html", name=input_name, menu=input_menu, year = input_year, guests = input_guests, donation = input_donation)