class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numbs_dic = {}
        pop_count = 0
        for number in nums:
            numbs_dic[number] = 0

        for index in range(len(nums)):
            if numbs_dic[nums[index - pop_count]] >= 2:
                pop_count += 1
                nums.pop(index- pop_count)
            else:
                numbs_dic[nums[index - pop_count]] += 1
        
        print(len(nums), nums)
