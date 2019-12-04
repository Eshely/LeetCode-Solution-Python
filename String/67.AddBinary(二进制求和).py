class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 2进制转10进制，求和，再转为2进制

        # 2进制-->10进制
        a10, b10 = 0, 0
        for i, v in enumerate(a[::-1]):
            a10 += int(v) * 2 ** i
        for i, v in enumerate(b[::-1]):
            b10 += int(v) * 2 ** i

        ret = a10 + b10
        if ret == 0:
            return '0'

        # 10进制-->2进制
        s = ''
        while ret:
            s += str(ret % 2)
            ret //= 2
        return s[::-1]


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    s = Solution()
    print(s.addBinary(a, b))