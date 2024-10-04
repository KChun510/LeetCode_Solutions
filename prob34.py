class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        left, right = 0, len(nums) - 1
        left_b, right_b = False, False

        while(left <= right):
            mid = left + (right - left) // 2
            if nums[mid] == target or (right - left) < 4:
                while(left < len(nums) and right >= 0):
                    if nums[left] == target and not left_b:
                        output[0] = left
                        left_b = True
                    if nums[right] == target and not right_b:
                        output[1] = right
                        right_b = True
                    if output[0] > 0 and output[1] > 0:
                        return output
                    else:
                        left += 1
                        right -= 1

            elif nums[mid] > target:
                right = mid + 1
            elif nums[mid] < target:
                left = mid - 1

        return output


# Beats top 95% in speed 

# Because were already given a loosley sorted arr in decending order we can do a binary search.
# Eliminating half of the array, until we have a sub section with our 2 wanted vals.
# Once we have our sub section, turns into a two pointer problem

"""
Time Complexity: O(log n) + O(4) == O(log n)
Mem: O(1)
"""
            
            


        
