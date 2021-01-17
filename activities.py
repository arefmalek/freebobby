import json
import random

with open("activity/activities.json") as f:
    info = json.load(f)

def movie():
    database = info["movie"]
    index = random.randint(0,len(database)-1)

    return "Looking for a movie? Watch: " + database[index]

def television():
    database = info["TV"]
    index = random.randint(0,len(database)-1)

    return "Looking for a show? Watch: " + database[index]

def game():
    database = info["game"]
    index = random.randint(0,len(database)-1)

    return "Looking for a game? Try {}. Link below:\n{}".format(database[index]["name"], database[index]["Link"]) 