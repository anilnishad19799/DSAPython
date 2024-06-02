from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.storekeyvalue = defaultdict(list)
        self.storelistval = [[],[]]

    def set(self, key: str, value: str, timestamp: int):
        # self.storelistval = self.storekeyvalue[key]
        if key in self.storekeyvalue.keys():
            self.storelistval = self.storekeyvalue[key]
            self.storelistval[0].append(value)
            self.storelistval[1].append(timestamp)
            self.storekeyvalue[key] = self.storelistval
        else:
            self.storelistval = [[],[]]
            self.storelistval[0].append(value)
            self.storelistval[1].append(timestamp)
            self.storekeyvalue[key] = self.storelistval

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.storekeyvalue.keys():
            return ""

        timestampval = self.storekeyvalue[key][1]
        actualvalue = self.storekeyvalue[key][0]

        if timestamp < timestampval[0]:
            return ""

        """Apply here binary search """
        l = 0
        r = len(timestampval) - 1
        index = -1

        while l<=r:
            mid = (l+r) // 2
            if timestampval[mid] == timestamp:
                return actualvalue[mid]
            elif timestampval[mid] < timestamp:
                index = mid
                l = mid+1
            else:
                r = mid -1

        return actualvalue[index]

t = TimeMap()
t.set("ctondw", "ztpearaw", 1);  # store the key "foo" and value "bar" along with timestamp = 1.
# print(t.get("foo", 1));         # return "bar"
# print(t.get("foo", 3));         # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
t.set("vrobykydll", "hwliiq", 2); # store the key "foo" and value "bar2" along with timestamp = 4.
t.set("gszaw", "ztpearaw", 2); # store the key "foo" and value "bar2" along with timestamp = 4.
t.set("ctondw", "gszaw", 2); # store the key "foo" and value "bar2" along with timestamp = 4.
print(t.get("gszaw", 5));         # return "bar2"
# print(t.get("foo", 5));   




# ["TimeMap","set","set","set","set","get","get","get","get","get","get","set","get","get","get","set","set","set","set","get","get"]
# [[],["ctondw","ztpearaw",1],["vrobykydll","hwliiq",2],["gszaw","ztpearaw",3],["ctondw","gszaw",4],["gszaw",5],["ctondw",6],["ctondw",7],["gszaw",8],["vrobykydll",9],["ctondw",10],["vrobykydll","kcvcjzzwx",11],["vrobykydll",12],["ctondw",13],["vrobykydll",14],["ztpearaw","zondoubtib",15],["kcvcjzzwx","hwliiq",16],["wtgbfvg","vrobykydll",17],["hwliiq","gzsiivks",18],["kcvcjzzwx",19],["ztpearaw",20]]