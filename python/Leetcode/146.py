from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cache_capacity = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache_capacity.keys():
            value = self.cache_capacity.pop(key)
            self.cache_capacity[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_capacity.keys():
            self.cache_capacity.pop(key)
        elif len(self.cache_capacity) >= self.capacity:
            self.cache_capacity.popitem(last=False)
        self.cache_capacity[key] = value


obj = LRUCache(2)
param_1 = obj.get(2)
print(param_1)
params2 = obj.put(2,6)
param_3 = obj.get(1)
print(param_3)
params4 = obj.put(1,5)
params5 = obj.put(1,2)
param_6 = obj.get(1)
print(param_6)
param_7 = obj.get(2)
print(param_7)
