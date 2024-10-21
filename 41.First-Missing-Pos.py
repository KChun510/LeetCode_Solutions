class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Side case
        if len(nums) == 1 and nums[0] != 1:
            return 1

        nums.sort()
        smallest = 1
        first_pos = True

        # Side case, after sorting if only have negative vals 
        if nums[len(nums) - 1] <= 0:
            return 1

        for n in nums:
            if n <= 0:
                continue

            # Catch if the first positive == 1
            elif first_pos and n > 0:
                if n == 1:
                    first_pos = False
                    continue
                else:
                    return 1

            # Update the smallest value as we go/ account for dupes.
            elif smallest + 1 == n or smallest == n:
                smallest = n

            # return the first missing pos
            elif smallest + 1 != n:
                smallest += 1
                return smallest

        # We've gotten to the end, with nothing missing.
        # Return max + 1 
        return smallest + 1
        
