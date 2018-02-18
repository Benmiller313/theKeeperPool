import requests

from constants import URL_ROOT
from season import Season

class Schedule(object):

    schedule_url = "{}{}".format(URL_ROOT, "/api/v1/schedule")

    def __init__(self, team_id, start_date=None, end_date=None):
        if not start_date or not end_date:
            if start_date or end_date:
                raise ValueError("Must provide both start and end date, or neither")
            current_season = Season()
            start_date = current_season.regular_season_start
            end_date = current_season.regular_season_end

        params = {
            "teamId": team_id,
            "startDate": start_date,
            "endDate": end_date,
        }

        resp = requests.get(Schedule.schedule_url, params=params)
        schedule_data = resp.json()

        self.total_games = schedule_data["totalGames"]
