from tabulate import tabulate # type: ignore
from data_scraper import web_scraper

def create_table(contestants, selections):
    dicti = {contestants[x]:selections[x] for x in range(len(contestants))}
    batsmen = web_scraper("https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946")
    bowlers = web_scraper("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2024-15946")
    batterList = []
    bowlerList = []
    
    for d in dicti:
        try:
            batterList.append([d,dicti[d][0],batsmen[dicti[d][0]]])
        except KeyError:
            batterList.append([d,dicti[d][0],f"{min(batsmen.values())}"])
        try:
            bowlerList.append([d,dicti[d][1],bowlers[dicti[d][1]]])
        except KeyError:
            bowlerList.append([d,dicti[d][1],f"{min(bowlers.values())}"])
    
    return(batterList, bowlerList)