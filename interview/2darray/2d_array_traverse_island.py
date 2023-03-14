graph = [[1, 1, 0, 0, 0], 
         [0, 0, 1, 0, 1], 
         [1, 0, 0, 0, 1], 
         [1, 1, 0, 1, 0], 
         [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])
count=0

class Graph(object):
    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph
        self.visited = [[False for j in range(self.COL)]for i in range(self.ROW)]

    def countislands(self):
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.visited[i][j] == False and self.graph[i][j] == 1:
                    self.dfs(i,j)
            count += 1
        return count

    def dfs(self,i,j):
        rowNbr = [-1,0,0,1] 
        colNbr = [0,-1,1,0]
        self.visited[i][j]=True
        for k in range(4):
            if self.isSafe(i + rowNbr[k], j + colNbr[k]):
                self.dfs(i + rowNbr[k], j + colNbr[k])

    def isSafe(self, i, j):
        return (i >= 0 and i < self.ROW and j >= 0 and j < self.COL and not self.visited[i][j] and self.graph[i][j])

g= Graph(row,col,graph)
print (g.countislands())
