/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function partition(head: ListNode | null, x: number): ListNode | null {
	let lessThan_arr: number[] = []
	let greatThan_or_Eq: number[] = []
	let curr = head
	let curr_2 = head

	while (curr) {
		if (curr.val < x) {
			lessThan_arr.push(curr.val)
		} else if (curr.val >= x) {
			greatThan_or_Eq.push(curr.val)
		}
		curr = curr.next
	}

	while (curr_2) {
		if (lessThan_arr.length) {
			curr_2.val = lessThan_arr.shift()
		}
		else if (greatThan_or_Eq.length) {
			curr_2.val = greatThan_or_Eq.shift()
		}
		curr_2 = curr_2.next
	}

	return head
};
