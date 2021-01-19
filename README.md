# Bobby Buddy

## Inspiration
We have all suffered mentally from the pandemic in one way or another, and we felt that we wanted to make a tool to help those that were probably feeling the same way. We wanted a bot that would bring our friends together, not apart.

## Functions
These sort of things are explainable, but probably better shown than anything, enjoy :)

### Text detection
One of the largest issues we wanted Bobby to do is to pick up on the little things. We made sure that if Bobby detected a 'sad' (ex: "sad") or mad (ex: "pressed) he would be able to provide a nice message :)
![](demo_text_detection.gif)

### Good news!
2020 was not a year of good news - for that reason, we made sure that whenever a user wanted, Bobby could quickly give a user good news. The best part of the function is that the function calls using the ```PRAW``` API so that we can always the freshest content from the hot page of r/upliftingnews (and a randomized selection so that the news is different)

### Activity
We made a bs4 script to scrape the top 250 movies AND songs from imdb and store it in a database that Bobby can easily give to a user should they want to watch somthing with some friends. 

### Excuse the typing lol
![](demo_goodnews.gif)


### Fresh Music
Using a billboard API, we are able to constantly queue for the top 100 songs on billboard at any time and give a randomized selection of 10 songs at any point in time.  

### Todo List
We wanted people to keep track of the things they do in one day, and get some positive reinforcement for all of the activities they did for the day. Bobby does both :>
![](demo_songlist.gif)

## Challenges we ran into
Major issues parsing through data structures of various platforms we were scraping stories/media off of. Using discord API to display messages to the bot users. Running asynchronous tasks for our Discord bot, like to remind users of their tasks.

## Accomplishments that I'm proud of
Integrating numerous different social media platforms into a cohesive and clean product, especially one that I could find useful in my own life (because my friends and I use Discord frequently, and we can make use of the bot ourselves), and doing this in a short timeframe.

## What I learned
How to pull API data and integrate social media content, such as praw and discord. In order to build our databases, we needed to learn how to webscrape with technologies like bs4 in order to scrape larger scale sights (like idmb’s 500 TV and movies) and pick up smaller APIs like Billboard’s in order to always receive the freshest music. 

## What's next for BobbyBuddyBot
We hope to introduce more features that we think can help anyone’s state of mental health. In particular, we have a “Daily Dashboard” in the works, which would greet our users every day with an uplifting quote, encouragement, and a positive news story. This feature would also be customizable to add any other features the user may want. We hope to spread this to our friends and hopefully, they can find the BobbyBuddyBot as useful as we did.
