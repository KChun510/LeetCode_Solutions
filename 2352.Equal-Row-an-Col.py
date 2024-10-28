class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        outPut = 0
        gridLen = len(grid)


        for col in range(len(grid[0])):
            colElems = []
            for row in range(gridLen):
                colElems.append(grid[row][col])

            
            tempCount = 0
            for row in grid:
                if colElems == row:
                    outPut += 1

        return outPut
