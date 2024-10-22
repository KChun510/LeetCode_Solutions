class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        filled = False
        mapS = {"low": float('inf'), "mid": float('inf'), "high" : float('inf') }

        for i in range(len(nums)):
            if nums[i] < mapS['low']:
                mapS['low'] = nums[i]
            elif nums[i] > mapS['low'] and nums[i] <= mapS['mid']:
                mapS['mid'] = nums[i]
            elif nums[i] > mapS['low'] and nums[i] > mapS['mid']:
                mapS['high'] = nums[i]
                filled = True
                break
        if filled:
            return True

        return False

        
        
