class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Turn the list of numbers into a dictionary. indice is the key, numb is the value
        dic, save = {}, []
        i = 0
        for n in nums:
            dic[i] = n 
            i += 1
        
        #Loop through the indecies for the list of numbers
        for indi in (range(len(nums))):
            
            #Creating a remainder, for lookup in dictionay values
            rem = target - nums[indi]
            
            #if remainder found in dic.values, using "indi" and "count" as counts like a prev and curr in while loop.
            # "indi" I.e: Prev, will be updated if the raminder not found in dic.values. 
            #"count" I.e: Curr, will always be 1+ prev.
            #indi and count are needed to keep track of indecies 
            
            if rem in dic.values():      
                count = indi + 1
                
                while count < len(nums):
                    if dic[indi] + dic[count] == target:
                        save += indi, count
                        return save
                    else: 
                        count += 1
