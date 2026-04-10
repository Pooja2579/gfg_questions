class Solution:
    def isPalindrome(self, n):
		# code here
# 		if n<0:
# 		    return False
		    
		if str(abs(n)) == str(abs(n))[::-1]:
		    return True
		else:
		    return False