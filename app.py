# Bismillah al-Rahmaan al-Raheem
# Ali Shah | Oct. 29, 2020
# WEB1.1 Assignment 1: Request/Response

from flask import Flask
from random import randint

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

@app.route("/sayntimes/<word>/<n>")
def sayntimes(word, n):
    """Displays a word repeatedly based on user's input"""

    if word.isalpha() and n.isdigit():
        n = int(n)
        ntimes = f"{word} " * n
        return ntimes
    else:
        return "Invalid input. Please try again by entering a word and a number!"

@app.route("/reverse/<string>")
def reverse(string):
    """Displays a string in reverse order based on user's input"""
    return string[::-1]

@app.route("/strangecaps/<string>")
def strangecaps(string):
    """Displays characters of a string in alternating case based on user's input"""

    if string[0].islower():
        switch = True
    else:
        switch = False

    strangecaps = ""

    for char in string:
        if switch:
            strangecaps += char.lower()
        else:
            strangecaps += char.upper()
        switch = not switch

    return strangecaps

@app.route("/dicegame")
def dicegame():
    """Generates a number between 1-6; displays a message based on output"""
    num = randint(1, 6)
    msg = "won" if num == 6 else "lost"
    return f"You rolled a {num}. You {msg}!"

if __name__ == "__main__":
    app.run(debug=True)
