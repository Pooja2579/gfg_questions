import math

class Solution:
    def countCoPrime(self, arr):
        k = 0
        for i in range(len(arr)-1):
            if math.gcd(arr[i], arr[i+1]) != 1:
                k+=1
                
        return k
            