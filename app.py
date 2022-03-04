"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, redirect, render_template
from markov import MarkovbutBetter
from tokens import tokenize
import twitter


app = Flask(__name__)


@app.before_first_request
def before_first_request():
    """Runs only once at Flask startup"""
    # TODO: Initialize your histogram, hash table, or markov chain here.
    tokens = tokenize('sample.txt')
    mark = MarkovbutBetter



@app.route("/")
def home():
    corpus = open("sample.txt", "r").read()
    source = tokenize(corpus)    
    markov = MarkovbutBetter(source)
    sentence = markov.walk()
     
    return render_template('index.html', sentence = sentence)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['sentence']
    twitter.tweet(status)
    return redirect('/')


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
