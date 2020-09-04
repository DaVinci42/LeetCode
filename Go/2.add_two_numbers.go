package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	left := l1
	right := l2
	var head *ListNode
	var preNode *ListNode
	carry := false
	for left != nil || right != nil || carry {
		sum := 0
		if left != nil {
			sum += left.Val
			left = left.Next
		}
		if right != nil {
			sum += right.Val
			right = right.Next
		}
		if carry {
			sum += 1
		}
		carry = sum >= 10
		n := &ListNode{sum % 10, nil}
		if head == nil {
			head = n
			preNode = n
		} else {
			preNode.Next = n
			preNode = n
		}
	}
	return head
}
