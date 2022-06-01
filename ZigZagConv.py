#Function, Converts input str into a zig zag orientation then returns the new str.
def convert(s , numRows):

    if numRows < 2:
        return s
    
    grow, i = 0, True
    res = [""] * numRows
    
#Loop through each str char
    for letter in s:
      
      #Add a letter to each row, till row maximum reached  
      if grow:
            res[i] += letter
            i += 1
      #Add a letter to each row, descending order/ till row min  
      else:
           i -= 1
           res[i] += letter
        
        #If reached row max, grow = false
        if i == numRows:
            i -= 1
            grow = False
        
        #If reached row min, grow = True
        elif i == 0:
            i += 1
            grow = True
    
    return "".join(res)
