function zeroFilledSubarray(nums: number[]): number {
	let sum = 0
	let zero_count = 0

	if (nums.length === 1) return (nums[0] === 0 ? 1 : 0)
	for (let i = 0; i < nums.length; ++i) {
		if (nums[i] === 0) {
			zero_count++
		}
		else if (nums[i] !== 0 && zero_count > 0) {
			sum += (zero_count * (zero_count + 1)) / 2
			zero_count = 0
		}
	}
	sum += (zero_count * (zero_count + 1)) / 2

	return sum
};
