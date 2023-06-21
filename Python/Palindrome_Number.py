class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted_str = str(x)
        reversed_str = converted_str[::-1] 
        if converted_str == reversed_str:
            return True
        else:
            return False
