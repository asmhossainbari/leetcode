from typing import List

class UnionFind:
    def __init__(self, n_city):
        self.parent = list(range(n_city + 1))
        self.rank = [0] * (n_city + 1)
        self.count = n_city

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

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


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city = len(isConnected)
        uf = UnionFind(city)
        for i in range(city):
            for j in range(i + 1, city):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.count

sol = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(sol.findCircleNum(isConnected))  # Output: 2
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(sol.findCircleNum(isConnected))  # Output: 3