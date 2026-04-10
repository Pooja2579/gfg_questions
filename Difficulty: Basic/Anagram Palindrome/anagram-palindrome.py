#User function Template for python3

class Solution:

    def isPossible(self, S):

        # code here
        freq = {}

        for char in S:
            freq[char] = freq.get(char, 0)+1
    
        odd_count = 0
        for count in freq.values():
            if count%2 != 0: #odd
                odd_count +=1
        
        return 1 if odd_count<=1 else 0