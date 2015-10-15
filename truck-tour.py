from collections import deque

class Pump(object):
	def __init__(self, index, petrol, distance):
		self.index = index
		self.i = index
		self.petrol = petrol
		self.p = petrol
		self.distance = distance
		self.d = distance
	def __repr__(self):
		return "%d: p=%d d=%d" % (self.i, self.p, self.d)

def complete_cycle(q, n):
	tank = 0
	for i in range(n):
		tank += q[i].petrol
		tank -= q[i].distance
		if tank < 0:
			return False
	return q[0].index

n = int(raw_input())
q = deque()
for i in range(n):
	petrol, distance = map(int, raw_input().strip().split())
	q.append(Pump(i, petrol, distance))

while True:
	run = complete_cycle(q, n)
	if run:
		print run
		break
	q.rotate(-1)
