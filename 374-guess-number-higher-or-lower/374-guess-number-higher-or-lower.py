# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n
        
        while(low<=high):
            m = (low+high)//2
            print(low,high,m)
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                low = m+1       
            elif guess(m) == -1:
                high = m-1
                
            
                
        return -1
        