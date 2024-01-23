from typing import List


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return formatted

def MergeSort(nums: List[int], low: int, high: int) -> None:
    serialized = serialize(nums)
    if low < high:
        mid = low + (high - low) // 2

        # Sorting the first and second halves
        MergeSort(nums, low, mid)
        serialized = serialize(nums)
        MergeSort(nums, mid + 1, high)
        serialized = serialize(nums)
        Merge2SortedList(nums, low, mid, high)
        serialized = serialize(nums)

def Merge2SortedList(nums: List[int], low: int, mid: int, high: int) -> None:

    serialized = serialize(nums)
    n1 = mid - low + 1
    n2 = high - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        serialized = serialize(nums)
        L[i] = nums[low + i]
    for j in range(n2):
        serialized = serialize(nums)
        R[j] = nums[mid + 1 + j]

    i, j, k = 0, 0, low

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            nums[k] = L[i]
            serialized = serialize(nums)
            i += 1
        else:
            nums[k] = R[j]
            serialized = serialize(nums)
            j += 1
        k += 1

    while i < n1:
        nums[k] = L[i]
        serialized = serialize(nums)
        i += 1
        k += 1

    while j < n2:
        nums[k] = R[j]
        serialized = serialize(nums)
        j += 1
        k += 1
    serialized = serialize(nums)



if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    low = 0
    high = len(arr) - 1
    MergedArray = MergeSort(arr, low, high)
    print(MergedArray)
