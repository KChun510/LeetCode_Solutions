lass Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = {}
        for prev in range(len(s)):
            for nxt in range(prev, len(s)+1):
                tmp = s[prev:nxt]
                if tmp == tmp[::-1] and tmp != '' and len(tmp) > 1:
                    dic[tmp] = len(tmp)

        if(dic):
            return max(dic, key=dic.get)
        else:
            return s[0]
        
