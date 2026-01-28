export class ListNode {
	val: number;
	next: ListNode | null;
	constructor(val?: number, next?: ListNode | null) {
		this.val = val === undefined ? 0 : val;
		this.next = next === undefined ? null : next;
	}
}

export function addTwoNumbers(
	l1: ListNode | null,
	l2: ListNode | null
): ListNode | null {
	const resultList: ListNode = new ListNode();
	let curr = resultList;
	let carry = 0;

	while (l1 != null && l2 != null) {
		const currentValue = (l1.val + l2.val + carry) % 10;
		carry = Math.floor((l1.val + l2.val + carry) / 10);
		curr.next = new ListNode(currentValue);
		curr = curr.next;
		l1 = l1.next;
		l2 = l2.next;
	}

	let remaining = l1 ?? l2;

	while (remaining != null && carry != 0) {
		const currentValue = (remaining.val + carry) % 10;
		carry = Math.floor((remaining.val + carry) / 10);
		remaining = remaining.next;
		curr.next = new ListNode(currentValue);
		curr = curr.next;
	}

	if (carry != 0) {
		curr.next = new ListNode(carry);
	} else {
		curr.next = remaining;
	}

	return resultList.next;
}
