from flask import Flask, render_template, request
import re
import requests
import datetime
import os
from openai import OpenAI
import random

client = OpenAI()


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


@app.route("/github_input", methods=["GET"])
def github_input():
    return render_template(
        "github_input.html",
    )


@app.route("/github_info", methods=["POST"])
def github_submit():
    input_github_username = request.form.get("username")

    response = requests.get(
        f"https://api.github.com/users/{input_github_username}/repos"
    )
    if response.status_code == 200:
        repos = response.json()
        data = {}

        for repo in repos:
            name = repo["name"]
            full_name = repo["full_name"]
            commits_url = f"https://api.github.com/repos/{full_name}/commits"
            commits_response = requests.get(commits_url)

            latest_commit_data = {}
            if commits_response.status_code == 200:
                commits_data = commits_response.json()
                if commits_data:
                    latest_commit = commits_data[0]
                    latest_commit_data = {
                        "hash": latest_commit["sha"],
                        "author": latest_commit["commit"]["author"]["name"],
                        "date": format_date(latest_commit["commit"]["author"]["date"]),
                        "message": latest_commit["commit"]["message"],
                    }
                


            data[name] = {
                "updated_at": format_date(repo["updated_at"]),
                "pushed_at": format_date(repo["pushed_at"]),
                "latest_commit": latest_commit_data,
            }
            
    return render_template(
        "github_info.html", username=input_github_username, data=data
    )


@app.route("/chatgpt_compliment_generator", methods=["GET"])
def compliment_page():
    return render_template(
        "compliment.html",
    )


@app.route("/chatgpt_get_compliment", methods=["POST"])
def generate_compliment():
    compliment_list = ["programming abilities", "smile", "personality", "style", "intellect",
    "kindness", "wisdom", "ability", "aptitude", "cooking ability", "athelticism","wit",
    "confidence", "friendliness", "ambition"]

    user_message = "Please give me a compliment relating to my " + random.choice(compliment_list) + "."
    

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a kind individual, who uses beautiful language."},
    {"role": "user", "content": user_message}],
    temperature = 0.7
    )
    try:
        compliment = response.choices[0].message.content
    except:
        return "An error has occurred, please try again later."
    return compliment


def process_query(entity: str) -> str:
    if entity == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif entity == "asteroids":
        return "Unknown"
    elif entity == "What is your name?":
        return "james_ankur"
    elif entity.startswith("Which of the following numbers is the largest"):
        numbers = [int(num) for num in re.findall(r"\d+", entity)]
        last_three_numbers = numbers[-3:]
        largest = max(last_three_numbers)
        return str(largest)
    elif "What is" in entity and "plus" in entity:
        numbers = [int(num) for num in re.findall(r"\d+", entity)]
        last_two_numbers = numbers[-2:]
        total = sum(last_two_numbers)
        return str(total)
    elif "What is" in entity and "multiplied" in entity:
        numbers = [int(num) for num in re.findall(r"\d+", entity)]
        last_two_numbers = numbers[-2:]
        result = last_two_numbers[0] * last_two_numbers[1]
        return str(result)
    elif "What is" in entity and "minus" in entity:
        numbers = [int(num) for num in re.findall(r"\d+", entity)]
        last_two_numbers = numbers[-2:]
        total = result = last_two_numbers[0] - last_two_numbers[1]
        return str(total)

    elif entity.startswith(
        "Which of the following numbers is both a square and a cube:"
    ):
        numbers = [int(num) for num in re.findall(r"\d+", entity)]
        output = ""
        for num in numbers:
            if is_cube(num) and is_square(num):
                output = output + str(num) + ", "
        return output[:-2]

    elif entity.startswith("Which of the following numbers are primes"):
        numbers = [int(num) for num in re.findall(r"\d+", entity)]
        output = ""
        for num in numbers:
            if is_prime(num):
                output = output + str(num) + ", "
        return output[:-2]

    return "Please query for dinosaurs or asteroids!"


@app.route("/query", methods=["GET"])
def query():
    q = request.args.get("q")
    info = process_query(q)
    if q == "dinosaurs":
        return render_template("dinosaurs.html", entity=q, info=info)
    elif q == "asteroids":
        return render_template("asteroids.html", entity=q, info=info)
    elif info == "Please query for dinosaurs or asteroids!":
        return render_template("others.html", entity=q, info=info)

    return info


def is_cube(number):
    cube_root = round(number ** (1 / 3))
    return cube_root**3 == number


def is_square(number):
    sq_root = round(number ** (1 / 2))
    return sq_root**2 == number


def is_prime(number):
    if number == 1 or number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
    return True


# With help from : https://stackoverflow.com/questions/18795713/parse-and-format-the-date-from-the-github-api-in-python
def format_date(date_string):
    date = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
    date = date.strftime("%a %b %d, %Y at %H:%M GMT")
    return date
