def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]
            if guess == target:
                return nums.index(target)
            if guess > target:
                high = mid - 1
            else:
                low = mid + 1
        return low
