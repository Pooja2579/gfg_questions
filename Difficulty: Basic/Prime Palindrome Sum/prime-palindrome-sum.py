#User function Template for python3

class Solution:
    def getPPS(self, a, b):
        # code here 
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            
            if num %2 == 0:
                return False
            for i in range(3, int(num**0.5)+1, 2):
                if num % i == 0:
                    return False
            return True
    
        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        total = 0
        for num in range(a, b+1):
            if is_prime(num) and is_palindrome(num):
                total += num
    
        return total