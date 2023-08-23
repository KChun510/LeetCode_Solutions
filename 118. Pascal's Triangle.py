class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        stack = []

        def recur(res, stack, n):
            if stack == []:
                stack = [1]
                res += [stack]
                recur(res, stack, n+1)
            elif n == numRows:
                return res
            else:
                prev, nxt = 0, 1
                tmp = [0] + stack + [0]
                stack = []
                while nxt < len(tmp):
                    stack += [tmp[prev] + tmp[nxt]]
                    prev, nxt = prev + 1, nxt + 1
                res += [stack]
                recur(res, stack, n+1)
        
        recur(res, stack, 0)
        return res


"""
Time: O(N^2), There is an operation for each row, and each row has n operations adding sums to a list
Space: O(N^2), One N comes from the recursive stack, and the second N comes from the res which is going tp hold N elements N*N = n^2

"""
