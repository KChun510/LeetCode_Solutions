class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Find the shortest string in arr 
        short = min(strs, key=len)
        long = max(strs, key=len)

        Tsave = []
        #Tsave = Longest possible common prefix 


        for chars, charl in zip(short, long):
            if chars == charl:
                Tsave += chars
        
        arrlen = len(Tsave)
        i.e: arr length = x. WANT var, length = range(len(Tsave))
    
        #We want to do a check through strs compared Tsave
        for word in strs:
            if Tsave == None:
                return ""
            for i in range(arrlen):
                if word[i] == Tsave[i]:
                    pass
                else:
                    x = i
                    while x != arrlen:
                        Tsave[x] = ""
                        x +=1
                
                

        return "".join(Tsave)
