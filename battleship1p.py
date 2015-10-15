from collections import Counter
from heapq import *
from random import randint

def shoot(grid, h, dash):
	if not h:
		return heappop(dash)[1]
	lin, col = h[0], h[1]
	num_lins, num_cols = len(grid), len(grid[0])
	directions = Counter({ 'left': 0, 'right': 0, 'down': 0, 'up': 0 })
	p = []
	if col > 0 and grid[lin][col-1] == '-':
		directions['left'] += 1
		if col+1 < num_cols and grid[lin][col+1] == 'h':
			directions['left'] += 1
		heappush(p, (directions['left'], [lin,col-1]))
	if col < num_cols-1 and grid[lin][col+1] == '-':
		directions['right'] += 1
		if col-1 >= 0 and grid[lin][col-1] == 'h':
			directions['right'] += 1
		heappush(p, (directions['right'], [lin,col+1]))
	if lin < num_lins-1 and grid[lin+1][col] == '-':
		directions['down'] += 1
		if lin-1 >= 0 and grid[lin-1][col] == 'h':
			directions['down'] += 1
		heappush(p, (directions['down'], [lin+1,col]))
	if lin > 0 and grid[lin-1][col] == '-':
		directions['up'] += 1
		if lin+1 >= 0 and grid[lin+1][col] == 'h':
			directions['up'] += 1
		heappush(p, (directions['up'], [lin-1,col]))
	# Return best movement.
	if len(p) >= 1:
		return heappop(p)[1]
	else:
		return heappop(dash)[1]

n = int(raw_input())
grid = []
h = False
dash = []
for i in range(n):
	line = list(raw_input().strip())
	grid.append(line)
	pos_h = filter(lambda j: line[j] == 'h', range(len(line)))
	if len(pos_h) >= 1:
		h = [i, pos_h[0]]
	pos_dash = filter(lambda j: line[j] == '-', range(len(line)))
	if len(pos_dash) >= 1:
		heappush(dash, (randint(0, 20), [i, pos_dash[0]]))

res = shoot(grid, h, dash)
print res[0], res[1]
