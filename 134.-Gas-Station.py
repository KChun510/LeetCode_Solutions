class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # First things firt
        # if sum(gas) >= sum(cost), then we know there is a solution.
        # We can get around

        # Next gather an array called diff each elem = gas - cost

        # Then have a total called 0, save the first index that leads
        diff = []
        total = 0
        start_index = 0
        start = True
        if sum(gas) < sum(cost):
            return -1

        for index in range(len(gas)):
            diff.append(gas[index] - cost[index])

        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                total = 0
                start_index = 0
                start = True
            elif total > 0 and start:
                start = False
                start_index = i
        
        return start_index
            







        
