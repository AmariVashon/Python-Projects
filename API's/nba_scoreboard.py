from requests import get
from pprint import PrettyPrinter, pprint

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

# pretty printer is used to see the json/dictionary output in a readable format when determining what aspects of the games are to be used
printer = PrettyPrinter()

def get_links():
    '''
    Easily allows for access to current day information, such as currentScoreboard
    Sends a request to the master page and returns the 'links' values 
    '''
    data = get(BASE_URL + ALL_JSON).json()

    links = data['links']
    return links

def pregame(hTeam, vTeam, period, start):
    '''
    Displays the scoreboard in a manner consistent with a scoreboard before a game starts:
        - Sets the score, clock, and period to 0
        - Displays the start time of the game
    '''
    print(f"{hTeam['triCode']} vs. {vTeam['triCode']}")
    print(f"{0} - {0}")
    print(f"0:00 | period: {period['current']}")
    print(f"Start time: {start}")

def activegame(hTeam, vTeam, period, clock):
    '''
    Displays the scoreboard in a manner consistent with a live scoreboard:
        - Displays the current clock, score, and period
    '''
    print(f"{hTeam['triCode']} vs. {vTeam['triCode']}")
    print(f"{hTeam['score']} - {vTeam['score']}")
    print(f"{clock} | period: {period['current']}")

def postgame(hTeam, vTeam):
    '''
    Displays the scoreboard in a manner consistent with a scoreboard after the game has ended:
        - Displays the final score and who won
        - Sets the period to 'Final'
    '''
    print(f"{hTeam['triCode']} vs. {vTeam['triCode']}")
    print(f"{hTeam['score']} - {vTeam['score']}")
    if int(hTeam['score']) > int(vTeam['score']):
        print(f"{hTeam['triCode']} wins | period: Final")
    else:
        print(f"{vTeam['triCode']} wins | period: Final")

def get_stats():
    '''
    This is the main function that loops through all of today's games 
        - Gathers the period, visiting team, home team, clock, and start time of all the games to be used in the previous -game functions
        - Gathers if a game is activated (has started) to allow for pre and postgame functions to be created and differentiated
        - A counting variable is used for formatting purposes, so that the dashed lines appear between all the games
    '''
    team_stats = get_links()['currentScoreboard']
    data = get(BASE_URL + team_stats).json()['games']
    count = 0
    for game in data:
        period = game['period']
        vTeam = game['vTeam']
        hTeam = game['hTeam']
        clock = game['clock']
        start = game['startTimeEastern']
        activate = game['isGameActivated']

        if activate == False and period['current'] == 0:
            if count == 0:
                pregame(hTeam, vTeam, period, start)
                count += 1
            else:
                print("-"*25)
                pregame(hTeam, vTeam, period, start)
                count += 1
        elif activate == False and period['current'] >= 4:
            if count == 0:
                postgame(hTeam, vTeam)
                count += 1
            else:
                print("-"*25)
                postgame(hTeam, vTeam)
                count += 1
        else:
            if count == 0:
                activegame(hTeam, vTeam, period, clock)
                count += 1
            else:
                print("-"*25)
                activegame(hTeam, vTeam, period, clock)
                count += 1

def get_scoreboard():
    '''
    This is a function to easily access the keys of each game, such as the visiting team (vTeam) and home team (hTeam)
    '''
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        print(game.keys())

get_stats()
