### backtrack problem
We can imagine the procedure of backtracking as the tree traversal. Starting from the root node, search for solutions that are located at the leaf nodes. Each intermediate node represents a partial candidate solution that could potentially lead us to a final valid solution. At each node, we would fan out to move one step further to the final solution.

```python
def backtrack(current_candidate, rest_candidates):
	if find a solution(current_candidate): # reach the end
		output this solution
		return
	for next_candidate in rest_candidates:
		if next_candidate is valid:
			place(next_candidate) # path.append(next_candidate)
			backtrack(next_candidate, rest_candidates)
			remove(next_candidate) # path.pop()
```

| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 37. Sudoku Solver | Hard | Time: O(9!^9), Space: O(81) |
| 77. Combinations | Hard | Time: O(knCk), Space: O(nCk) |
| 51. N-Queens | Hard | Time: O(n!), Space: O(n^2) |
| 52. N-Queens II | Hard | Time: O(n!), Space: O(n) |
| 489. Robot Room Cleaner | Hard | Time: O(n-m), Space: O(n-m) |
