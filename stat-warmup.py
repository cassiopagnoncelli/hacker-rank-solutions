from math import sqrt

def calc_median(s):
	q = len(s) // 2
	if len(s) % 2 == 1:
		return s[q]
	else:
		return float(s[q] + s[q-1]) / 2.0

def calc_mode(s):
	most_frequent_idx = 0
	d = {}
	for i in s:
		res = d.get(i) if d.has_key(i) else 0
		d.update({ i: res + 1 })
		if d.get(i) > d.get(most_frequent_idx):
			most_frequent_idx = i
	return most_frequent_idx

def calc_sd(s, mean):
	return (sum(map(lambda x: (float(x) - mean)**2, s)) / float(len(s))) ** 0.5

def basic_statistics(l):
	s = sorted(l)
	n = float(len(s))
	mean = sum(map(lambda x: float(x), s)) / n
	median = calc_median(s)
	mode = calc_mode(s)
	sd = calc_sd(s, mean)
	ci_lower = mean - 1.96 * sd/sqrt(n)
	ci_upper = mean + 1.96 * sd/sqrt(n)
	print "%.1f" % mean
	print "%.1f" % median
	print mode
	print "%.1f" % sd
	print "%.1f %.1f" % (ci_lower, ci_upper)

n = int(raw_input())
ints = map(int, raw_input().split())
basic_statistics(ints)
