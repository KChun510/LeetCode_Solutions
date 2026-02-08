function singleNumber(nums: number[]): number {
	let map: { [key: number]: number } = {};

	for (const num of nums) {
		if (map[num]) map[num] += 1;
		else map[num] = 1;
	}

	for (const key in map) {
		const parse_num: number = Number(map[key]);
		if (parse_num !== 3) return Number(key);
	}

	return 0;
};
