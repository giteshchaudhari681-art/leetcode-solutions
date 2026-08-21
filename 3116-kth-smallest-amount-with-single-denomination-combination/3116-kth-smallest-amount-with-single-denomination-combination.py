class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd
        from itertools import combinations

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << len(coins)):
                value = 1
                bits = 0

                for i in range(len(coins)):
                    if mask & (1 << i):
                        value = lcm(value, coins[i])
                        bits += 1

                        if value > x:
                            break

                if value <= x:
                    if bits % 2 == 1:
                        total += x // value
                    else:
                        total -= x // value

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left