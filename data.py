from tabulate import tabulate # type: ignore
from data_scraper import web_scraper

def create_table(contestants, selections):
    dicti = {contestants[x]:selections[x] for x in range(len(contestants))}
    batsmen = web_scraper("https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-men-s-t20-world-cup-2024-15946")
    bowlers = web_scraper("https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-men-s-t20-world-cup-2024-15946")
    batterList = []
    bowlerList = []
    #batterList.append(["Name", "Batsmen", "Runs"])
    #bowlerList.append(["Name", "Bowler", "Wickets"])
    
    for d in dicti:
        try:
            batterList.append([d,dicti[d][0],batsmen[dicti[d][0]]])
        except KeyError:
            batterList.append([d,dicti[d][0],f"<{min(batsmen.values())}"])
        try:
            bowlerList.append([d,dicti[d][1],bowlers[dicti[d][1]]])
        except KeyError:
            bowlerList.append([d,dicti[d][1],f"<{min(bowlers.values())}"])
    
    return(batterList, bowlerList)#+list_to_html_table(bowlerList[1:],bowlerList[0]))
    #print(tabulate(batterList,tablefmt='html'))

def list_to_html_table(data, columns=None):
    """Converts a list of lists or list of dictionaries into a basic HTML table."""

    html_table = "<table class=\"sortable\">\n"

    if columns:
        html_table += "<thead>\n"
        for col_name in columns:
            html_table += f"<th>{col_name}</th>\n"
        html_table += "</thead>\n"

    for row in data:
        html_table += "<tr>\n"
        if isinstance(row, dict):
            if columns:
                for col_name in columns:
                    html_table += f"<td>{row.get(col_name, '')}</td>\n"
            else:
                for col_value in row.values():
                    html_table += f"<td>{col_value}</td>\n"
        else:
            for item in row:
                html_table += f"<td>{item}</td>\n"
        html_table += "</tr>\n"

    html_table += "</table>\n"

    return html_table


#contestants = ['Jesse','Simran','Sankalp','Sanjay','Sumat','Akhil']
#selections = [['Head','Nortje'],['Marsh','Zampa'],['Warner','Bumrah'],['Kohli','Starc'],['Yadav','Boult'],['Pooran','Pandya']]
#create_table(contestants, selections)