class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        max_len = len(matrix[0]) - 1
        for line in matrix:
            first_val = line[0]
            last_val = line[max_len]
            if target == first_val or target == last_val:
                return True
            elif target > first_val and target < last_val:
                start = 0
                end = max_len
                while (start <= end):
                    middle = (start + end) // 2
                    if target == line[middle]:
                        return True
                    elif target < line[middle]:
                        end = middle - 1
                    elif target > line[middle]:
                        start = middle + 1

        return False

            
