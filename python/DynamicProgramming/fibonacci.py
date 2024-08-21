""" This program is to implement fibonacci serites in dynamic programming """

""" This is simple program implement in simple way"""
# def fibo(n):
#     if n <= 0:
#         return n
#     return fibo(n-2) + fibo(n-1)

# n = 1
# output = fibo(n)
# print(output)


""" This is program to be implemented in dynamic programming
    Here time complexity is 0(N) and space complexity 0(2N) of one recusrsion and other for dp array
"""

def fibo(n, dp):
    if n==0:
        return 0
    
    if n==1:
        return 1
    
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = fibo(n-1, dp) + fibo(n-2, dp)
    return dp[n]

n = 6
dp = [-1]*(n+1)  # Adjusted size of dp array to handle n
output = fibo(n, dp)
print(output)


""" Here convert memoization to tabulation (Bottom up) where Base case is to be required 
    Here Time complexity is 0(N) and space complexity 0(N)
"""

def fibo(n, dp):
    dp[0] = 0
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[-1])

n = 6
dp = [-1]*(n+1)  # Adjusted size of dp array to handle n
output = fibo(n, dp)


""" A more better optimal approach where space complexity reduce to 0(1) 
    using prev , prev2 and curr variable 
"""
    
def fibo(n):
    prev2 = 0
    prev = 1

    for i in range(2, n+1):
        curr = prev + prev2
        prev2 = prev
        prev = curr
    
    print(prev)

n = 6
output = fibo(n)