def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l) // 2
            if ((m + 1 == len(nums) or nums[m] > nums[m+1]) and (m == 0 or nums[m] > nums[m-1])):
            # in the constraints it say "an element is always considered to be strictly greater than a neighbor that is outside the array" so with
            # m + 1 == len(num) and m == 0 ensures we are out of the range
                return m
            if m > 0 and nums[m] < nums[m-1]: 
                r = m - 1
                
            else:
                l = m + 1
        return l
