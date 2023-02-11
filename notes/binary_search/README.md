### Binary Search problem
Binary search is always a powerful tool when we find there is a sorted componont in the problem. Moreover, Binary search can also be applied for such problem: find the minimum/maximum values, so that all elements in the list meet the requirment. Here is a useful template to find the smallest / largest values.

```python
def find_minimum(array):
	l, r = 0, len(array) # define minimum and maximum possible value
	while l < r:
		mid = l + (r - l) // 2
		if meet(mid): # if mid meets requirement, other values may also on left side
			r = mid
		else:
			l = mid + 1
	return l

def find_maximum(array): # problem changes to find the minimum val that doesn't meet requirements
	l, r = 0, len(array)
	while l < r:
		mid = l + (r - l) // 2
		if not meet(mid):
			r = mid
		else:
			l = mid + 1
	return l - 1
```

| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 33. Search in Rotated Sorted Array | Medium | Time: O(logn), Space: O(1) |
| 81. Search in Rotated Sorted Array II | Medium | Time: O(logn), Space: O(1) |
| 153. Find Minimum in Rotated Sorted Array | Medium | Time: O(logn), Space: O(1) |
| 154. Find Minimum in Rotated Sorted Array II | Hard | Time: O(logn), Space: O(1) |