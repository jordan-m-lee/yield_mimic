import numpy as np
import matplotlib.pyplot as plt
import os
import operator

class wave:
    
    def __init__(self, energy, filament, grid, focus, data):
        self.energy = energy
        self.filament = filament
        self.grid = grid
        self.focus = focus
        self.data = data

#file = '----';

BIG = []
np.array(BIG)
path = '-----'

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
       BIG.append(wave(headers[0], headers[1], headers[2], headers[3], raw_data))
    BIG.sort(key=operator.attrgetter('energy'))

collector = []
sample = []
grid = []
stage = []
num = 0

np.array(collector)
np.array(sample)
np.array(grid)
np.array(stage)

while num < (len(BIG[0].data) / 4):
    collector.append(BIG[0].data[num])
    sample.append(BIG[0].data[num + 1])
    grid.append(BIG[0].data[num + 2])
    stage.append(BIG[0].data[num + 3])
    num += 1

collector_draw = []
#np.array(collector_draw)

print(len(collector))

for num in range(len(collector[0])):
    sumlist = []
    np.array(sumlist)
    for x in range(len(collector)):
        sumlist.append(collector[x][num])
    collector_draw.append(np.average(sumlist))
    num += 1
    
numbers = np.arange(2500)

print(np.size(collector))
print(np.shape(collector)[1])

plt.plot(numbers, collector_draw, 'r');
plt.axis();
plt.show();
