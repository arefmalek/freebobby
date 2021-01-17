import billboard
import numpy as np
import random

def random_queue():
    chart = billboard.ChartData('hot-100')

    numbers = np.random.randint(100, size=10)

    songs = "Looking for some new hits? try these:\n "
    for num in numbers:
        songs += (str(chart[num]) + '\n')
    
    return songs

def top_five():
  chart = billboard.ChartData('hot-100')

  numbers = np.arange(1,6)

  songs = []
  for num in numbers:
    songs.append(str(chart[num]))
  return songs

