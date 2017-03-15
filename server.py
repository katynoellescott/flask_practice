from flask import Flask, request
from random import choice, randint


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

@app.route('/')
def index():
    """Home page."""

    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    """Say hello"""

    return "<html><body><h2>Heya!</h2></body></html>" #add code here to greet user

@app.route('/lucky')
def lucky_number():
    """Provides a random lucky number"""
    lucky_num= randint(1,21) # add code here of getting a lucky number and return a string
    lucky_message= "Your lucky number is %s." % lucky_num # with the lucky number

    return "<html><body><h3>%s</h3></body></html>" % lucky_message

@app.route('/psychic')
def psychic_prediction():
    '''Magic 8 Ball emulator'''
    c = ["Outcome looks good", "Ask again later", "For sure", "Definitely not"]
    prediction = choice(c)
    return """<html><body><img src="/static/cat.jpg"><h3>%s</h3></body></html>""" %prediction    


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
