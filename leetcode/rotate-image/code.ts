export function rotate(matrix: number[][]): number[][] {
	let mid: number = (matrix.length - 1) / 2;
	let len: number = matrix.length % 2 ? 1 : 0.5;
	let x: number;
	let y: number;
	let x0: number;
	let y0: number;
	let temp: number;
	while (mid - len >= 0) {
		for (let pos = 0; pos < 2 * len; pos++) {
			x = 0 - len; // top left row
			y = 0 - len + pos; // top left col
			x0 = 0 - y;
			y0 = x;
			temp = matrix[mid + x][mid + y];

			while (mid + x0 != mid - len || mid + y0 != mid - len + pos) {
				matrix[mid + x][mid + y] = matrix[mid + x0][mid + y0];
				x = x0;
				y = y0;
				x0 = 0 - y;
				y0 = x;
			}

			matrix[mid + x][mid + y] = temp;
		}
		len++;
	}

	return matrix;
}
