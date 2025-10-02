class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 1 # Pointer to place the next unique element

        for right_pointer in range(1, len(nums)):# Pointer to explore the array
            if nums[right_pointer] != nums[right_pointer-1]: # Found a new unique element
                nums[left_pointer] = nums[right_pointer] # Place it at the left_pointer position
                left_pointer += 1 # Move the left_pointer to the next position
            # If it's a duplicate, just move the right_pointer forward
            right_pointer += 1 
        return left_pointer # The length of the array with unique elements