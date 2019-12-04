class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]  # 0b10101


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    s = Solution()
    print(s.addBinary(a, b))