#!/bin/python

# Single pass with lookahead solution.
#
# The worst-case scenario runs in quadratic time
#   O(sum(i^2, i=0..|input|-1))-time,
# which is equivalent to O(|input|^2)-time, whereas the best case obviously
# runs in O(|input|)-time. Moreover, it stands in linear-space complexity,
# O(|input|)-space, across all scenarios.
#
def characterReverse(input):
  rev = list(input)
  for i in range(0, len(rev) - 1):
    if rev[i] == 't':
      j = i
      while j < len(rev) - 1 and rev[j] == 't' and ((ord(rev[j]) >= 'A' and ord(rev[j]) <= 'Z') or (ord(rev[j]) >= 'a' and ord(rev[j]) <= 'z')):
        j += 1
      j += 1
      if rev[j] == 'h':
        rev[j], rev[i] = rev[i], rev[j]
  return "".join(rev)

_input = raw_input()

res = characterReverse(_input);
print res
