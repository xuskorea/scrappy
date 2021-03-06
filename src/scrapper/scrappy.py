import requests


from bs4 import BeautifulSoup

url = 'https://www.resultados-futbol.com/segundab'


def get_teams():


    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find(id="tabla2")
    rows = table.find_all('tr')
    teams = []

    for row in rows[1:]:
        team = {}
        name = row.find("td", class_="equipo sube")
        if(name == None):
            name = row.find("td", class_="equipo")
        team["name"] = name.find("a").getText()

        point = row.find("td",class_="pts")
        team["points"] = point.getText()

        games_played = row.find("td", class_="pj")
        team["games_played"] = games_played.getText()

        win = row.find("td", class_="win")
        team["win"] = win.getText()

        draw = row.find("td", class_="draw")
        team["draw"] = draw.getText()

        lose = row.find("td", class_="lose")
        team["lose"] = lose.getText()
        teams.append(team)
    return teams




