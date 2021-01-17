import billboard
import numpy as np
import random

def random_queue():
    chart = billboard.ChartData('hot-100')

    numbers = np.random.randint(100, size=1)

    songs = []
    for num in numbers:
        songs.append("-p " + str(chart[num]))
    
    return songs

