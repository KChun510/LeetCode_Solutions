function maximumGap(nums: number[]): number {
	if (nums.length == 1) return 0;
	const freqMap = new Map<number, number>();
	let max_diff = 0;
	for (const n of nums) {
		freqMap.set(n, (freqMap.get(n) ?? 0) + 1);
	}
	const sortedMap = new Map(
		[...freqMap.entries()].sort(([a], [b]) => a - b)
	);
	let first = 0;
	let next = 0;
	let first_pass = true;
	for (const [key, value] of sortedMap) {
		if (first_pass) {
			next = key;
			first = key;
			first_pass = !first_pass;
		} else {
			const temp = next;
			next = key;
			first = temp;
		}

		if (next - first > max_diff) max_diff = next - first;
	}


	return max_diff;
};
