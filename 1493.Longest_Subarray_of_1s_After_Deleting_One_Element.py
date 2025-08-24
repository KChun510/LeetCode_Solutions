class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_sub = 0
        i = 0
        no_zeros = True

        while i < len(nums):
            if nums[i] == 1:
                curr_sub = 1
                j = i + 1
                first_del = True
                while j < len(nums):
                    if nums[j] == 1:
                        curr_sub += 1
                    elif first_del:
                        first_del = False
                        no_zeros = False
                        i = j
                    else:
                        break
                    j += 1
                max_sub = max(curr_sub, max_sub)
                if first_del: 
                    i = j

            elif no_zeros:
                no_zeros = False
            i += 1
            
        return max_sub  - 1 if no_zeros else max_sub


                    
      
