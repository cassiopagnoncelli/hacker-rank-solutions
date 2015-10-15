class Trie:
  def __init__(self, final):
    self.final = final
    self.children = {}
  def insert(self, word):
    head = word[0]
    tail = word[1:]
    # Check string in trie prefixes `word'
    if self.final:
      return False
    # Check `word' prefixes string in trie
    if len(tail) == 0 and head in self.children:
      return False
    # Insert
    if len(tail) == 0:
      self.children[head] = Trie(True)
      return True
    else:
      if head not in self.children:
        self.children[head] = Trie(False)
      return self.children[head].insert(tail)
  def preorder(self, x):
    if len(self.children) == 0:
      return x.upper() if self.final else x
    else:
      c = []
      for k in self.children.keys():
        c.append(self.children[k].preorder(k))
      return x + "(" + ",".join(c) + ")"
  def __repr__(self):
    return self.preorder('.')

n = int(raw_input())
t = Trie(False)
for i in range(n):
  w = raw_input()
  if not t.insert(w):
    print "BAD SET"
    print w
    break
else:
  print "GOOD SET"
