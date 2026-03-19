class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left = 0
            right = len(row)-1
            while left < right:
                row[left] = abs(row[left] - 1)
                row[right] = abs(row[right] - 1)
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1
            if right == left:
                row[left] = abs(row[left]-1)
        return image