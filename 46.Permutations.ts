function permute(nums: number[]): number[][] {
	const len = nums.length - 1;
	let res: number[][] = [];

	function recur(nums_copy: number[], iter: number[]) {
		if (iter.length > len) res.push(iter);

		for (const num of nums_copy) {
			recur(nums_copy.filter(elem => elem != num), [...iter, num])
		}
		return res;
	}

	return recur(nums, [])
};
