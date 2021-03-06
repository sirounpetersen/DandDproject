import requests
import json
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd



spellsurl = "https://www.dnd5eapi.co/api/spells"
r = requests.get(spellsurl)

spellsdict = (r.json())


#maze
a = (spellsdict["results"][198]["index"])
mazeurl = spellsurl +"/" + a 

q = requests.get(mazeurl)
mazedict = q.json()

updated = {}

keys = ['name', 'range', 'ritual', 'duration', 'concentration, casting_time', 'level']

for key, val in mazedict.items():
  if key in keys:
    updated[key] = val


pd.DataFrame.from_dict(updated)


engine = create_engine('mysql://root:codio@localhost/dandd')
pd.DataFrame.to_sql('Maze spell', con=engine, if_exists='replace', index=False)


"""{'index': 'maze', 
'name': 'Maze', 
'desc': ['You banish a creature that you can see within range into a labyrinthine demiplane. The target remains there for the duration or until it escapes the maze.', 
  'The target can use its action to attempt to escape. When it does so, it makes a DC 20 Intelligence check. If it succeeds, it escapes, and the spell ends (a minotaur or goristro demon automatically succeeds).', 
  'When the spell ends, the target reappears in the space it left or, if that space is occupied, 
  in the nearest unoccupied space.'], 
'range': '60 feet', 
'components': ['V', 'S'], 
'ritual': False, 
'duration': 'Up to 10 minutes', 
'concentration': True, 
'casting_time': '1 action', 
'level': 8, 
'school': {'index': 'conjuration', 
'name': 'Conjuration', 
'url': '/api/magic-schools/conjuration'}, 
'classes': 
  [{'index': 'wizard', 'name': 'Wizard', 'url': '/api/classes/wizard'}], 
'subclasses': [], 
'url': '/api/spells/maze'}
"""
