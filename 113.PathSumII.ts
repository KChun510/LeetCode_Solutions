/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
function pathSum(root: TreeNode | null, targetSum: number): number[][] {
	let res: number[][] = [];

	function recur(node: TreeNode | null, iterSum: number, path: number[]) {
		if (!node) return; // Base case, either passed in empty node. I.e: Step pass a leaf. 

		iterSum += node.val; // Add the current node to sum
		path.push(node.val); // Add current node to path/stack.

		if (!node.left && !node.right && iterSum === targetSum) {
			res.push([...path]); // On success case, save path
		}

		recur(node.left, iterSum, path); // Left traverse
		recur(node.right, iterSum, path); // Right traverse

		path.pop(); // When reached base case. Stack frame is popped "backtrack". Have to make sure path, is updated to match.
	}
	recur(root, 0, [])
	return res;
};
