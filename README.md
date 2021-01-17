# Bobby Buddy


## Inspiration
We have all suffered mentally from the pandemic in one way or another, and we felt that we wanted to make a tool to help those that were probably feeling the same way. We wanted a bot that would bring our friends together, not apart.

## What it does
Detects signs of poor mental health through passive text detection, gives uplifting news stories, and suggests interactive activities (movies, TV shows, games) to bring friends together

## How I built it
Built with Python, running multiple social media APIs to collect the most up to date information
The core of our application really focuses on integrating multiple APIs in order to streamline object data to the user. For example, our !activity command that suggests interactive activities, we scrape from imdb top 250 movies and top 250 TV shows to build a dictionary of games, movies, and TV shows. This dictionary can be accessed to return an activity that friends can do to get together. We imported randint to access a random value in a key-value pair; this returns a random movie, TV show, or game (depending on the commands: !activity game, !activity movie, !activity TV)

Our passive text detection returns a photo from subreddit r/awww when “sad” or “angry” keywords are detected in a user’s text (negative emotions indicated from the words in a message). We split the string that’s a sentence into a list of words based on whitespace between words; we iterate through the list of split text and if an element in the list is also present in list of “sad” and “angry” keywords, returns the “angry” or “sad” word.

By using Python Reddit API Wrapper (PRAW), we were able to queue for the most popular posts on reddit and filter for our subreddit (r/aww) by compiling all this data in a list, we can randomly pick a post that we would like to give the user, and have the discord bot return the post’s content, in addition to a message :)

## Challenges I ran into
Major issues parsing through data structures of various platforms we were scraping stories/media off of. Using discord API to display messages to the bot users. Running asynchronous tasks for our Discord bot, like to remind users of their tasks.

## Accomplishments that I'm proud of
Integrating numerous different social media platforms into a cohesive and clean product, especially one that I could find useful in my own life (because my friends and I use Discord frequently, and we can make use of the bot ourselves), and doing this in a short timeframe.

## What I learned
How to pull API data and integrate social media content, such as praw and discord. In order to build our databases, we needed to learn how to webscrape with technologies like bs4 in order to scrape larger scale sights (like idmb’s 500 TV and movies) and pick up smaller APIs like Billboard’s in order to always receive the freshest music. 

## What's next for BobbyBuddyBot
We hope to introduce more features that we think can help anyone’s state of mental health. In particular, we have a “Daily Dashboard” in the works, which would greet our users every day with an uplifting quote, encouragement, and a positive news story. This feature would also be customizable to add any other features the user may want. We hope to spread this to our friends and hopefully, they can find the BobbyBuddyBot as useful as we did.
