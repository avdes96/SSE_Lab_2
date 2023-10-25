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
    return render_template(
        "form_submit_page.html",
        name=input_name,
        menu=input_menu,
        year=input_year,
        guests=input_guests,
        donation=input_donation,
    )


def process_query(entity: str) -> str:
    if entity == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif entity == "asteroids":
        return "Unknown"
    return "Please query for dinosaurs or asteroids!"


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    info = process_query(q)
    if q == "dinosaurs":
        return render_template("dinosaurs.html", entity=q, info=info)
    elif q == "asteroids":
        return render_template("asteroids.html", entity=q, info=info)
    else:
        return render_template("others.html", entity=q, info=info)
