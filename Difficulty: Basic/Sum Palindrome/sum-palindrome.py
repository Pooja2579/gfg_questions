#User function Template for python3

class Solution:
    
        
    def isSumPalindrome (self, n):
        # code here 
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
    
        def reverse_check(num):
            return str(num)[::-1]
        iteration = 0
        while iteration<5:
            
            if is_palindrome(n):
                return n
    
            reversed_str = reverse_check(n)
            n = int(reversed_str)+n
            iteration +=1
    
        if is_palindrome(n):
            return n
        return -1 