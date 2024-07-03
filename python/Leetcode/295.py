import heapq

class MedianFinder:

    """
    solution using sorting method
    def __init__(self):
        self.allvalue = []

    def addNum(self, num: int) -> None:
        self.allvalue.append(num)        

    def findMedian(self) -> float:
        totallen = len(self.allvalue)
        self.allvalue = sorted(self.allvalue)
        if totallen%2==1:
            return float(self.allvalue[totallen//2])
        else:
            firstval = self.allvalue[(totallen//2)-1]
            secondval = self.allvalue[(totallen//2)]
            return float((firstval+secondval)/2)
    """
        
    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if len(self.h1) == len(self.h2):
            heapq.heappush(self.h2, -heapq.heappushpop(self.h1, -num))
        else:
            heapq.heappush(self.h1, -heapq.heappushpop(self.h2, num))

    def findMedian(self) -> float:
        return float(self.h2[0]) if (len(self.h1) + len(self.h2)) & 1 else (-self.h1[0] + self.h2[0]) / 2
            

medianFinder = MedianFinder();
medianFinder.addNum(1);   
medianFinder.addNum(2);   
out = medianFinder.findMedian();
print(out) 
medianFinder.addNum(3);    
out = medianFinder.findMedian();
print(out) 