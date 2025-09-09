from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, upper=True, lower=True, numbers=True, symbols=True):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Select at least one option!"

    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        upper = request.form.get("uppercase") == "on"
        lower = request.form.get("lowercase") == "on"
        numbers_chk = request.form.get("numbers") == "on"
        symbols_chk = request.form.get("symbols") == "on"
        password = generate_password(length, upper, lower, numbers_chk, symbols_chk)
    return render_template("index.html", password=password)
from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length=12, upper=False, lower=False, numbers=False, symbols=False):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Select at least one option!"

    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    length = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        upper = request.form.get("uppercase") == "on"
        lower = request.form.get("lowercase") == "on"
        numbers_chk = request.form.get("numbers") == "on"
        symbols_chk = request.form.get("symbols") == "on"
        password = generate_password(length, upper, lower, numbers_chk, symbols_chk)
    return render_template("index.html", password=password, length=length)

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
