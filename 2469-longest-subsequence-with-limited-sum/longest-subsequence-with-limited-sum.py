class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        answer = len(queries) * [0]
        queryList =  list(enumerate(queries))
        queryList.sort(key = lambda x: x[1])
        left = 0
        right = 0
        prefix = 0
        count = 0
        while right < len(queryList):
            if prefix == queryList[right][1]:
                answer[queryList[right][0]] = count
                right += 1
            elif prefix > queryList[right][1]:
                answer[queryList[right][0]] = count-1
                right += 1

            else:
                if left >= len(nums):
                    answer[queryList[right][0]] = count
                    right += 1
                else:
                    prefix += nums[left]
                    count += 1
                    left += 1
        return answer
