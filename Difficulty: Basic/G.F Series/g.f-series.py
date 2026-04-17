class Solution:
    def gfSeries(self, N : int) -> None:
        # code here
        def printGfSeries(n):
            if n == 1:
                return 0
            elif n == 2:
                return 1
            else:
                return (printGfSeries(n-2)**2 -printGfSeries(n-1))
        
    
        for i in range(1, N+1):
            print(printGfSeries(i), end=" ") 
        print()

        
        
