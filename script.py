import json
import requests
import time
import yaml

config = yaml.load(file("settings.yml"))

teams_file = open('teams.txt')
teams = []

for line in teams_file:
    teams.append(line.strip())

github_url = "https://api.github.com/repos/rosedu/{0}/stats/contributors"
data = "<html><body><h1>Facebook Hackathon - Number of commits</h1><ul>"

for team in teams:
    req = requests.get(github_url.format(team), auth=(config['user'], config['password']))
    response = json.loads(req.content)
    noCommits = 0
    noLOC = 0

    for author in response:
        try:
            noCommits += author['total']
            noLOC += author['weeks'][0]['a'] + author['weeks'][0]['d']
        except:
            pass

    data += "<li>{0} - {1}</li>".format(team, noCommits)
    time.sleep(3)
data += "</ul></body></html>"

print data
