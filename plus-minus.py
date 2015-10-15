n = float(raw_input())
v = map(int, raw_input().strip().split())

pos = float(len(filter(lambda x: x > 0, v))) / n
neg = float(len(filter(lambda x: x < 0, v))) /n
zer = float(len(filter(lambda x: x == 0, v))) / n

print "%.3f" % pos
print "%.3f" % neg
print "%.3f" % zer
