import { canJump } from './code';

describe('jump-game', () => {
	test('Base Case', () => {
		const input = [0];
		const output = true;
		expect(canJump(input)).toEqual(output);
	});

	test('Base Case by 1', () => {
		const input = [1, 1];
		const output = true;
		expect(canJump(input)).toEqual(output);
	});

	test('Base Case failure', () => {
		const input = [0, 1];
		const output = false;
		expect(canJump(input)).toEqual(output);
	});

	test('Base Case By N', () => {
		const input = [2, 0, 1];
		const output = true;
		expect(canJump(input)).toEqual(output);
	});

	test('Base Case Failure by N', () => {
		const input = [2, 0, 0, 1];
		const output = false;
		expect(canJump(input)).toEqual(output);
	});

	test('Will Jump < m', () => {
		const input = [3, 0, 2, 0, 1];
		const output = true;
		expect(canJump(input)).toEqual(output);
	});

	test('Cant Jump > m', () => {
		const input = [2, 0, 0, 0, 1];
		const output = false;
		expect(canJump(input)).toEqual(output);
	});

	test('Case 1', () => {
		const input = [2, 3, 1, 1, 4];
		const output = true;
		expect(canJump(input)).toEqual(output);
	});

	test('Case 2', () => {
		const input = [3, 2, 1, 0, 4];
		const output = false;
		expect(canJump(input)).toEqual(output);
	});
});
