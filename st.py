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

def contains(text):
    sad_keywords = ['depressed', 'sad']
    angry_keywords = ['pressed', 'pissed', 'mad']
    
    keywords = sad_keywords.copy()
    keywords.extend(angry_keywords)
    for w in split(lower(remove_punctuation(text))):
        if w in keywords:
            return True, w
    return False, w

def are_you_okay(word):
    link = rf.cute()

    return ("You said: {}. Are you ok? Here's something cute to cheer you up :)\n{}".format(word, link.url))
