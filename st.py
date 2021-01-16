import string
import reddit_functions as rf

punctuation_remover = str.maketrans('', '', string.punctuation)
def remove_punctuation(s):
    #Return a string with the same contents as s, but with punctuation removed.
    return s.strip().translate(punctuation_remover)

def lower(s):
    #Return a lowercased version of s
    return s.lower()

def split(s):
    #Return a list of words contained in s, which are sequences of characters
    return s.split()

def contains(text, keywords):
    for w in split(lower(remove_punctuation(text))):
        if w in keywords:
            return w
    return None

sad_keywords = ['depressed', 'sad']
angry_keywords = ['pressed', 'pissed', 'mad']

def are_you_okay(text):
    sad_word, mad_word = contains(text, sad_keywords), contains(text, angry_keywords)

    link = rf.cute()
    if sad_word:
        print("You said: ", sad_word, ". Are you ok? Here's a photo of a puppy to cheer you up" + link)
    elif mad_word:
        print('You said: ', mad_word, ". What is going on? Here's a photo of a kitten to calm you down" + link)

are_you_okay("I am depressed")