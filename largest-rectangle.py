# http://www.geeksforgeeks.org/largest-rectangle-under-histogram/

def top(s):
	return s[len(s)-1]

def largest_rectangle(h):
	s = []
	max_area, area_with_top, i, n = 0, 0, 0, len(h)
	while i < n:
		if len(s) == 0 or h[top(s)] <= h[i]:
			s.append(i)
			i += 1
		else:
			t = s.pop()
			if len(s) == 0:
				area_with_top = h[t] * i
			else:
				area_with_top = h[t] * (i - top(s) - 1)
			if max_area < area_with_top:
				max_area = area_with_top
	while len(s) > 0:
		t = s.pop()
		if len(s) == 0:
			area_with_top = h[t] * i
		else:
			area_with_top = h[t] * (i - top(s) - 1)
		if max_area < area_with_top:
			max_area = area_with_top
	return max_area

ig = raw_input()
v = map(int, raw_input().strip().split())
print largest_rectangle(v)
