import discord
import os
import json
import numpy as np

import reddit_functions as rf
import billboard_functions as bf
import st
import activities as act

with open("keys.json") as f:
    info = json.load(f)


headers = ['Task', 'Start', 'End']
todolist = np.empty(shape=[0,3])

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #good news subreddit
    if message.content.startswith('!goodnews'):
        news, link = rf.good_news()
        await message.channel.send("Here's some good news\n\n" + 
        news + "\n" + link)
    
    #gives movie game or TV show
    elif message.content.startswith('!activity '):
        answer = ""
        genre = message.content.split(' ')
        if len(genre) > 0:
            genre = genre[1]
            if genre == "game":
                answer = act.game()
            if genre == "TV":
                answer = act.television()
            if genre == "movie":
                answer = act.movie()
        
        await message.channel.send(answer)
        return

               
    
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

    ###Calendar/To Do List
    elif message.content.startswith('$addtask'):
        global todolist
        args = message.content.split(' ')
        task = args[1]
        start = args[2]
        end = args[3]
        item = np.array([task, start, end])
        todolist = np.append(todolist, [item], axis=0)

        todolist = todolist[todolist[:, 1].argsort()]
        print(todolist)

        await message.channel.send('Task added')

    elif message.content.startswith('$todo'):
        await message.channel.send(headers)
        for item in todolist:
            await message.channel.send(item)

    elif message.content.startswith('$done'):
        args = message.content.split(' ')[1]
        for item in range(len(todolist)):
            if args == todolist[item][0]:
                await message.channel.send("Congrats on finishing " + args + "!")
                todolist = np.delete(todolist, item, axis=0)
    



    
    

client.run(info["discord"]["discord_token"])