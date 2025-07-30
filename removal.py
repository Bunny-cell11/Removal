def removeDuplicates(nums: list[int]) -> int:
    """
    Given a sorted array nums, remove the duplicates in-place such that each element appears only once.
    The relative order of the elements should be kept the same.

    You must do this by modifying the input array in-place without allocating extra space.

    Returns:
        The new length of the array after removing duplicates.
    """
    if not nums:
        return 0

    # 'k' will track the index of the next unique element
    k = 1
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous unique element
        if nums[i] != nums[k - 1]:
            # Move the current element to the position of the next unique element
            nums[k] = nums[i]
            # Increment 'k' to point to the next available position for a unique element
            k += 1

    # 'k' now represents the number of unique elements in the modified 'nums' array.
    # The elements in nums[:k] are the unique elements.
    return k

# Example Usage:
nums1 = [1, 1, 2]
length1 = removeDuplicates(nums1)
print(f"New length: {length1}, Modified array: {nums1[:length1]}")  # Output: New length: 2, Modified array: [1, 2]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
length2 = removeDuplicates(nums2)
print(f"New length: {length2}, Modified array: {nums2[:length2]}")  # Output: New length: 5, Modified array: [0, 1, 2, 3, 4]

nums3 = []
length3 = removeDuplicates(nums3)
print(f"New length: {length3}, Modified array: {nums3[:length3]}")  # Output: New length: 0, Modified array: []

nums4 = [1, 1, 1]
length4 = removeDuplicates(nums4)
print(f"New length: {length4}, Modified array: {nums4[:length4]}")  # Output: New length: 1, Modified array: [1]
