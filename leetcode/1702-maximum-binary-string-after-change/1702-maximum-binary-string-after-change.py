class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        freq = Counter(binary)
        result = ""
        for i in range(len(binary)):
            if binary[i] == '1':
                result += '1'
            else:
                for i in range(freq['0']-1):
                    result += '1'
                result += '0'
                break
        while len(result) < len(binary):
            result += '1'
        return result
