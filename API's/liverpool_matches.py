import requests

headers = {
    "apikey": "my_api_key"
}

# premiere league id 237
# la liga id 538
params = (
  # 2021 - 2022 season
   ("season_id","1980"),
)
response = requests.get('https://app.sportdataapi.com/api/v1/soccer/matches', headers=headers, params=params).json()
for data in response['data']:
    if data['home_team']['name'] == "Liverpool FC" or data['away_team']['name'] == "Liverpool FC":
        print(f"{data['home_team']['name']} vs. {data['away_team']['name']}")
