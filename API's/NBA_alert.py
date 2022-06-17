'''
This project is meant to run in the background, and starts running daily at 12:00 PM
This project sends a desktop notification each time an NBA game starts
In the event that this runs after NBA games have started, it will send a notification saying which games have started
'''
import requests
from plyer import notification
import datetime
import time

URL = "https://data.nba.net"

data = requests.get(URL + "/prod/v1/today.json").json()
x = data['links']['todayScoreboard']
# x = "/prod/v1/20220410/scoreboard.json"
scoreboard = requests.get(URL + x)

# times = ["10:43 AM ET", "10:44 AM ET", "10:45 AM ET"]

def to_military(time):
    time = time[:len(time) - 3]
    if "AM" in time:
        if time[:2] == "12":
            return "0" + str(int(time[:2]) % 12) + time[2:5]
        elif time[:2] == "10" or time[:2] == "11":
            return time[:2] + time[2:5]
        else:
            return "0" + str(int(time[:1]) % 12) + time[1:5]
    else:
        if time[:2] == "12":
            return time[:5]
        elif time[:2] == "10" or time[:2] == "11":
            return str(int(time[:2]) + 12) + time[2:5]
        else:
            return str(int(time[:1]) + 12) + time[1:5]

def strip_times(times):
    return times.rstrip()

def sort_times(times):
    return sorted(times)

start_times = []
teams = []

for game in scoreboard.json()['games']:
    start_times.append(game['startTimeEastern'])
    teams.append([game['hTeam']['triCode'], game['vTeam']['triCode']])

new_times = list(map(to_military, start_times))
final_times = sort_times(new_times)
final_times = list(map(strip_times, final_times))

print(datetime.datetime.now().strftime("%H:%M"))
print(final_times)
# print(teams)


while final_times != []:
    x = datetime.datetime.now().strftime("%H:%M")
    for game in scoreboard.json()['games']:
        if to_military(game['startTimeEastern']).rstrip() in final_times:
            if x == to_military(game['startTimeEastern']).rstrip():
                notification.notify(
                            title = "NBA Game Alert",
                            message = f"{game['hTeam']['triCode']} vs. {game['vTeam']['triCode']} starts now",
                            timeout = 2
                        )
                final_times.remove(to_military(game['startTimeEastern']).rstrip())
            elif x > to_military(game['startTimeEastern']).rstrip():
                notification.notify(
                            title = "NBA Game Alert",
                            message = f"{game['hTeam']['triCode']} vs. {game['vTeam']['triCode']} started at {game['startTimeEastern'].rstrip()}",
                            timeout = 2
                        )
                final_times.remove(to_military(game['startTimeEastern']).rstrip())

time.sleep(5)
