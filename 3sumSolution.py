class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr_len = len(nums)
        output = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = arr_len - 1
            while j < k:
                target = (nums[i] + nums[j]) * -1
                if target < nums[k]:
                    k -= 1
                elif target > nums[k] or target < nums[0]:
                    j += 1
                elif target == nums[k]:
                    output.add((nums[i], nums[j], nums[k])) 
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return [list(triple) for triple in output]

