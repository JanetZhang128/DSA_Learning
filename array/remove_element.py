class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0# Pointer for the next position to place a non-val element

        for i in range(len(nums)): # Iterate through each element in the array
            if nums[i] != val:# If the current element is not equal to val
                nums[k] = nums[i]# Place it at the k-th position
                k += 1# Move the pointer k to the next position

        del nums[k:]# Optional: Remove the extra elements beyond the new length
        return k# The new length of the array without val elements