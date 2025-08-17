function findJudge(n: number, trust: number[][]): number {
	if (trust.length == 1) return trust[0][1]
	if (trust.length == 0) return n == 1 ? 1 : -1
	type Graph = Record<number, number[]>
	function build_graph(trust: number[][]): Graph {
		const graph: Graph = {}
		for (const [u, v] of trust) {
			if (!graph[u]) graph[u] = []
			if (!graph[v]) graph[v] = []
			graph[u].push(v)
		}
		return graph
	}
	const trust_graph = build_graph(trust)

	let no_trust = 0
	let suspect_judge_int = -1
	let suspect_judge_string = ""

	for (const key in trust_graph) {
		if (trust_graph[key].length == 0) {
			no_trust++
			suspect_judge_int = parseInt(key)
			suspect_judge_string = key
		}
		if (no_trust > 1) return -1
	}

	for (const key in trust_graph) {
		if (trust_graph[key].includes(suspect_judge_int) || key == suspect_judge_string) continue
		else {
			return -1
		}

	}

	return suspect_judge_int
};
