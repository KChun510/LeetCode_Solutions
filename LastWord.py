 def lengthOfLastWord(self, s: str) -> int:
        
      #Reverse the given string
        rever = s[::-1]
        space = " "
        letcount = 0
       
      #Loop through the reversed s
        for char in rever:
            
            if len(s) == 1 and char != space:   #edge case
                return 1
            
            elif char != space: #if char does not equal a space, increase let count
                letcount += 1.
            
            elif char == space and letcount > 0:  #if spaced reached and let count != 0 return let count.
                return int(letcount)
        
        return int(letcount) 

                
