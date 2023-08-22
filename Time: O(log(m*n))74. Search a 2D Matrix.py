class Solution:
    #Next time you approach this problem, do an additional binary sort. We only did a binary sort in the x. But we can also do a binary sort in the y with all the list[i][0] values
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1  #The last line in the matrix

        while (start <= end or end == 0):
            first_middle = (start + end) // 2
            if target == matrix[first_middle][0] or target == matrix[first_middle][len(matrix[0]) - 1]:
                return True
            elif target > matrix[first_middle][0] and target < matrix[first_middle][len(matrix[0]) - 1] or end == 0:
                start = 0
                end = len(matrix[0]) -1
                while (start <= end):
                    middle = (start + end) // 2
                    if target == matrix[first_middle][middle]:
                        return True
                    elif target < matrix[first_middle][middle]:
                        end = middle - 1
                    elif target > matrix[first_middle][middle]:
                        start = middle + 1
                return False
            elif target < matrix[first_middle][0]:
                end = first_middle - 1
            elif target > matrix[first_middle][0]:
                start = first_middle + 1
        return False
