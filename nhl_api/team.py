import requests

from constants import URL_ROOT
from player import Player
from schedule import Schedule


class Team(object):

    teams_url = URL_ROOT + "/api/v1/teams/"

    def __init__(self, id):
        self.id = id

        resp = requests.get("{}{}".format(Team.teams_url,id))
        team_data = resp.json()["teams"][0]
        self.name = team_data["name"]
        self.abbreviation = team_data["abbreviation"]
        self.url = team_data["link"]

        resp = requests.get(URL_ROOT + self.url + "/roster")
        roster_data = resp.json()["roster"]
        self._roster_ids = [player["person"]["id"] for player in roster_data]

    def roster(self):
        for player_id in self._roster_ids:
            yield Player(player_id)

    def schedule(self, start_date=None, end_date=None):
        return Schedule(self.id, start_date, end_date)
