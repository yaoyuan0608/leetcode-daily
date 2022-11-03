### Sliding windows problem (general)
Sliding windows problem can be recognized as: find out the maximum/minimum subarray with some constrains. Then the basic constructure will be: use two pointers to represent the window, move right pointer to update something (value, count, dictionary..) until it reach the constrains, then move left pointer and narrow down the window.

| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 3. Longest Substring Without Repeating Characters | Medium | Time: O(n), Space: O(1) |
| 76. Minimum Window Substring | Hard | Time: O(n), Space: O(m) |
| 159. Longest Substring with At Most Two Distinct Characters | Medium | Time: O(n), Space: O(1) |
| 209. Minimum Size Subarray Sum | Medium | Time: O(n), Space: O(1) |
| 340. Longest Substring with At Most K Distinct Characters | Medium | Time: O(n), Space: O(k) |
| 424. Longest Repeating Character Replacement | Medium | Time: O(n), Space: O(k) |
| 487. Max Consecutive Ones II | Medium | Time: O(n), Space: O(1) |
| 713. Subarray Product Less Than K | Medium | Time: O(n), Space: O(k) |
| 1004. Max Consecutive Ones III | Medium | Time: O(n), Space: O(k) |
| 1208. Get Equal Substrings Within Budget | Medium | Time: O(n), Space: O(n) |
| 1493. Longest Subarray of 1's After Deleting One Element | Medium | Time: O(n), Space: O(1) |
| 1695. Maximum Erasure Value | Medium | Time: O(n), Space: O(n) |
| 1838. Frequency of the Most Frequent Element | Medium | Time: O(n), Space: O(n) |
| 2009. Minimum Number of Operations to Make Array Continuous | Hard | Time: O(nlogn), Space: O(1) |
| 2024. Maximize the Confusion of an Exam | Medium | Time: O(n), Space: O(1) |

This technique can be used to solve "at most k" (constrains) problem, and we can apply this technique to solve "exact k" problem, by finding the difference between helper(k) - helper(k-1).

| Question | Difficulty | Complexity |
| :---: | :---: | :---: |
| 930. Binary Subarrays With Sum | Medium | Time: O(n), Space: O(1) |
| 992. Subarrays with K Different Integers | Hard | Time: O(n), Space: O(k) |
| 1248. Count Number of Nice Subarrays | Medium | Time: O(n), Space: O(1) |
| 2062. Count Vowel Substrings of a String | Easy | Time: O(n), Space: O(1) |