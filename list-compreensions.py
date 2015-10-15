x = int(raw_input())
y = int(raw_input())
z = int(raw_input())
n = int(raw_input())

print sum(sum([[ [ [X,Y,Z] for Z in range(z+1) if X+Y+Z != 2 ] for Y in range(y+1)] for X in range(x+1) ], []), [])
