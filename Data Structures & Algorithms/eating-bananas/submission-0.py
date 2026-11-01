import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = max(1, sum(piles) // h)
        high = max(piles)
        while low <= high:
            speed = (low + high) // 2 
            total_hours = 0
            for bananas in piles:
                total_hours += (bananas + speed - 1) // speed
                if total_hours > h: 
                    break
            if total_hours <= h:
                high = speed - 1
            else:
                low = speed + 1           
        return low
            

        