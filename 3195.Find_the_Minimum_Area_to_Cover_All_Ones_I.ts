function minimumArea(grid: number[][]): number {
	const one_loc_col: Record<number, number> = {}
	const one_loc_row: Record<number, number> = {}
	let one_count = 0

	for (let row = 0; row < grid.length; ++row) {
		for (let col = 0; col < grid[0].length; ++col) {
			const curr_val = grid[row][col]
			if (curr_val === 1) {

				if (one_loc_col[0] === undefined) one_loc_col[0] = col
				else if (col < one_loc_col[0]) one_loc_col[0] = col

				if (!one_loc_col[1]) one_loc_col[1] = col
				else if (col > one_loc_col[1]) one_loc_col[1] = col

				if (one_loc_row[0] === undefined) one_loc_row[0] = row


				if (one_loc_row[1] === undefined) one_loc_row[1] = row
				else if (one_loc_row[1] < row) one_loc_row[1] = row

				one_count++
			}
		}
	}
	const test_res = ((one_loc_col[1] + 1) - one_loc_col[0]) * ((one_loc_row[1] + 1) - one_loc_row[0])
	return test_res ? test_res : one_count
}
