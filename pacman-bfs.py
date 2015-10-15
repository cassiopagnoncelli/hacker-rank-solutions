from collections import deque
from copy import copy

def print_grid(grid):
	for i in range(len(grid)):
		print "".join(grid[i])

def unvisited(rows, cols):
	v = []
	for i in range(rows):
		v.append([False] * cols)
	return v

def unvisited_neighbourhood(grid, x, v):
	up = [x[0]-1, x[1]]
	down = [x[0]+1, x[1]]
	left = [x[0], x[1]-1]
	right = [x[0], x[1]+1]
	walkable = ['-', '.']
	n = []
	if up[0] >= 0 and grid[up[0]][up[1]] in walkable:
		n.append(up)
	if down[0] < len(grid) and grid[down[0]][down[1]] in walkable:
		n.append(down)
	if left[1] >= 0 and grid[left[0]][left[1]] in walkable:
		n.append(left)
	if right[1] < len(grid[0]) and grid[right[0]][right[1]] in walkable:
		n.append(right)
	return n[::-1]

explored = 0
ex_nodes = []
def find_food(grid, p, f, visited, path):
	global explored
	global ex_nodes
	explored += 1
	ex_nodes.append(p)
	if p[0] == f[0] and p[1] == f[1]:
		return path
	visited[p[0]][p[1]] = True
	for adj in unvisited_neighbourhood(grid, p, visited):
		if not visited[adj[0]][adj[1]]:
			ext_path = copy(path)
			ext_path.append(adj)
			res = find_food(grid, adj, f, visited, ext_path)
			if res:
				return res
	return False

pacman = map(int, raw_input().split())
food = map(int, raw_input().split())
dims = map(int, raw_input().split())
grid = []
for i in range(dims[0]):
	grid.append(list(raw_input().strip()))
grid[pacman[0]][pacman[1]] = '-'

visited = unvisited(len(grid), len(grid[0]))
res = find_food(grid, pacman, food, visited, [pacman])

# Result.
print explored
for a,b in ex_nodes:
	print a, b

print len(res) - 1
for a,b in res:
	print a, b
