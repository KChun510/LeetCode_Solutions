function largestGoodInteger(num: string): string {
	let res = "-1"
	let prev = num[0]
	let cnt = 0

	for (let curr of num.slice(1) as any) {
		if (prev == curr) {
			cnt++
			if (cnt == 2 && (parseInt(curr) > parseInt(res))) {
				res = curr
			}
		}
		else {
			cnt = 0
		}
		prev = curr
	}
	return res === "-1" ? "" : res.repeat(3)
};
