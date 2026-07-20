class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        maxScore = 0
        tokens.sort()
        low = 0
        high = len(tokens)-1
        while low <= high:
            if power >= tokens[low]:
                power -= tokens[low]
                score += 1
                maxScore = max(maxScore, score)
                low += 1
            elif power < tokens[low] and score > 0:
                power += tokens[high]
                score -= 1
                high -= 1
            else:
                break
        return maxScore

