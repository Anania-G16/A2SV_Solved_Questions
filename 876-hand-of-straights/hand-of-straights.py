class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        hand.sort()
        for num in hand:
            if freq[num] == 0:
                continue
            freq[num] -= 1
            for i in range(1, groupSize):
                if not freq[num + i]:
                    return False
                freq[num + i] -= 1
        return True