from flask import Flask
from exercises import factorial,isPalindrome
from scrappy import get_teams

app = Flask(__name__)


@app.route("/index")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return get_teams()


@app.route("/factorial/<int:number>")
def factorial(number):
    return str(factorial(number))

@app.route("/palindrome/<string:palindrome>")
def palindrome(palindrome):
    return isPalindrome(palindrome)



if __name__ == "__main__":
    app.run()