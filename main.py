from gevent import monkey

# Monkey-patching standart Python library for async working
monkey.patch_all()

# Import WSGI server from Gevent
from gevent.pywsgi import WSGIServer

# Import Compress module from Flask-Compress for compress static content (HTML, CSS, JS)
from flask_compress import Compress

from flask import Flask, render_template, request, redirect
import sqlite3
import requests


app = Flask(__name__)


# Create Compress with default params
compress = Compress()

# Init compress for our Flask app
compress.init_app(app)

def create_table():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    # Changing database to include likes and dislikes
     
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        answer TEXT NOT NULL,
        likes INTEGER,
        dislikes INTEGER
    );
    """)

    conn.commit()
    conn.close()

@app.route("/")
def index():
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM questions")
    questions = cursor.fetchall()

    conn.close()

    return render_template("index.html", questions=questions)  
    # cursor = conn.cursor()

@app.route("/add", methods=["GET", "POST"])
def add_question():
    if request.method == "POST":
        question = request.form["question"].lower()
        answer = request.form["answer"].lower()

        # Removing the profanity filter from here 

        # swear_words = ["arse", "arsehole", "as useful as tits on a bull", "balls", "bastard", "beaver", "beef curtains", "bell", "bellend", "bent", "berk", "bint", "bitch", "blighter", "blimey", "blimey o'reilly", "bloodclaat", "bloody", "bloody hell", "blooming", "bollocks", "bonk", "bugger", "bugger me", "bugger off", "built like a brick shit-house", "bukkake", "bullshit", "cack", "cad", "chav", "cheese eating surrender monkey", "choad", "chuffer", "clunge", "cobblers", "cock", "cock cheese", "cock jockey", "cock-up", "cocksucker", "cockwomble", "codger", "cor blimey", "corey", "cow", "crap", "crikey", "cunt", "daft", "daft cow", "damn", "dick", "dickhead", "did he bollocks!", "did i fuck as like!", "dildo", "dodgy", "duffer", "fanny", "feck", "flaps", "fuck", "fuck me sideways!", "fucking cunt", "fucktard", "gash", "ginger", "git", "gob shite", "goddam", "gorblimey", "gordon bennett", "gormless", "he’s a knob", "hell", "hobknocker", "I'd rather snort my own cum", "jesus christ", "jizz", "knob", "knobber", "knobend", "knobhead", "ligger", "like fucking a dying man's handshake", "mad as a hatter", "manky", "minge", "minger", "minging", "motherfucker", "munter", "muppet", "naff", "nitwit", "nonce", "numpty", "nutter", "off their rocker", "penguin", "pillock", "pish", "piss off", "piss-flaps", "pissed", "pissed off", "play the five-fingered flute", "plonker", "ponce", "poof", "pouf", "poxy", "prat", "prick", "prick", "prickteaser", "punani", "punny", "pussy", "randy", "rapey", "rat arsed", "rotter", "scrubber", "shag", "shit", "shite", "shitfaced", "skank", "slag", "slapper", "slut", "snatch", "sod", "sod-off", "son of a bitch", "spunk", "stick it up your arse!", "swine", "taking the piss", "tits", "toff", "tosser", "trollop", "tuss", "twat", "twonk", "u fukin wanker", "wally", "wanker", "wankstain", "wazzack", "whore"]

        # for word in swear_words:
        #     if word in question or word in answer:
        #         return f"Error: Question or answer contains the word, `{word}` which cannot be used in this website."


        # Validate reCAPTCHA response
        recaptcha_response = request.form.get("g-recaptcha-response")
        secret_key = "your-secret-key-here"
        verify_url = f"https://www.google.com/recaptcha/api/siteverify?secret={secret_key}&response={recaptcha_response}"
        response = requests.get(verify_url)
        result = response.json()

        # Check if reCAPTCHA validation was successful
        if not result["success"]:
            return "Error: reCAPTCHA validation failed. Please solve the captcha and then click submit."

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO questions (question, answer, likes, dislikes) VALUES (?, ?, 0, 0)", (question, answer))
        # Initializing the number of likes and dislikes to 0
        # They will incremented whenever the respective buttons are pressed

        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add_question.html")

if __name__ == "__main__":
    create_table()
    http_server = WSGIServer(('0.0.0.0', 8080), app)
http_server.serve_forever()