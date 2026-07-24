class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False
        freq = Counter(nums)
        nums.sort()
        for n in nums:
            if freq[n] == 0:
                continue
            freq[n] -= 1
            for i in range(1, k):
                if not freq[n + i]:
                    return False
                freq[n+i] -= 1
        return True
