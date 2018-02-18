import requests

from constants import URL_ROOT

class Player(object):

    players_url = URL_ROOT + "/api/v1/people/"

    def __init__(self, id):
        self.id = id

        resp = requests.get("{}{}".format(Player.players_url, self.id))
        player_data = resp.json()["people"][0]

        self.full_name = player_data["fullName"]
        self.first_name = player_data["firstName"]
        self.last_name = player_data["lastName"]
        self.primary_number = player_data["primaryNumber"]
        self.birth_date = player_data["birthDate"]
        self.age = player_data["currentAge"]
        self.primary_position = player_data["primaryPosition"]
        self.team_id = player_data["currentTeam"]["id"]

    @property
    def team(self):
        from team import Team
        return Team(self.team_id)

