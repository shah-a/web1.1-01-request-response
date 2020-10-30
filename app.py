# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Oct. 29, 2020
# WEB1.1 Assignment 1: Request/Response

from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    """Shows a greeting to the user"""
    return "Are you there, world? It's me, Ducky!"

@app.route("/penguins")
def penguins():
    """Route for penguin input"""
    return "Penguins are cute!"

@app.route("/dragons")
def dragons():
    """Route for dragon input"""
    return "Dragons are cool!"

@app.route("/animal/<users_animal>")
def favourite_animal(users_animal):
    """Display a message that changes based on user's animal input"""
    return f"Wow, {users_animal} are wonderful!"

@app.route("/dessert/<users_dessert>")
def favourite_dessert(users_dessert):
    """Display a message that changes based on user's dessert input"""
    return f"How did you know I liked {users_dessert}?"

@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    """Display a story based on user's adjective and noun inputs"""
    story = f"I need to write a funny story, but the {adjective} {noun} is chasing me!"
    return story

@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    """Displays the product of two numbers based on user's input"""

    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)
        result = number1 * number2
        calc = f"{number1} times {number2} is {result}."
        return calc
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

if __name__ == "__main__":
    app.run(debug=True)
