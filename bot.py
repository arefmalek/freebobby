import discord
import os
import json

import reddit_functions as rf

with open("keys.json") as f:
    info = json.load(f)

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!goodnews'):
        news, link = rf.good_news()
        await message.channel.send("Here's some good news\n\n" + 
        news + "\n" + link)
    elif message.content.startswith('!sad'):
        post = rf.cute()


        await message.channel.send("If you're feeling sad, here's something cute to cheer you up\n\n" + 
        "from u/" + post.author.name + ": " + post.title + '\n' + post.url
        )
    

client.run(info["discord"]["discord_token"])