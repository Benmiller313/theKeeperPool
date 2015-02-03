from django.core.management.base import BaseCommand, CommandError
from teampages.models import Team
from teampages.ODSUtil.ODSReader import ODSReader



class Command(BaseCommand):
    help = 'Builds the team tables'

    def handle(self, *args, **options):
        for team_name in [team.name for team in Team.objects.all()]:
            print team_name
            db = ODSReader("keeperpool20142015.ods")
            sheet =  db.getSheet(team_name + "'s Team")
            roster = {"F" : [], "D" : [], "G": []}
            lineup = {"F" : [], "D" : [], "G": []}
            picks = {}

            for row in sheet: 
                try:
                    roster[row[0]].append([row[0], row[1], row[2]])
                except:
                    pass
                try:
                    lineup[row[3]].append([row[3], row[4], row[5]])
                except:
                    pass
                try:
                    picks.setdefault(row[6], []).append(row[7])
                except:
                    pass

            self.createRoster(roster, team_name)
            self.createLineup(lineup, team_name)
            self.createPicks(picks, team_name)

    def createRoster(self, roster, team_name):
        with open("teampages/templates/teampages/teams/rosters/"+team_name+".html", "w") as f:
            f.write("<tbody>\n")
            f.write("<tr>\n")
            f.write('<td class="position-cell" align="middle" rowspan="15">F</td>\n')
            f.write("<td >{name}</td><td >${salary}</td>\n".format(name=roster["F"][0][1], salary=roster["F"][0][2]))    
            f.write("</tr>\n")        
            for player in roster["F"][1:]:
                f.write("<tr>\n")
                f.write("<td >{name}</td>\n".format(name=player[1]))
                f.write("<td >${salary}</td>\n".format(salary=player[2]))
                f.write("</tr>\n")
            f.write("<tr>\n")
            f.write('<td class="position-cell" align="middle" rowspan="7">D</td>\n')
            f.write("<td >{name}</td><td >${salary}</td>\n".format(name=roster["D"][0][1], salary=roster["D"][0][2]))    
            f.write("</tr>\n")        
            for player in roster["D"][1:]:
                f.write("<tr>\n")
                f.write("<td >{name}</td>\n".format(name=player[1]))
                f.write("<td >${salary}</td>\n".format(salary=player[2]))
                f.write("</tr>\n")
            f.write("<tr>\n")
            f.write('<td class="position-cell" align="middle" rowspan="4">G</td>\n')
            f.write("<td >{name}</td><td >${salary}</td>\n".format(name=roster["G"][0][1], salary=roster["G"][0][2]))    
            f.write("</tr>\n")        
            for player in roster["G"][1:]:
                f.write("<tr>\n")
                f.write("<td >{name}</td>\n".format(name=player[1]))
                f.write("<td >${salary}</td>\n".format(salary=player[2]))
                f.write("</tr>\n")
            f.write("</tbody>\n")
            f.write("<tfoot>\n")
            f.write("<tr><td></td><td>Salary:</td><td>${salary}</td></tr>\n".format(salary=format(int(self.calculateSalary(roster)), ",d")))
            f.write("<tr><td></td><td>Forwards:</td><td>{forwards}</td></tr>\n".format(forwards=len(roster["F"])))
            f.write("<tr><td></td><td>Defence:</td><td>{defence}</td></tr>\n".format(defence=len(roster["D"])))
            f.write("<tr><td></td><td>Goalies:</td><td>{goalies}</td></tr>\n".format(goalies=len(roster["G"])))
            f.write("</tfoot>\n")

    def createLineup(self, lineup, team_name):        
        with open("teampages/templates/teampages/teams/lineups/"+team_name+".html", "w") as f:
            f.write("<tbody>\n")
            f.write("<tr>\n")
            f.write('<td class="position-cell" align="middle" rowspan="9">F</td>\n')
            f.write("<td >{name}</td><td >${salary}</td>\n".format(name=lineup["F"][0][1], salary=lineup["F"][0][2]))    
            f.write("</tr>\n")        
            for player in lineup["F"][1:]:
                f.write("<tr>\n")
                f.write("<td >{name}</td>\n".format(name=player[1]))
                f.write("<td >${salary}</td>\n".format(salary=player[2]))
                f.write("</tr>\n")
            f.write("<tr>\n")
            f.write('<td class="position-cell" align="middle" rowspan="4">D</td>\n')
            f.write("<td >{name}</td><td >${salary}</td>\n".format(name=lineup["D"][0][1], salary=lineup["D"][0][2]))    
            f.write("</tr>\n")        
            for player in lineup["D"][1:]:
                f.write("<tr>\n")
                f.write("<td >{name}</td>\n".format(name=player[1]))
                f.write("<td >${salary}</td>\n".format(salary=player[2]))
                f.write("</tr>\n")
            f.write("<tr>\n")
            f.write('<td class="position-cell" align="middle" rowspan="2">G</td>\n')
            f.write("<td >{name}</td><td >${salary}</td>\n".format(name=lineup["G"][0][1], salary=lineup["G"][0][2]))    
            f.write("</tr>\n")        
            for player in lineup["G"][1:]:
                f.write("<tr>\n")
                f.write("<td >{name}</td>\n".format(name=player[1]))
                f.write("<td >${salary}</td>\n".format(salary=player[2]))
                f.write("</tr>\n")
            f.write("</tbody>\n")
            f.write("<tfoot>\n")
            f.write("<tr><td></td><td>Salary:</td><td>${salary}</td></tr>\n".format(salary=format(int(self.calculateSalary(lineup)), ",d")))
            f.write("<tr><td></td><td>Forwards:</td><td>{forwards}</td></tr>\n".format(forwards=len(lineup["F"])))
            f.write("<tr><td></td><td>Defence:</td><td>{defence}</td></tr>\n".format(defence=len(lineup["D"])))
            f.write("<tr><td></td><td>Goalies:</td><td>{goalies}</td></tr>\n".format(goalies=len(lineup["G"])))
            f.write("</tfoot>\n")

    def createPicks(self, picks, team_name):
        with open("teampages/templates/teampages/teams/picks/"+team_name+".html", "w", ) as f:
            for year, picks in picks.iteritems():
                if len(picks) > 0:
                    f.write('<div class="col-md-3">\n')
                    f.write('<table class="table">\n')
                    f.write('<tbody>\n')
                    f.write('<tr>\n')
                    f.write('<td class="position-cell" align="middle" rowspan="{numpicks}">{year}</td>\n'.format(numpicks=len(picks), year=year))
                    f.write('<td>{pick}</td>\n'.format(pick=picks[0]))
                    f.write('</tr>')
                    for pick in picks[1:]:
                        f.write('<tr>\n')
                        f.write('<td>{pick}</td>\n'.format(pick=pick))
                        f.write('</tr>\n')
                    f.write('</tbody>\n')
                    f.write('</table>\n')
                    f.write('</div>\n')


    def calculateSalary(self, players):
        salary = 0
        for position, players in players.iteritems():
            for player in players:
                salary += float(player[2].replace(",", ""))
        return salary





