import { containsNearbyDuplicate } from './code';

describe('Contains Duplicate 2', () => {
	test('Case 1', () => {
		expect(containsNearbyDuplicate([1, 2, 3, 1], 3)).toBeTruthy();
	});

	test('Case 2', () => {
		expect(containsNearbyDuplicate([1, 0, 1, 1], 1)).toBeTruthy();
	});

	test('Case 3', () => {
		expect(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)).toBeFalsy();
	});

	test('Case 4', () => {
		expect(
			containsNearbyDuplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15),
		).toBeFalsy();
	});
});
