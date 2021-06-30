import requests
from keys, import keys
from tweepy import API, OAuthHandler



auth = OAuthHandler(apikey, apisecret)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


trends = api.trends_place(id=23424977)
trending = []
for trend in trends[0]["trends"]:
    trending.append(trend["name"])
print(trending)

# url = "https://api.twitter.com/1.1/statuses/update.json"
# obj = {"status": "value"}

# response = requests.post(url, data = obj)
# print(response.json())

