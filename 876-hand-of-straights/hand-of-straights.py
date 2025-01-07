class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = Counter(hand)
        elements = sorted(freq.keys())
        group = 0
        for element in elements:
            if freq[element] > 0:
                count = freq[element]
                for j in range(groupSize):
                    if element+j not in freq or freq[element+j] < count:
                        return False
                    freq[element+j]-=count
                group+=1
        return True