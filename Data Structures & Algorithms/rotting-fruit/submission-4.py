class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rotten = 0
        fresh = 0
        rotten_idx = []
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    num_rotten +=1
                    rotten_idx.append([i,j])
                elif grid[i][j] == 1:
                    fresh +=1

        direc = [[1,0],[-1,0], [0,1], [0,-1]]

        mins = 0
        while fresh > 0 and len(rotten_idx) > 0:
            new_rot = []
            for i in rotten_idx:
                r = i[0]
                c = i[1]

                for j in direc:
                    nr = r + j[0]
                    nc = c + j[1]

                    if nr >= 0 and nr < row and nc >= 0 and nc < col:
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2
                            fresh -= 1
                            new_rot.append([nr,nc])
            mins +=1
            rotten_idx = new_rot


        if fresh > 0:
            return -1
        else:
            return mins

        