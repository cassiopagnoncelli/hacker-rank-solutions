def fib_mod(a, b, n):
  if n == 0:
    return a
  elif n == 1:
    return b
  for i in range(n-1):
    b, a = b**2 + a, b
  return a

a, b, n = map(int, raw_input().split())
print fib_mod(a, b, n)