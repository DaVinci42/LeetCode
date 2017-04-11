/**
 * Created by DaVinci42 on 2017/4/11.
 */

// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

// Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
// The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

// Please note that your returned answers (both index1 and index2) are not zero-based.
// You may assume that each input would have exactly one solution and you may not use the same element twice.

// Input: numbers={2, 7, 11, 15}, target=9
// Output: index1=1, index2=2

public class TwoSumII {

    public int[] main(int[] numbers, int target) {
        int tempPre = numbers[0] - 1;
        for (int i = 0; i < numbers.length; i++) {
            int pre = numbers[i];
            if (pre == tempPre) {
                continue;
            } else {
                tempPre = pre;
            }
            int tempPost = pre - 1;
            for (int j = i + 1; j < numbers.length; j++) {
                int post = numbers[j];
                if (tempPost == post) {
                    continue;
                }
                int sum = pre + post;
                if (sum == target) {
                    return new int[]{i + 1, j + 1};
                } else if (sum > target) {
                    break;
                } else {
                    tempPost = post;
                }
            }
        }
        return null;
    }
}
