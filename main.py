from summoner.Summoner import  Summoner

s = Summoner("Tsukuyõmi", "la1")
print(s.__str__())
matchs = s.get_matchs()
for match in matchs:
    print(match)
    