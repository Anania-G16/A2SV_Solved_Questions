class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        needs = Counter()

        for n in nums:
            if not freq[n]:
                continue
            if needs[n]:
                freq[n] -= 1
                needs[n] -= 1
                needs[n + 1] += 1
            else:
                if freq[n+1] and freq[n+2]:
                    freq[n] -= 1
                    freq[n+1] -= 1
                    freq[n+2] -= 1
                    needs[n+3] += 1
                else:
                    return False

        return True

