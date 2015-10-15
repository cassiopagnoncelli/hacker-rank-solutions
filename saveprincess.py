#!/bin/python
def displayPathtoPrincess(n, grid):
	steps = n // 2
	# Princess at top left.
	if grid[0][0] == 'p':
		for i in range(steps):
			print 'UP'
			print 'LEFT'
	# Princess at top right.
	elif grid[0][n-1] == 'p':
		for i in range(steps):
			print 'UP'
			print 'RIGHT'
	# Princess at bottom left.
	elif grid[n-1][0] == 'p':
		for i in range(steps):
			print 'DOWN'
			print 'LEFT'
	# Princess at bottom right.
	elif grid[n-1][n-1] == 'p':
		for i in range(steps):
			print 'BOTTOM'
			print 'RIGHT'
	else:
		princess_at = 'error'

m = input()
grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m, grid)
