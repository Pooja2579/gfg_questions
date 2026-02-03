import math

class Solution:
    def countCoPrime(self, arr):
        k = 0
        for i in range(len(arr)-1):
            if math.gcd(arr[i], arr[i+1]) != 1:
                k+=1
                
        return k


# count_insertions = 0
# for i from 0 to n-2:
#     if gcd(arr[i], arr[i+1]) != 1:
#         count_insertions += 1
