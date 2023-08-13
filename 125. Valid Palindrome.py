
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = ''
        s = s.lower()
        for let in s:
            if let.isalnum():
                l += let
        
        print(s)
        if l[::-1] == l:
            return True
        else:
            return False
