def icecream(m, costs):
	for i in range(len(costs)):
		for j in range(i+1, len(costs)):
			if costs[i] + costs[j] == m:
				return (i+1, j+1)

cases = int(raw_input())
for i in range(cases):
	m = int(raw_input())
	ignore = int(raw_input())
	costs = map(int, raw_input().strip().split())
	print "%d %d" % icecream(m, costs)
