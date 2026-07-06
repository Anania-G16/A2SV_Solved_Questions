class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        answer = []

        for size in range(len(arr), 1, -1):
            max_index = 0
            for i in range(1, size):
                if arr[i] > arr[max_index]:
                    max_index = i

            if max_index == size - 1:
                continue

            if max_index != 0:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                answer.append(max_index + 1)

            arr[:size] = reversed(arr[:size])
            answer.append(size)

        return answer