### Non-overlapping problem (meeting room problem)
For these non-overlapping/overlapping problem, the key point is to find out the relation between the start point and end point of each interval. Then we can choose whether to delete/merge/oeprate iteratively.

| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 452. Minimum Number of Arrows to Burst Balloons | Medium | Time: O(nlogn), Space: O(n) |
| 435. Non-overlapping Intervals | Medium | Time: O(nlogn), Space: O(n) |
| 56. Merge Intervals | Medium | Time: O(nlogn), Space: O(n) |
| 252. Meeting Rooms | Easy | Time: O(nlogn), Space: O(1) |
| 253. Meeting Rooms II | Medium | Time: O(nlogn), Space: O(n) |
| 1094. Car Pooling | Medium | Time: O(nlogn), Space: O(n) |

### Monotonic problem
Monotonic technique is used for "next greater element problem". The order of the input array is fixed, when we scan the array, if a smaller/bigger element take the same effort for the previous elements, we can consider to use monotonic problem.
| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 503. Next Greater Element II | Medium | Time: O(n), Space: O(n) |
| 739. Daily Temperatures | Medium | Time: O(n), Space: O(n) |
| 1762. Buildings With an Ocean View | Medium | Time: O(n), Space: O(n) |
| 456. 132 Pattern | Medium | Time: O(n), Space: O(n) |
| 42. Trapping Rain Water | Hard | Time: O(n), Space: O(n) |
| 84. Largest Rectangle in Histogram | Hard | Time: O(n), Space: O(n) |
| 1944. Number of Visible People in a Queue | Hard | Time: O(n), Space: O(n) |
