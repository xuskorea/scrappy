import os

from flask import Flask, json, jsonify
from exercises import factorial, isPalindrome
from scrapper.scrappy import get_teams
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "teamdatabase.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Team(db.Model):
    __tablename__ = 'teams'
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    points = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)
    games_played = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    win = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    draw = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)
    lose = db.Column(db.String(80), unique=False, nullable=True, primary_key=False)


db.create_all()


def to_dic(team):
    data = {}
    data["name"] = team.name
    data["points"] = team.points
    data["games_played"] = team.games_played
    data["win"] = team.win
    data["draw"] = team.draw
    data["lose"] = team.lose
    return data


def data_to(data):
    return Team(name=data["name"], points=data["points"], games_played=data["games_played"], win=data["win"],
                draw=data["draw"], lose=data["lose"])


@app.route("/index")
def index():
    try:
        teams = [data_to(team) for team in get_teams()]
        db.session.add_all(teams)
        db.session.commit()
    except Exception as e:
        print(e)
        print("Failed to add teams")
    return "Indexed!"


@app.route("/teams")
def teams():
    teams = Team.query.all()
    return json.dumps([to_dic(team) for team in teams])


@app.route("/factorial/<int:number>")
def factorial(number):
    return str(factorial(number))


@app.route("/palindrome/<string:palindrome>")
def palindrome(palindrome):
    return isPalindrome(palindrome)


if __name__ == "__main__":
    app.run(debug=True)
