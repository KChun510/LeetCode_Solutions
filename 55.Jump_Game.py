class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True

        i = 0
        while i < len(nums):
            avail_jump = nums[i]
            max_jump = 0
            max_jump_idx = i + 1
            if avail_jump == 0 and i < len(nums) - 1: return False
            elif i + avail_jump >= len(nums) - 1: return True
            j = i + 1

            while j <= min(i + avail_jump, len(nums) - 1):
                if(nums[j] >= max_jump):
                    max_jump_idx = j
                    max_jump = nums[j]
                j += 1

            i = i + avail_jump if nums[i + avail_jump] != 0 and max_jump < avail_jump else max_jump_idx
        return True






          



            
        
        
