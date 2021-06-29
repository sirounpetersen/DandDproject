import requests
from tweepy import API, OAuthHandler
apikey = "lHYJaCpgMMKLNDlWaDcNjMeMa"
apisecret = "NlQC2riUCfC9F0r4IqQPrVYbWP9e4kcBN5hEovcTInVIFAqWBQ"
token = "894961955957551105-uPz08lGX57JC3woITvQ2NxvGa9HHQpA"
tokensecret = "OOD2k5mfLKukLIHrSXCOL5ZgFqPWdOeVhfuDzlUXieTKE"
bearer = "AAAAAAAAAAAAAAAAAAAAAHKoHwEAAAAAKNC4f0%2BhSW5xyv3iR%2BrTMFo8XpY%3DH5KRuSK86u9o1UtlxoVvW8ShIkMA1Bf4tacWn3AosFLJJZl8q6"


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

