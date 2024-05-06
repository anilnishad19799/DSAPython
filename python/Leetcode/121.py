""" Sliding windows protocol """

# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]

l = 0
r = 1
n = len(prices)
maxprofit = 0
while r < n:

    maxprofit = max(maxprofit, prices[r] - prices[l])
    if prices[r] < prices[l]:
        l = r
    
    r+=1

print(maxprofit)