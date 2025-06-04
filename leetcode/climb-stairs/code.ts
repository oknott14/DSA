export function climbStairs(n: number): number {
	if (n < 2) return 1;
	else if (n == 2) return 2;

	let n1: number = 1;
	let n2: number = 2;
	let temp: number;
	for (let i = 3; i < n; i++) {
		temp = n2;
		n2 += n1;
		n1 = temp;
	}

	return n1 + n2;
}
