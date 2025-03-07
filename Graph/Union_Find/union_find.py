
class UnionFind:
    """
    The purpose of using rank is to make the tree balanced by attaching shorter tree under the taller tree
    """
    def __init__(self, n):
        self.parent = list(range(n)) # assuming 0-based indexing
        self.rank = [0] * n
        self.count = n

    """
    Finding the root of x with path compression
    Path compression flattens the tree by pointing each node directly to the root
    """
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    """
    merge two sets into one
    """
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1

