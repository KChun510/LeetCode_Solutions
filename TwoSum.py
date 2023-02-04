class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in (range(len(nums))):
            val1 = target - nums[i]
            val2 = target - val1  #Val2 is the remainder 
            check = i + 1
            if val1 in nums and val2 in nums:#If val1 and remainder in array, loop and return indecie
                while (check <= (len(nums)-1)):
                    if (nums[i] + nums[check] == target):
                        return (i, check)
                    else:
                        check += 1 
