from flask import Flask, render_template, request
import re

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


def process_query(entity):
    if entity == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif entity == "asteroids":
        return "Unknown"
    elif entity == "What is your name?":
        return "james_ankur"
    elif entity.startswith("Which of the following numbers is the largest"):
        numbers = [int(num) for num in re.findall(r'\d+', entity)]
        last_three_numbers = numbers[-3:]
        largest = max(last_three_numbers)
        return str(largest)
    elif "What is" in entity and "plus" in entity:
        numbers = [int(num) for num in re.findall(r'\d+', entity)]
        last_two_numbers = numbers[-2:]
        total = sum(last_two_numbers)
        return str(total)
    elif "What is" in entity and "multiplied" in entity:
        numbers = [int(num) for num in re.findall(r'\d+', entity)]
        last_two_numbers = numbers[-2:]
        product = product(last_two_numbers)
        return str(product)

    return "Please query for dinosaurs or asteroids!"

@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    info = process_query(q)
    return info