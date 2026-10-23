class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(word):
            value = ""
            for char in word:
                value += str(ord(char) - ord('a'))
            return int(value)

        return convert(firstWord) + convert(secondWord) == convert(targetWord)
        