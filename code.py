#User function Template for python3
class Solution:
    def totHammingDist(self, arr):
        # code here
        
        def cntOne(n):
            cnt = 0 
            while n > 0:
                if n%2 == 1:
                    cnt +=1
                n = n//2
            return cnt
                
        result = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                xor = arr[i]^arr[j]
                result = result + cntOne(xor)
                
        return result