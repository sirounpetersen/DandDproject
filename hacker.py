import json 
import requests
#open file

idurl = "https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty"

myobj = {"text": "text"}
response = requests.get(idurl, data = myobj)
first = (response.json()[0])
storyurl = "https://hacker-news.firebaseio.com/v0/item/"+str(first)+".json?print=pretty"


res = requests.get(storyurl)
dct = (res.json())

for key, val in dct.items():
  if key == 'by' or key == 'title' or key == 'url':
    print(key, val)
    print("")
