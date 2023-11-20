class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            # Check is the left side is sorted
            if nums[low] <= nums[mid]:
                # Check if its on the left side (I.e: Sorted side)
                if nums[low] <= nums[mid] < nums[high]:
                    high = mid - 1
                # Else it's on the right side ("Still sorted, but just rotated/out of place")
                # Remeber, that it's only sliced but still in ascending
                else:
                    low = mid + 1
            
            # IF right side is sorted
            else:
                # Check if it's on the right-side (I.e: Sorted side)
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                # else it's on the left side
                # The left side is sorted, but just indexed-rotated. 
                else:
                    high = mid - 1

        return -1



"""
Logic: This is binary sort with extra features. First we get our middle index, and check if the left or right side is sorted.

If a side is sorted, then we check if the target is in the sorted side. Else if its not in the sorted side, then we pick the other side. 


Run-Time: The binary sort algo has an O(log(n)) run-time, because we keep halfing our n//2 after each pass.
"""

        
