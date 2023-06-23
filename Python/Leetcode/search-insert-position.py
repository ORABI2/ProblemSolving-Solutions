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
        # -----> we will use next line if we didn't find the target and need to know where it's position in the list
        return low
