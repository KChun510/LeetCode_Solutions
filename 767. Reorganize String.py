class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = {}
        save = ""
        for elem in s:
            if elem in dic:
                dic[elem] += 1
            else:
                dic[elem] = 1

       
        
        count = 0
        save_index = 0
        check = 0
        prev = ""
        vals = sorted(list(dic.values()), reverse=True)
        keys = sorted(dic, key=dic.get, reverse=True)
        


        while count <= len(s):
            tmp = 0
            for index in range(check, len(vals)): #First capture the largest index, then add to save
                if vals[index] > tmp:
                    tmp = vals[index]
                    save_index = index
            if save_index != prev:
                save += keys[save_index]
                vals[save_index] -= 1
                prev = save_index
                check = 0
                count -= 1
            else:
                check += 1

            
            count += 1
        if len(save) == len(s):
            return save
        else:
            return ""
