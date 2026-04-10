#User function Template for python3
class Solution:
    def isDeciBinPalin (self, N):
        # code here 
        def chnage_binary(num):
            res = ''
            while num>0:
                res = str(num%2) + res
                num //= 2
            return res
        
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        if not is_palindrome(N):
            return "No"
        
        binary = chnage_binary(N)
    
        if binary == binary[::-1]:
            return "Yes"
        else:
            return "No"