from typing import List

def bubbleSort(nums:List) -> List:
    length = len(nums)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True

        if not swapped:
            break
    return nums

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubbleSort(arr))


