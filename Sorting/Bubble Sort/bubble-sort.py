from typing import List
class Sorting:
    def bubble_sort(nums:List):
        for idx in range(len(nums) - 1):
            swapped = False
            for inner_idx in range(len(nums) - idx - 1):
                if nums[inner_idx] >  nums[inner_idx + 1]:
                    nums[inner_idx], nums[inner_idx + 1] = nums[inner_idx + 1], nums[inner_idx]
                    swapped = True
            if not swapped:
                break
        return nums

if __name__ == "__main__":
    data = [53, 47, 67, 32, 21, 33, 10]
    sorted_data = Sorting.bubble_sort(data)
    print(sorted_data)
