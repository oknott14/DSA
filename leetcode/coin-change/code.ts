export function coinChange(coins: number[], amount: number): number {
	let amounts = new Array<number>(amount + 1);
	amounts[0] = 0;
	let minSum = amount + 1;

	for (let i = 1; i < amounts.length; i++) {
		minSum = amount + 1;
		for (let j = 0; j < coins.length; j++) {
			if (i - coins[j] >= 0) {
				minSum = Math.min(minSum, amounts[i - coins[j]] + 1);
			}
		}

		amounts[i] = minSum;
	}

	if (amount < amounts[amount]) {
		return -1;
	} else {
		return amounts[amount];
	}
}

function dfs_coinChange(coins: number[], amount: number): number {
	coins = coins.sort((a, b) => b - a);
	let counts: Record<number, number> = {};
	let result = Infinity;

	let dfs = (sum: number, numberOfCoins: number) => {
		if (
			amount < sum ||
			result <= numberOfCoins ||
			(sum in counts && counts[sum] <= numberOfCoins)
		) {
			return;
		} else if (sum == amount) {
			result = Math.min(result, numberOfCoins);
			return;
		}

		counts[sum] = numberOfCoins;

		for (let coin of coins) {
			dfs(sum + coin, numberOfCoins + 1);
		}
	};

	dfs(0, 0);
	if (result == Infinity) {
		result = -1;
	}

	return result;
}
