class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left = 0
        right = len(skill)-1
        sum = skill[left] + skill[right]
        result = 0
        while left < right:
            if sum !=  skill[left] + skill[right]:
                return -1
            result += skill[left] * skill[right]
            left += 1
            right -= 1
        return result

