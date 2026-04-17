#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        if n == 1:
            print("GFG", end=' ')
        else:
            print('GFG', end=' ')
            self.printGfg(n-1)