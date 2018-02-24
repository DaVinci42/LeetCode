"""
454. 4Sum II

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500.
All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution:

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        if (A is None or len(A) == 0 or
                B is None or len(B) == 0 or
                C is None or len(C) == 0 or
                D is None or len(D) == 0):
            return 0

        for nums in [A, B, C, D]:
            nums.sort()

        A_B_sum_dict = dict()
        for a in A:
            for b in B:
                count = 0 if a + b not in A_B_sum_dict else A_B_sum_dict[a + b]
                count += 1
                A_B_sum_dict[a + b] = count

        count = 0
        for c in C:
            for d in D:
                s = c + d
                if -s in A_B_sum_dict:
                    count += A_B_sum_dict[-s]
        return count
