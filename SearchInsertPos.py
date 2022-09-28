def searchInsert(nums, target):
        
    prev, nxt = 0 , 1
    i = 0
    mx = max(range(len(nums))) 
    mn = min(range(len(nums)))

    if target in nums:
        for n in nums:
            if n == target:
                return i
            else:
                i += 1

    else:

        if target > nums[mx]:
            return mx + 1

        elif target < nums[mn]:
            return mn

        while nxt <= len(nums):
                if target > nums[prev] and target < nums[nxt]:
                    return nxt
                else:
                    nxt += 1
                    prev += 1
