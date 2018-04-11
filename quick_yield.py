import numpy as np

def yield_average(raw_data):
    collector = []
    collector_draw = []

    sample = []
    sample_draw = []
    
    grid = []
    grid_draw = []
    
    stage = []
    stage_draw = []
    
    averages = []
    num = 0

    np.array(collector)
    np.array(sample)
    np.array(grid)
    np.array(stage)
    np.array(averages)

    while num < (np.shape(raw_data)[0] / 4):
        collector.append(raw_data[num * 4])
        sample.append(raw_data[(num * 4) + 1])
        grid.append(raw_data[(num * 4) + 2])
        stage.append(raw_data[(num * 4) + 3])
        num += 1

    for num in range(np.shape(collector)[1]):
        sumlist = []
        np.array(sumlist)
        for x in range(len(collector)):
            sumlist.append(collector[x][num])
        collector_draw.append(np.average(sumlist))
        num += 1
        
    for num in range(np.shape(sample)[1]):
        sumlist = []
        np.array(sumlist)
        for x in range(len(sample)):
            sumlist.append(sample[x][num])
        sample_draw.append(np.average(sumlist))
        num += 1
        
    for num in range(np.shape(grid)[1]):
        sumlist = []
        np.array(sumlist)
        for x in range(len(grid)):
            sumlist.append(grid[x][num])
        grid_draw.append(np.average(sumlist))
        num += 1
        
    for num in range(np.shape(stage)[1]):
        sumlist = []
        np.array(sumlist)
        for x in range(len(stage)):
            sumlist.append(stage[x][num])
        stage_draw.append(np.average(sumlist))
        num += 1
        
    averages.append(collector_draw)
    averages.append(sample_draw)
    averages.append(grid_draw)
    averages.append(stage_draw)
    
    return(averages)
