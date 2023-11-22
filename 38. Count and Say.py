class Solution:
    def countAndSay(self, n: int) -> str:
        loop = 1
        def recur(loop:int ,temp: str) -> str:
            save = ""
            # Our base case, if our recursive calls excede n return temp
            if (loop < n):
                index = 0
            
                while index < len(temp):
               
                    if (len(temp) > 1 and index < len(temp) - 1):
                    """
                    Need to check if len(temp) > 1, because were going to be making comparisons with temp[index] and  
                    temp[index + 1]

                    why?: Need to seperate substrings. And count the same elems whithin the sub-string

                    -and-

                    because were using a while loop, we need to ensure when we incrament our index that it is still whithin 
                    our string range

                    """  
                        if temp[index] == temp[index + 1]: # Check if the index + 1, is a substring
                            count = 1
                            while index < len(temp) - 1  and temp[index] == temp[index + 1]: 
                                # if it is a substring count all elems whithin
                                count += 1
                                index += 1
                            # Append the substring to "save"
                            save += str(count) + temp[index]
                            index += 1
                       
                        # If not a substring then add '1' + elem. to save
                        else: 
                            save += "1" + temp[index]
                            index += 1 
                    
                    # Starting out, the len of temp or countAndSay(1) will always > 1.
                    # So append "1" + elem
                    else:
                        save += "1" + temp[index]
                        index += 1
                    
                    
                # If we reached the end of our string, make next recursive call   
                return recur(loop + 1, save)
                
            # Once we made our needed recursive calls, return temp (completed string)
            else:
                return temp
                       
            
        return recur(loop, str(loop))


"""
Logic: Brute force, starting with countAndSay(1) = "1". We then add "1" into our temp, which will then turn into "11" with countAndSay(2). We keep making countAndSay() calls until countAndSay(n) == n. 
With each recursive call, we linearly check our temp string. Counting all elements whithin string, then adding them to our temp string. Then passing temp, to the next recursive call. - There is inner logic to take account for substrings.


i.e: (Each recursive call, we count the elems in the string. Append them to a new string. Then pass new string to next call. Until we reached desired loops)


Run-Time: O(n^2). When n is input, we make recursive calls n-(n+1), n-(n+2), n-(n+x) until x == n. This linear recursive nature runs in O(n) time. However, whithin each recursive call we do a linear search with the string. This is also a O(n), operation.
Meaning that these two operations combined will give us O(n^2) run time:


Mem-usage: O(n), the call stack will only ever get as large as n


"""
