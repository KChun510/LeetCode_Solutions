function countDays(days: number, meetings: number[][]): number {
	// Zero, do nothing, Neg, a comes before b. Pos, a comes after b.
	meetings.sort((a, b) => (a[0] - b[0]) || (a[1] - b[1]))
	let prev_end = 0

	for (const meeting of meetings) {
		const end = meeting[1]
		const start = Math.max(meeting[0], prev_end + 1)
		const length = end - start + 1
		days -= Math.max(length, 0)
		prev_end = Math.max(end, prev_end)
	}
	return days
};
