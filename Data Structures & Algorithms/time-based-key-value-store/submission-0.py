from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.dict_time = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_time[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_time:
            return ""
        left = 0
        right = len(self.dict_time[key]) -1 
        while left <= right:
            mid = (left + right)//2
            if self.dict_time[key][mid][1] == timestamp:
                return self.dict_time[key][mid][0]
            if self.dict_time[key][mid][1] > timestamp: 
                right = mid - 1
            else:
                left = mid + 1
        if right < 0:
            return ""
        return self.dict_time[key][right][0]
