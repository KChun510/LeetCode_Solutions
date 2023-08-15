lass Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        save_arr = []

       
        
        if len(x) % 2 == 0 and x[0] != "-": #even case
            save_arr += [x[0:len(x)//2]]
            save_arr += [x[len(x)//2: ]]
        elif len(x) % 2 != 0 and x[0] != "-": #odd case
            save_arr += [x[0:len(x)//2]]
            save_arr += [x[len(x)//2 + 1: ]]
        else:
            return False

        if save_arr[0] == save_arr[1][::-1]:
            return True
        else: 
            return False
        
