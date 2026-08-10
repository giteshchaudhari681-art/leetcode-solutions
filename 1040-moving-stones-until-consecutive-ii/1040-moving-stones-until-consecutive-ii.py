class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        maxMoves = max(
            stones[-1] - stones[1] + 1 - (n - 1),
            stones[-2] - stones[0] + 1 - (n - 1)
        )
        minMoves = n
        left = 0
        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1
            already = right - left + 1
            if already == n - 1 and stones[right] - stones[left] == n - 2:
                minmoves = min(minMoves, 2)
            else:
                minMoves = min(minMoves, n - already)
        return [minMoves, maxMoves]