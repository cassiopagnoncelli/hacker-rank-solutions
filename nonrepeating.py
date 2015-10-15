#!/bin/python

def firstNonRepeatingCharacter(input):
  # Histogram for ASCII table.
  histogram = [0] * 127

  # Characters distributions along the ASCII table.
  # This portion takes Theta(|input|)-time and Theta(|input|)-space.
  for c in list(input):
    index = ord(c)
    histogram[index] += 1

  # Finds the first occurence wherein a character appears a single time.
  for c in list(input):
    index = ord(c)
    if histogram[index] == 1:
      return chr(index)
  return ''

_input = raw_input()

res = firstNonRepeatingCharacter(_input);
print res
