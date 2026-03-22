class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        i = 0
        while i < len(temperatures):
            if len(stack) == 0 or temperatures[i] < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    result[stack[-1]] = i-stack[-1]
                    stack.pop()
                stack.append(i)
            i += 1 
        return result