"""
223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""


class Solution:

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        if area1 == 0:
            return area2
        if area2 == 0:
            return area1

        cover_l, cover_b, cover_r, cover_t, = max(
            A, E), max(B, F), min(C, G), min(D, H)

        cover_area = 0
        if cover_l < cover_r and cover_b < cover_t:
            cover_area = (cover_r - cover_l) * (cover_t - cover_b)

        return area1 + area2 - cover_area
