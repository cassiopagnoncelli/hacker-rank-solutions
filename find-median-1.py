import bisect

def calc_median(v):
	mid = len(v) // 2
	if len(v) % 2 == 1:
		return v[mid]
	return float((v[mid] + v[mid-1]) / 2.0)

n = int(raw_input())
v = []
for i in range(n):
	x = float(raw_input())
	bisect.insort(v, x)    # sorted-inserts x into v returning its position at v in O(n)
	print calc_median(v)
