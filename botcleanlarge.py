# Manhattan distance.
def distance(a, b):
	return abs(a[0] - b[0]) + abs(a[1] - b[1])

def parse_board(bot, board):
	d = []
	closest_dirty = 0
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == 'd':
				d.append([ i, j, distance(bot, [i,j]) ])
				if d[len(d)-1][2] < d[closest_dirty][2]:
					closest_dirty = len(d) - 1
	return d, closest_dirty

def print_board(board, closest):
	board[closest[0]][closest[1]] = 'D'
	for line in board:
		print "".join(line)

def next_move(bot, board):
	if board[bot[0]][bot[1]] == 'd':
		return "CLEAN"
	dirties, closest = parse_board(bot, board)
	lin,col = dirties[closest][0], dirties[closest][1]
	#print_board(board, [lin,col])
	L, C = bot[0]-lin, bot[1]-col
	if abs(L) > abs(C):
		return "DOWN" if L < 0 else "UP"
	else:
		return "RIGHT" if C < 0 else "LEFT"

if __name__ == "__main__":
	pos = [int(i) for i in raw_input().strip().split()]
	dim = [int(i) for i in raw_input().strip().split()]
	board = [[j for j in raw_input().strip()] for i in range(5)]
	print next_move(pos, board)

