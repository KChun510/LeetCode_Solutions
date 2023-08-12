class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < len(nums):
            save_k = nums[0 : -k]    
            del nums[0: -k]
            nums += save_k
        else:
            for i in range(k):
                save = nums[0: -1]    
                del nums[0: -1]
                nums += save
