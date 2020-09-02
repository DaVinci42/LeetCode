package main

func twoSum(nums []int, target int) []int {
	if nums == nil {
		return []int{}
	}

	m := make(map[int]int)
	for i, v := range nums {
		if val, ok := m[target-v]; ok {
			return []int{val, i}
		}
		m[v] = i
	}
	return []int{}
}
