class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        
        for i in range(len(gas)):
            current = gas[i] - cost[i]
            total += current
            if total < 0:
                start = i + 1
                total = 0
        
        return start
            
        