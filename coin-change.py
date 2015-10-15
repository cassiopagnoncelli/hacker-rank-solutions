def how_many(S, n, m):
  # Create matrix.
  table = map(lambda y: map(lambda x: [0], range(m)), range(n+1))
  for i in range(m):
    table[0][i] = 1

  for i in range(n+1):
    for j in range(m):
      x = table[i - S[j]][j] if i - S[j] >= 0 else 0
      y = table[i][j-1] if j >= 1 else 0
      table[i][j] = x + y

  return table[n][m-1]


n, forget = map(int, raw_input().split())
coins = map(int, raw_input().split())

print how_many(coins, n, len(coins))