import { eraseOverlapIntervals } from './code';

describe('non-overlapping-intervals', () => {
	test('returns 0 on empty list', () => {
		const input: [number, number][] = [];
		const output = 0;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('returns 0 on ordered non-overlapping interval list', () => {
		const input: [number, number][] = [
			[1, 2],
			[3, 4],
			[5, 6],
		];
		const output = 0;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('returns 0 on un-ordered non-overlapping interval list', () => {
		const input: [number, number][] = [
			[5, 6],
			[1, 2],
			[3, 4],
		];
		const output = 0;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('removes single overlapping interval', () => {
		const input: [number, number][] = [
			[1, 2],
			[1, 2],
			[3, 4],
		];
		const output = 1;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('removes many overlapping intervals', () => {
		const input: [number, number][] = [
			[1, 2],
			[1, 2],
			[3, 4],
			[3, 4],
		];
		const output = 2;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('returns minimum intervals', () => {
		const input: [number, number][] = [
			[1, 2],
			[3, 4],
			[1, 2],
			[5, 6],
			[7, 8],
		];
		const output = 1;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('Returns small interval when it crosses 2 larger ones', () => {
		const input: [number, number][] = [
			[1, 5],
			[5, 10],
			[4, 6],
		];
		const output = 1;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('Case 1', () => {
		const input: [number, number][] = [
			[1, 2],
			[2, 3],
			[3, 4],
			[1, 3],
		];

		const output = 1;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input: [number, number][] = [
			[1, 2],
			[1, 2],
			[1, 2],
		];

		const output = 2;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});

	test('Case 3', () => {
		const input: [number, number][] = [
			[1, 2],
			[2, 3],
		];

		const output = 0;

		expect(eraseOverlapIntervals(input)).toEqual(output);
	});
});
