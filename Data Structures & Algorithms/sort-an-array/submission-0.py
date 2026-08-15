class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # Step 1: Build a Max-Heap from the array
        # Start from the last non-leaf node and heapify down to index 0
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(nums, n, i)

        # Step 2: Extract elements from the heap one by one
        for i in range(n - 1, 0, -1):
            # Move the current root (maximum element) to the end
            nums[0], nums[i] = nums[i], nums[0]
            
            # Call max heapify on the reduced heap to restore heap property
            self._heapify(nums, i, 0)
            
        return nums

    def _heapify(self, nums: list[int], n: int, i: int) -> None:
        """Helper to maintain the max-heap property for a subtree rooted at index i."""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child exists and is greater than root
        if left < n and nums[left] > nums[largest]:
            largest = left

        # Check if right child exists and is greater than the current largest
        if right < n and nums[right] > nums[largest]:
            largest = right

        # If the largest element is not the root, swap and continue heapifying down
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            self._heapify(nums, n, largest)
