def get_positions(grid):
	l = len(grid)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 'p':
				p = [ j+1, l-i ]
			elif grid[i][j] == 'm':
				m = [ j+1, l-i ]
	return [ p, m ]

def nextMove(n,r,c,grid):
	princess, bot = get_positions(grid)
	rel = [princess[0] - bot[0], princess[1] - bot[1]]
	#print 'p=',princess, 'b=',bot, 'r=',rel
	if abs(rel[0]) >= abs(rel[1]):   # LEFT / RIGHT
		return "RIGHT" if rel[0] > 0 else "LEFT"
	else:                            # UP / DOWN
		return "UP" if rel[1] > 0 else "DOWN"

n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
	grid.append(raw_input())

print nextMove(n,r,c,grid)
