def max_subarray(v):
  current_sum = -10**10
  current_index = -1
  best_sum = -10**10
  best_start_index = -1
  best_end_index = -1

  for i in xrange(len(v)):
    val = current_sum + v[i]
    if val > 0:
      if current_sum == 0:
        current_index = i
      current_sum = val
    else:
      current_sum = 0

    if current_sum > best_sum:
      best_sum = current_sum
      best_start_index = current_index
      best_end_index = i

  return sum(v[best_start_index : best_end_index + 1])

def max_noncont_subarray(v):
  return sum(filter(lambda x: x > 0, v))

num_cases = int(raw_input())

for i in range(num_cases):
  n = int(raw_input())
  v = map(int, raw_input().split())
  print max_subarray(v), max_noncont_subarray(v)
