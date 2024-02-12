2. The merge function has a complexity of `O(n)`, the merge sort algorithm has a complexity of `O(n log n)`; The overall complexity is `O(n log n)`.
3. It recursively splits the list into two halves, sort each half, and then merge the two halves back together. 
```python
[8, 42, 25, 3, 3, 2, 27, 3]
[[8, 42, 25, 3], [3, 2, 27, 3]]
[[[8, 42], [25, 3]], [[3, 2], [27, 3]]]
[[[8], [42], [25], [3]], [[3], [2], [27], [3]]]
[[[8, 42], [3, 25]], [[2, 3], [3, 27]]]
[[[3, 8, 25, 42], [2, 3, 3, 27]]]
[2, 3, 3, 3, 8, 25, 27, 42]
```
4. Yes the divide-and-conquer strategy done manually matches the steps in the code. 