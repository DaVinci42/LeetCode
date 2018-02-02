"""
413. Arithmetic Slices

A sequence of number is called arithmetic if it consists of at least three elements
and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given.
A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""


class Solution:

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A is None or len(A) < 3:
            return 0
        diff_list = list()
        for i in range(1, len(A)):
            diff = A[i] - A[i - 1]
            diff_list.append(diff)
        result = 0
        pre_diff, repeat_count = diff_list[0], 0
        for d in diff_list:
            if d == pre_diff:
                repeat_count += 1
            else:
                if repeat_count >= 3:
                    result += self.combine_in_count(repeat_count)
                pre_diff = d
                repeat_count = 1
        if repeat_count >= 3:
            result += self.combine_in_count(repeat_count)
        return result

    def combine_in_count(self, count):
        if count < 3:
            return 0
        elif count == 3:
            return 1
        else:
            return (1 + count - 2) / 2 * (count - 2)


s = Solution()
print(s.numberOfArithmeticSlices([1, 3, 5, 7, 9]))
