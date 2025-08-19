class MinStack {
	private stack: (number | null)[]
	private len = 0
	private min: number[]
	constructor() {
		this.stack = []
	}

	push(val: number): void {
		this.stack.push(val)
		this.len++
		if (!this.min) {
			this.min = [val]
		} else if (val <= this.min[0]) {
			this.min = [val].concat(this.min)
		} else {
			this.min.push(val)
		}
	}

	pop(): void {
		if (this.stack[this.len - 1] === this.min[0]) {
			this.min = this.min.slice(1, this.min.length)
		}
		this.stack = this.stack.slice(0, -1)
		this.len--
	}

	top(): number {
		return this.stack[this.len - 1]
	}

	getMin(): number {
		return this.min[0]
	}
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
