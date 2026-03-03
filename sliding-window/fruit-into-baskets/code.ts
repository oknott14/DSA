// O(N) runtime, O(1) space
export function totalFruit(fruits: number[]): number {
	if (!fruits.length) {
		return 0;
	}

	let left = 0;
	let temp = 0;
	let type1 = fruits[0];
	let type2 = fruits[0] + 1;
	let lastSame = 0;
	let longest = 0;

	for (let right = 0; right < fruits.length; right++) {
		if (fruits[right] == type2) {
			lastSame = right;
			temp = type1;
			type1 = type2;
			type2 = temp;
		} else if (fruits[right] != type1) {
			left = lastSame;
			lastSame = right;
			type2 = type1;
			type1 = fruits[right];
		}
		longest = Math.max(longest, right - left + 1);
	}

	return longest;
}

// O(N) runtime, O(N) space
export function totalFruitUsingMap(fruits: number[]): number {
	const fruitTypes = new Map<number, number>();
	let left = 0;
	let totalFruit = 0;

	for (let right = 0; right < fruits.length; right++) {
		// Add one to right count or initialize as 1
		fruitTypes.set(fruits[right], (fruitTypes.get(fruits[right]) ?? 0) + 1);

		if (fruitTypes.size <= 2) {
			// if total unique fruits fit in the basket => compare longest
			totalFruit = Math.max(totalFruit, right - left + 1);
		} else {
			// Otherwise decrement left and remove if zero
			fruitTypes.set(fruits[left], fruitTypes.get(fruits[left])! - 1);

			if (fruitTypes.get(fruits[left]) == 0) {
				fruitTypes.delete(fruits[left]);
			}

			left++;
		}
	}

	return totalFruit;
}
