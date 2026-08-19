class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = {}
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)
        ans = (n - len(reserved)) * 2
        for seats in reserved.values():
            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}
            if left.isdisjoint(seats) and right.isdisjoint(seats):
                ans += 2
            elif (left.isdisjoint(seats) or
                  middle.isdisjoint(seats) or
                  right.isdisjoint(seats)):
                ans += 1
        return ans