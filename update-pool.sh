#! /bin/bash

git pull
python manage.py loadTeamData
python manage.py loadStatData