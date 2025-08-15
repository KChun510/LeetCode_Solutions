function check_3_x_3(board: string[][]): boolean {
	const x3_rows = board.length
	const x3_cols = board[0].length
	let tracking_dic = {}

	for (let row = 0; row < x3_rows; row += 3) {
		for (let col = 0; col < x3_cols; col += 3) {
			for (let inner_row = row; inner_row < 3 + row; ++inner_row) {
				for (let inner_col = col; inner_col < 3 + col; ++inner_col) {
					if (board[inner_row][inner_col] == ".") continue
					const curr_val = parseInt(board[inner_row][inner_col])
					if (tracking_dic[curr_val]) {
						tracking_dic[curr_val]++
					} if (tracking_dic[curr_val] > 1) {
						console.log(tracking_dic)
						return false
					} else {
						tracking_dic[curr_val] = 1;
					}
				}
			}
			tracking_dic = {}
		}
	}
	return true
}


function isValidSudoku(board: string[][]): boolean {
	let tracking_dic = {}
	const col_len = board[0].length
	const total_row = board.length

	for (const row in board) {
		for (const col of board[row]) {
			if (col == ".") continue
			const col_val = parseInt(col)
			if (tracking_dic[col_val]) {
				tracking_dic[col_val]++
			} if (tracking_dic[col_val] > 1 || (col_val < 1 || col_val > 9)) {
				return false
			} else {
				tracking_dic[col_val] = 1;
			}
		}
		tracking_dic = {}
	}

	for (let col = 0; col < col_len; ++col) {
		for (let row = 0; row < total_row; ++row) {
			if (board[row][col] == ".") continue
			const curr_val = board[row][col]
			if (tracking_dic[curr_val]) {
				tracking_dic[curr_val]++
			} if (tracking_dic[curr_val] > 1) {
				return false
			} else {
				tracking_dic[curr_val] = 1;
			}
		}
		tracking_dic = {}
	}


	return check_3_x_3(board)
};
