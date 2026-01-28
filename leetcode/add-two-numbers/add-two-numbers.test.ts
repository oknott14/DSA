import { addTwoNumbers, ListNode } from './code';

function createList(arr: number[]) {
	const list = new ListNode(arr[0]);
	let curr = list;

	for (const num of arr.slice(1)) {
		curr.next = new ListNode(num);
		curr = curr.next;
	}

	return list;
}

function listToArr(list: ListNode | null): number[] {
	const arr = [];

	while (list != null) {
		arr.push(list.val);
		list = list.next;
	}

	return arr;
}
describe('addTwoNumbers', () => {
	test('Case 1', () => {
		const l1 = createList([2, 4, 3]);
		const l2 = createList([5, 6, 4]);
		const answer = [7, 0, 8];
		const result = addTwoNumbers(l1, l2);

		expect(listToArr(result)).toEqual(answer);
	});

	test('case 2', () => {
		const l1 = createList([9, 9, 9, 9, 9, 9, 9]);
		const l2 = createList([9, 9, 9, 9]);
		const answer = [8, 9, 9, 9, 0, 0, 0, 1];
		const result = addTwoNumbers(l1, l2);

		expect(listToArr(result)).toEqual(answer);
	});
});
