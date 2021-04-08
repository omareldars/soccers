class Soccer:
    teamName=""
    noWin=0
    noLos=0
    totalTeams=0
    def __init__(self,tname,win,los):
        self.teamName = tname
        self.noWin = win
        self.noLos = los
        self.totalTeams = self.totalTeams + 1

    def incWins(self): 
        self.noWin = self.noWin + 1
        return self.noWin
        
    def goodRecords(self):
        if self.noWin > 20 and self.noLos < 5:
            return True
        else:
            return False

    def __str__(self):
        print("Team Name: ",self.teamName," , Number of Wins : ",self.noWin, " , Number of Loses : ",self.noLos)


class YouthSoccer(Soccer):
    def __init__(self,tname,win,los):
        super().__init__(tname,win,los)

    def goodRecords(self):
        if self.noWin > self.noLos:
            return True
        else:
            return False




def main():

    soccers = []
    soccers.append(Soccer("team1",10,20))
    soccers.append(Soccer("team2",30,5))
    soccers.append(YouthSoccer("team3",7,2))

    print("Total Created Teams = ",Soccer.totalTeams)
    soccers[::-1]
    # soccer = reversed(soccers,reverse=True)
    for i in soccers:
        i.__str__()


main()