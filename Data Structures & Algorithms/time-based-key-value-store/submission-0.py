from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:

        values = self.TimeMap[key]

        TimeStamp = [t for t,v in values]
        
        i = bisect.bisect_right(TimeStamp,timestamp) - 1
        
        if i>=0:
            return values[i][1]
        return ""


