class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_X = int(str(x)[::-1])
        MIN = -2**31
        MAX = 2**31 - 1
        if reversed_X < MIN or reversed_X > MAX:
            return 0
        return sign * reversed_X