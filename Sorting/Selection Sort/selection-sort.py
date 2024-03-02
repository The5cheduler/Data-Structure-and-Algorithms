from typing import List

class Sorting:
    def selection_sort(nums: List):
        for idx in range(len(nums)):
            current_min_idx = idx
            for new_idx in range(idx + 1, len(nums)):
                if nums[current_min_idx] > nums[new_idx]:
                    current_min_idx = new_idx

            nums[idx], nums[current_min_idx] = nums[current_min_idx], nums[idx]

        return nums

if __name__ == "__main__":
    data = [53, 47, 67, 32, 21, 33, 10]
    sorted_data = Sorting.selection_sort(data)
    print(sorted_data)