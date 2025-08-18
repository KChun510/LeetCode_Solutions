function check_left(left_node: TreeNode | null, right_node: TreeNode | null) {
	if (left_node.left && right_node.left) return true
	else return false
}

function check_right(left_node: TreeNode | null, right_node: TreeNode | null) {
	if (left_node.right && right_node.right) return true
	else return false
}

function check_mirror_out(left_node: TreeNode | null, right_node: TreeNode | null) {
	if ((left_node.left && right_node.right) && (!left_node.right && !right_node.left)) return true
	else return false
}

function check_mirror_in(left_node: TreeNode | null, right_node: TreeNode | null) {
	if ((left_node.right && right_node.left) && (!left_node.left && !right_node.right)) return true
	else return false
}

function check_equal_level(left_level: number[], right_level: number[]): boolean {
	right_level.reverse()
	for (let i = 0; i < 2; ++i) {
		if (left_level[i] !== right_level[i]) return false
	}
	return true
}

function check_next_row(left_node: TreeNode | null, right_node: TreeNode | null) {
	if (left_node?.left || left_node?.right || right_node?.left || right_node?.right) return true
	else return false
}

function isSymmetric(root: TreeNode | null): boolean {
	let left_stack = []
	let right_stack = []

	if (!root.left || !root.right) return (!root.left && !root.right ? true : false)

	left_stack.push(root.left)
	right_stack.push(root.right)

	if (root.left.val != root.right.val) return false

	while (left_stack.length && right_stack.length) {
		const left_node = left_stack.pop()
		const right_node = right_stack.pop()

		// Ensures there is both a L & R, node on each side
		if (check_left(left_node, right_node) && check_right(left_node, right_node)) {
			if (!check_equal_level([left_node.left.val, left_node.right.val], [right_node.left.val, right_node.right.val])) return false

			if (check_next_row(left_node.left, left_node.right) && check_next_row(right_node.left, right_node.right)) {
				left_stack.push(left_node.left)
				left_stack.push(left_node.right)
				right_stack.push(right_node.right)
				right_stack.push(right_node.left)
			}
		} else if (check_mirror_out(left_node, right_node)) {
			if (!check_equal_level([left_node.left.val], [right_node.right.val])) return false

			if (check_next_row(left_node.left, null) && check_next_row(null, right_node.right)) {
				left_stack.push(left_node.left)
				right_stack.push(right_node.right)
			}
		} else if (check_mirror_in(left_node, right_node)) {
			if (!check_equal_level([left_node.right.val], [right_node.left.val])) return false


			if (check_next_row(null, left_node.right) && check_next_row(right_node.left, null)) {
				left_stack.push(left_node.right)
				right_stack.push(right_node.left)
			}
			// If all other constraints fail, and next row. Return false. 
		} else if (check_next_row(left_node, right_node)) {
			return false
		}
	}
	return true
};
