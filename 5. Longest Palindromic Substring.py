class Solution:
    def longestPalindrome(self, s: str) -> str:
        save = ""
        biggest_len = 0
        for prev in range(len(s)):
            for nxt in range(prev, len(s)+1):
                tmp = s[prev:nxt]
                if tmp == tmp[::-1] and len(tmp) > biggest_len:
                    biggest_len = len(tmp)
                    save = tmp

        if save:
            return save
        else:
            return s[0]

"""
time complexity: O(n^3). For every n elements there is a n^2 operations, multiplied by the array slicing which is o(n)
Space complexity: O(1).  The Only mem allocated it save & biggest_len

"""
