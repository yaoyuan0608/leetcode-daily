### Binary Search problem
Binary search is always a powerful tool when we find there is a sorted componont in the problem. Moreover, Binary search can also be applied for such problem: find the minimum/maximum values, so that all elements in the list meet the requirment. Here is a useful template to find the smallest / largest values.
```python
def minimum_binary_search(array, func):
  l = 0
  r = len(array)
  while l < r:
    mid = l + (r - l) // 2
    # for all value greater/equal than array[mid], make func(x) true
    if func(mid):
      r = mid
    else:
      l = mid + 1
  return l
```
```python
def maximum_binary_search(array, func):
  l = 0
  r = len(array)
  while l < r:
    mid = l + (r - l) // 2
    # for all value greater/equal than array[mid], make func(x) false, than mid-1 is the maximum answer
    if not func(mid):
      r = mid
    else:
      l = mid + 1
  return l-1
```
| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 33. Search in Rotated Sorted Array | Medium | Time: O(logn), Space: O(1) |
| 81. Search in Rotated Sorted Array II | Medium | Time: O(logn), Space: O(1) |
| 153. Find Minimum in Rotated Sorted Array | Medium | Time: O(logn), Space: O(1) |
| 154. Find Minimum in Rotated Sorted Array II | Hard | Time: O(logn), Space: O(1) |
