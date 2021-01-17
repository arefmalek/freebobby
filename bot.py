import discord
import os
import json
import numpy as np

import reddit_functions as rf
import billboard_functions as bf
import st

with open("keys.json") as f:
    info = json.load(f)


headers = ['Task', 'Start', 'End', 'Done']
todolist = np.array([])

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

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
        "from u/" + str(post.author.name) + ": " + post.title + '\n' + post.url
        )
    
    elif message.content.startswith('!song'):
        charts = bf.random_queue()

        await message.channel.send("Now Queueing 10 random songs from billboard top 100\n")

        for song in charts:
            await message.channel.send(song)

    elif message.content.startswith('!today'):

        embedVar = discord.Embed(title="Daily Dashboard", description=" ", color=discord.Color.teal())

        rlink = rf.cute().url
        embedVar.set_thumbnail(url=rlink)
        embedVar.add_field(name='Post of the Day', value=rlink, inline=False)

        embedVar.add_field(name="Music's Top 5", value=bf.top_five(), inline=False)

        embedVar.add_field(name="Self Care Tip of the Day", value=bl.bucketRandom(), inline=False)

        embedVar.set_footer(text='Source: https://wholefully.com/self-care-ideas/')

        await message.channel.send(embed=embedVar)
    
    elif st.contains(message.content)[0]:
        info = st.contains(message.content)

        await message.channel.send(st.are_you_okay(info[1]))
    
    


    
    

client.run(info["discord"]["discord_token"])