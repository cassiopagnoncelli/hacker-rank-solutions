line = raw_input().strip()

time = line[:-2:]
pm = line[-2::].lower() == 'pm'
t = map(int, time.split(':'))

if pm and t[0] < 12:
    t[0] += 12
if not pm and t[0] == 12:
	t[0] = 0

print "%2.2d:%2.2d:%2.2d" % tuple(t)
