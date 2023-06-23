def firstBadVersion(self, n: int) -> int:
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid + 1): # If mid+1 is a bad version ... mid + 1 because we start from index 0 in the range of (n) 
            if not isBadVersion(mid): # And the previous version not bad 
                return mid + 1 
            high = mid - 1 # here we will lower our high-->(n-1) because all the next version is BAD !!!
        else:
            low = mid + 1 
