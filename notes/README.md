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

### Tree problem (general)
One trick to do tree problem is to think should we do some operations on the current node before/after the iteration, so to use the method of preorder traversal or postorder traversal.
| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 144. Binary Tree Preorder Traversal | Easy | Time: O(n), Space: O(n) |
| 145. Binary Tree Postorder Traversal | Easy | Time: O(n), Space: O(n) |
| 94. Binary Tree Inorder Traversal | Easy | Time: O(n), Space: O(n) |
| 270. Closest Binary Search Tree Value | Easy | Time: O(logn), Space: O(1) |
| 95. Unique Binary Search Trees II | Medium | Time: O(4^n/sqrt(n)), Space: O(4^n/sqrt(n)) |
| 110. Balanced Binary Tree | Easy | Time: O(nlogn), Space: O(1) |
| 222. Count Complete Tree Nodes | Medium | Time: O(n), Space: O(1) |
| 99. Recover Binary Search Tree | Medium | Time: O(n), Space: O(1) |
| 114. Flatten Binary Tree to Linked List | Medium | Time: O(n), Space: O(1) |
| 98. Validate Binary Search Tree | Medium | Time: O(n), Space: O(1) |
| 117. Populating Next Right Pointers in Each Node II | Medium | Time: O(n), Space: O(1) |
| 156. Binary Tree Upside Down | Medium | Time: O(n), Space: O(1) |
| 285. Inorder Successor in BST | Meidum | Time: O(n), Space: O(1) |
| 298. Binary Tree Longest Consecutive Sequence | Meidum | Time: O(n), Space: O(1) |
| 549. Binary Tree Longest Consecutive Sequence II | Meidum | Time: O(n), Space: O(1) |
| 450. Delete Node in a BST | Medium | Time: O(n), Space: O(1) |
| 437. Path Sum III | Meidum | Time: O(n), Space: O(n) |
| 333. Largest BST Subtree | Meidum | Time: O(n), Space: O(1) |
| 572. Subtree of Another Tree | Meidum | Time: O(n), Space: O(1) |
| 173. Binary Search Tree Iterator | Meidum | Time: O(n), Space: O(n) |
| 545. Boundary of Binary Tree | Meidum | Time: O(n), Space: O(n) |
| 272. Closest Binary Search Tree Value II | Hard | Time: O(n), Space: O(k) |
| 226. Invert Binary Tree | Easy | Time: O(n), Space: O(1) |
| 655. Print Binary Tree | Meidum | Time: O(n), Space: O(logn * 2^logn) |
| 897. Increasing Order Search Tree | Easy | Time: O(n), Space: O(1) |