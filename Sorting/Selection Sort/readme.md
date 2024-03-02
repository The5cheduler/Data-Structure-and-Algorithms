# Selection Sort

Selection sort is a simple comparison-based sorting algorithm. It works by dividing the input array into two parts: the sorted part and the unsorted part. Initially, the sorted part is empty, and the unsorted part contains the entire array.

## Algorithm Steps

1. Find the minimum element in the unsorted part of the array.
2. Swap the minimum element with the first element of the unsorted part.
3. Move the boundary of the sorted part one element to the right.
4. Repeat steps 1-3 until the entire array is sorted.

## Steps:
- Loop through the length of the array
- Set current_min_idx to current index
- Again Loop through the length of the array starting from current_idx + 1
- Check if value at current min idx is greater than value at inner idx
- If it is than set current_min_idx to inner_idx
- Swap the value at outer index with value at current_min_idx