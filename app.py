"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template, flash, redirect, request
from markov import MarkovbutBetter
from tokens import tokenize
import twitter


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    tokens = tokenize('sample.txt')
    mark = MarkovbutBetter(tokens)



@app.route("/")
def tweet():
    sentence = request.form['sentence']
    print(sentence)
    status = twitter.tweet(sentence)
    print(status)
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
