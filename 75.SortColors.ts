/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
	const color_dic = {
		0: 0,
		1: 0,
		2: 0
	}

	for (const num of nums) {
		color_dic[num]++
	}

	let color_in = 0;
	for (const index in nums) {
		while (color_dic[color_in] == 0) { color_in++ }
		nums[index] = color_in
		color_dic[color_in]--
	}
};
