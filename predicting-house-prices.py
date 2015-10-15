import numpy as np

# Input.
f, n = map(int, raw_input().split())
in_table = []
for i in xrange(n):
	in_table.append(map(float, raw_input().split()))

num_tests = int(raw_input())
in_pred = []
for i in xrange(num_tests):
	in_pred.append(map(float, raw_input().split()))

# Converting.
table = np.matrix(in_table)

ones = np.matrix(np.ones((n, 1)))

x = np.c_[ ones, table[:,range(0,f)] ]
y = table[:,f]

pred = np.matrix(in_pred)
pred = np.c_[ np.ones((num_tests, 1)), pred ]

# Finding best parameters.
params = ((np.linalg.inv((x.T).dot(x))).dot(x.T)).dot(y)

# Result
res = pred.dot(params)
for i in range(num_tests):
	print "%.2f" % float(res[i,0])
