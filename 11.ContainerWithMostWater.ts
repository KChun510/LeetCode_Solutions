function maxArea(height: number[]): number {
	let max_prod = 0;
	let w = 0;
	let h = 0;
	let left = 0;
	let right = height.length - 1;

	while (left < right) {
		w = right - left;
		h = Math.min(height[left], height[right]);
		const prod = w * h;
		if (prod > max_prod) max_prod = prod;

		// Greedy approach. 
		// Always take the greater height.
		if (height[left] <= height[right]) ++left;
		else --right;
	}
	return max_prod;
};
