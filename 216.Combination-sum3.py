class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        possible_set = [n for n in range(1,10)]
        res = []

        def backTrack(currRes, size, target, possible_set):        
            if len(currRes) == size and sum(currRes) == target:
                res.append(currRes)
                return
            
            elif len(currRes) >= k:
                return

            for i in range(len(possible_set)):
                backTrack(currRes + [possible_set[i]], size, target, possible_set[i+1:])

        if n != 0:
            backTrack([], k, n, possible_set) 

        return res

"""
Intuition
Note: BackTracking is un-intuitive at first. After doing a little study, it will click.

My intuition is that we want to find all possible combinations to find our target sum, with values 1-9 and a size k. Given the size constraint of k and a target sum, this gives us our base cases for our recursive function.

Thinking that we could form a recursive tree for this problem, backtracking was the choice.

Approach
Build a array of values 1-9, used whithin our backTack f(n).
Set our 2 base cases.
a) One being, we matched our size of K and target sum.
b) Two, were over our size K and don't meet target sum.
Build our recursive Tree.
An example of our first recursive stack, if our possible set was [1,2,3] and k = 3. The pattern bellow will repeat for values 2 and 3, but the root node changing to 2 and 3.

                [1]
        /        |       \
      [1]       [2]      [3]
      /|\       /|\      /|\
   [1][2][3] [1][2][3] [1][2][3]
Complexity
Time complexity:
This follows a Bionomial structure, of we have 9 options and pick K.

Number of base operations O(9 K) == 9!/k!(n-k)!
Plus we check the Sum, of our Sub array O(k)
Final: O((9 k) * k)

Space complexity:
In our Res, we save (9 k) options.
Plus our recursive tree height, which will be of height K.
Final: O((9 K) * k)
"""
