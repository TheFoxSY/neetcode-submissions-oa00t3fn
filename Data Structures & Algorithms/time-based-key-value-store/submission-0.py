class TimeMap:

    def __init__(self):
        self.mySet = {} # pair of {key : [value , timestamp]}       
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mySet:
            self.mySet[key] = []
        self.mySet[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        res , values = "" , self.mySet.get(key, [])
        l , r = 0, len(values) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1    # not assigning res here because no timestamp
        
        return res

        
