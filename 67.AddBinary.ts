function addBinary(a: string, b: string): string {
	let top = (a.length > b.length ? a : b);
	let bottom = (a == top ? b : a);
	top = top.split('').reverse().join('');
	bottom = bottom.split('').reverse().join('');
	let result = "";
	let carry = "0";

	for (let i = 0; i < top.length; ++i) {
		const ones = [top[i], bottom[i], carry];
		let one_count = 0;


		for (const one of ones) {
			if (one === "1") ++one_count;
		}
		if (one_count >= 3) {
			result += "1";
			carry = "1";
		} else if (one_count == 2) {
			result += "0";
			carry = "1";
		} else if (one_count == 1) {
			result += "1";
			carry = "0";
		} else {
			result += "0";
			carry = "0";
		}


	}
	if (carry === "1") result += "1";
	return result.split('').reverse().join('');
};
