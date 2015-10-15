def closest_numbers(l):
  l.sort()
  d = 10**7
  idx = []
  for i in range(1, len(l)):
    x = l[i] - l[i-1]
    if x < d:
      d = x
      idx = [i-1]
    elif x == d:
      idx.append(i-1)
  for i in idx:
    print l[i], l[i+1],

n = int(raw_input())
l = map(int, raw_input().split())
closest_numbers(l)