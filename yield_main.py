import numpy as np
import matplotlib.pyplot as plt
import os
import operator
import time
from quick_yield import yield_average

class wave:
    
    def __init__(self, date, energy, filament, grid, focus, data, average):
        self.date = date
        self.energy = energy
        self.filament = filament
        self.grid = grid
        self.focus = focus
        self.data = data
        self.average = average

#file = '--';

BIG = []
np.array(BIG)
path = '--'

for file in os.listdir(path):
    fullname = path + "/" + file 
    with open(fullname) as fp:
       headers = []
       cnt = 0
       tr = 0
       while cnt < 4:
           line = fp.readline()
           line = line.rstrip('\t')
           headers.append(line.rstrip('\n'))
           cnt += 1
       while tr < 4:
           holder = headers[tr].split()
           headers[tr] = float(holder[1])
           tr += 1
       raw_data = np.loadtxt(fullname, skiprows = 5);
       uniqueness = time.ctime(os.path.getmtime(fullname)) 
       BIG.append(wave(uniqueness, headers[0], headers[1], headers[2], headers[3], raw_data, yield_average(raw_data)))
       #print('Energy: ' + str(headers[0]) + 'eV')
    BIG.sort(key=operator.attrgetter('energy'))
