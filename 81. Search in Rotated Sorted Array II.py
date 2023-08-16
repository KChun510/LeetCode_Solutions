class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        prev = nums[0]

        count = 0

        for index in range(len(nums)):
            if nums[index] == target:
                return True
            elif nums[index] < prev:
                count = index
            prev = nums[index]

        left_side = nums[0: count - 1]
        nums = nums[count: ]        
        nums += left_side

        start = 0
        end = len(nums) - 1
        count = 0

        while(count < len(nums)):
            middle = (start + end) // 2
            if nums[middle] == target:
                return True
            elif nums[middle] > target:
                end = middle
                count += 1
            elif nums[middle] < target:
                start = middle
                count += 1

    

        return False


