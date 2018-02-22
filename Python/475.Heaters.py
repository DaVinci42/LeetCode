"""
475. Heaters

Winter is coming!
Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line,
find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately,
and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation:
The only heater was placed in the position 2, and if we use the radius 1 standard,
then all the houses can be warmed.

Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation:
The two heater was placed in the position 1 and 4. We need to use radius 1 standard,
then all the houses can be warmed.
"""


class Solution:

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        if houses is None or len(houses) == 0:
            return 0
        if heaters is None or len(heaters) == 0:
            return 0

        houses.sort()
        heaters.sort()

        min_radius = 0
        for i in houses:
            radius = self._min_radius(i, heaters)
            if radius > min_radius:
                min_radius = radius
        return min_radius

    # find the nearest heater
    def _min_radius(self, position, heaters):
        left, right = 0, len(heaters) - 1
        if position <= heaters[left]:
            return heaters[left] - position
        if position >= heaters[right]:
            return position - heaters[right]

        while right - left > 1:
            mid = int((left + right) / 2)
            mid_position = heaters[mid]
            if mid_position == position:
                return 0
            if mid_position > position:
                right = mid
            if mid_position < position:
                left = mid
        left_v, right_v = heaters[left], heaters[right]
        if position - left_v >= right_v - position:
            return right_v - position
        else:
            return position - left_v
