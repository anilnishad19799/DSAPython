""" Not optmial Solutions"""

# class Solution:
#     def dailyTemperatures(self, temperatures):
#         n = len(temperatures)
#         output = []
#         for i in range(len(temperatures)):
#             j = i+1
#             print("*"*100)
#             while j < n and (temperatures[j] <= temperatures[i]) :
#                 j+=1

#             if j==n:
#                 j = i
#             output.append(j-i)
        
#         return output


                
# s = Solution()
# # temperatures = [73,74,75,71,69,72,76,73]
# # temperatures = [30,40,50,60]
# # temperatures = [30,60,90]
# temperatures = [89,62,70,58,47,47,46,76,100,70]
# out = s.dailyTemperatures(temperatures)
# print(out)


# temperatures = [89,62,70,58,47,47,46,76,100,70]
temperatures = [73,74,75,71,69,72,76,73]
stack = []
output = [0] * len(temperatures)

for i, t in enumerate(temperatures):
    while stack and stack[-1][0] < t:
        stackt, stackindex = stack.pop()
        output[stackindex] = i - stackindex
    
    stack.append([t,i])

print(output)
