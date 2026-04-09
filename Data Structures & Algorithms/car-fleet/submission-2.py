class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = zip(position, speed)
        pair = list(pair)
        pair.sort()
        stack= []

        for p, s in pair[::-1]:
            time = (target - p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()     
        
        return len(stack)



        
            
        