class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count = {}
        for num in hand:
            count[num] = 1 + count.get(num, 0)

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if count.get(i,0) == 0:
                        return False
                    count[i] -= 1
        return True