import requests

from constants import URL_ROOT


class Season(object):

    seasons_url = "{}{}".format(URL_ROOT, "/api/v1/seasons/")

    def __init__(self, season_id=None):
        if not season_id:
            # Fetch the most recent season
            resp = requests.get(Season.seasons_url)
            season_data = resp.json()["seasons"][-1]
        else:
            resp = requests.get("{}{}".format(Season.seasons_url, season_id))
            season_data = resp.json()["seasons"][0]

        self.season_id = season_data["seasonId"]
        self.regular_season_start = season_data["regularSeasonStartDate"]
        self.regular_season_end = season_data["regularSeasonEndDate"]
