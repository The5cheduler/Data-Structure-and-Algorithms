from typing import List

class Sorting:
    def insertion_sort(nums: List):
        # Traverse through all the possible index for nums array
        for idx in range(len(nums)):
            # Define and set inner_idx value to current idx
            inner_idx = idx
            # Run a while loop; inner_idx > 0 and previous element is greater than current inner idx than swap and reduce the inner idx value 1
            while inner_idx > 0  and nums[inner_idx - 1] > nums[inner_idx]:
                nums[inner_idx], nums[inner_idx - 1] = nums[inner_idx - 1], nums[inner_idx]
                inner_idx -= 1
        return nums

if __name__ == "__main__":
    data = [53, 47, 67, 32, 21, 33, 10]
    sorted_data = Sorting.insertion_sort(data)
    print(sorted_data)
