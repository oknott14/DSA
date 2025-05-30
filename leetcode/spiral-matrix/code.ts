export function spiralOrder(matrix: number[][]): number[] {
	let j: number = -1; // left border
	let m: number = matrix[0].length; // right border
	let k: number = -1; // top border
	let n: number = matrix.length; // bottom border
	let row: number = 0;
	let col: number = 0;
	let inc: number = 1;
	let result: number[] = new Array(matrix.length * matrix[0].length);
	let inserted: number = 0;
	while (inserted < result.length) {
		while (j < col && col < m) {
			result[inserted++] = matrix[row][col];
			col += inc;
		}
		col -= inc;
		row += inc;

		while (k < row && row < n) {
			result[inserted++] = matrix[row][col];
			row += inc;
		}
		row -= inc;
		col -= inc;

		if (inc < 0) {
			// Moving Left or Up
			n--;
			j++;
			inc = 1;
		} else {
			m--;
			k++;
			inc = -1;
		}
	}

	return result;
}
