from numpy import zeros
import Queue

def adj(num_nodes, edges):
  m = zeros((num_nodes, num_nodes), int)
  for a, b in edges:
    m[a-1][b-1] += 1
  return m

class Graph(object):
  ''' Graph with adjacency matrix representation. '''
  def __init__(self, nodes, edges):
    self.num_nodes = nodes
    self.edges = edges
    self.m = adj(nodes, edges)
    self.dist = [None] * num_nodes
    self.pred = [10**7] * num_nodes
  def __repr__(self):
    print 'adjacency:', self.m
    print 'distances:', self.dist
    print 'predecessors:', self.pred
  def __str__(self):
    return 'Graph with ' + str(self.num_nodes) + ' nodes and ' + str(len(self.edges)) + ' edges.'
  def neigh(self, node):
    line = self.m[node-1,:]
    return map(lambda x: x + 1, [i for i in range(len(line)) if line[i] > 0])
  def dijkstra(self, start):
    src = start - 1
    # Initialize single source.
    self.dist = [None] * num_nodes
    self.pred = [10**7] * num_nodes
    self.dist[src] = 0
    # Set of vertices s and min priority queue q
    s = set([])
    q = Queue.PriorityQueue()
    [q.put(i) for i in range(self.num_nodes)]
    while not q.empty():
      x = q.get()
      s.union(set([x]))
      

if __name__ == '__main__':
  num_cases = int(raw_input())
  for c in range(num_cases):
    num_nodes, num_edges = map(int, raw_input().split())
    edges = []
    for e in range(num_edges):
      edges.append(map(int, raw_input().split()))
    start = int(raw_input())
    g = Graph(num_nodes, edges)
    print g
    g.dijkstra(start)
