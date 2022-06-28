from nba_api.stats.endpoints import leagueleaders
import pandas as pd

leaders = leagueleaders.LeagueLeaders()

x = leaders.get_dict()
df = x['resultSet']['rowSet']
headers = x['resultSet']['headers']


df = pd.DataFrame(df)
df.columns = headers
df.to_csv('C:\\Users\\avash\\Documents\\Python\\nba_stats.csv', index=False)
