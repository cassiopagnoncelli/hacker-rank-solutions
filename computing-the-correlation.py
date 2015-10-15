def corr(A, B):
	n = float(len(A))
	sumA, sumB, sumAB = sum(A), sum(B), sum(map(lambda (x,y): x*y, zip(A, B)))
	meanA, meanB = sumA/n, sumB/n
	ssA, ssB = sum(map(lambda x: x**2, A)), sum(map(lambda x: x**2, B))
	numer = n * sumAB - sumA*sumB
	denom = (n*ssA - sumA**2)**0.5 * ( n*ssB - sumB**2)**0.5
	return numer / denom

n = int(raw_input())
maths, physics, chem = [], [], []
for i in range(n):
	line = map(int, raw_input().split())
	maths.append(line[0])
	physics.append(line[1])
	chem.append(line[2])

print "%.2f" % corr(maths, physics)
print "%.2f" % corr(physics, chem)
print "%.2f" % corr(chem, maths)
