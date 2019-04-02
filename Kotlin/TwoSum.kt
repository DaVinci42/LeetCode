class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        if (nums.isEmpty()) return intArrayOf(0, 0)

        val map = mutableMapOf<Int, Int>()

        nums.forEachIndexed { i, v ->
            if (target - v !in map) {
                map[v] = i
            } else {
                return intArrayOf(i, map[target - v]!!)
            }
        }
        return intArrayOf(0, 0)
    }
}