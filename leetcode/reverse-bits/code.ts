export function reverseBits(n: number): number {
	let result = 0;
	let bit = 0;
	for (let i = 0; i < 32; i++) {
		bit = n & 1;
		result = (result << 1) | bit;
		n = n >> 1;
	}
	return result >>> 0;
}
