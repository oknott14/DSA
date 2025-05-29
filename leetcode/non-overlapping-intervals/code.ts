export function eraseOverlapIntervals(intervals: [number, number][]): number {
	if (!intervals.length) return 0;
	intervals = intervals.sort((a, b) => a[1] - b[1]);

	let lastEnd: number = intervals[0][1];
	let count: number = 0;

	for (let idx = 1; idx < intervals.length; idx++) {
		if (intervals[idx][0] < lastEnd) {
			count++;
		} else {
			lastEnd = intervals[idx][1];
		}
	}
	return count;
}
