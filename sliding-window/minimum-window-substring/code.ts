// O(M)
function hasAllChars(
	map: Map<string, number>,
	charMap: Map<string, number>,
): boolean {
	if (charMap.size != map.size) {
		return false;
	}

	for (let key of charMap.keys()) {
		if (!map.has(key) || map.get(key)! < charMap.get(key)!) {
			// Has 0 of Key
			// Has less key than char map
			return false;
		}
	}

	return true;
}

function canSpareChar(
	char: string,
	map: Map<string, number>,
	charMap: Map<string, number>,
): boolean {
	if (!charMap.has(char)) {
		// key not in map => doesnt matter how much we have
		return true;
	}

	// Map has one or more key
	// Map has > key than char map
	return map.has(char) && charMap.get(char)! < map.get(char)!;
}

export function minWindow(s: string, t: string): string {
	const tMap = new Map<string, number>();
	const sMap = new Map<string, number>();

	// Populate T Map O(M)
	for (const char of t) {
		tMap.set(char, (tMap.get(char) ?? 0) + 1);
	}

	let left = 0;
	let shortest = ` ${s}`;

	for (let right = 0; right < s.length; right++) {
		// If count is irrelivant => skip iteration
		if (!tMap.has(s[right])) {
			continue;
		}

		// Add newest char
		sMap.set(s[right], (sMap.get(s[right]) ?? 0) + 1);

		if (hasAllChars(sMap, tMap)) {
			// Has all chars and right count

			while (left <= right && canSpareChar(s[left], sMap, tMap)) {
				// We have all chars without the current char
				if (tMap.has(s[left])) {
					sMap.set(s[left], sMap.get(s[left])! - 1);

					if (sMap.get(s[left]) == 0) {
						// Remove if zero to allow size comparison
						sMap.delete(s[left]);
					}
				}

				// shrink window
				left++;
			}

			if (right - left + 1 < shortest.length) {
				shortest = s.substring(left, right + 1);
			}
		}
	}

	if (shortest.length > s.length) {
		return '';
	}

	return shortest;
}
