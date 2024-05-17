class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        output = []
        for i in range(len(temperatures)):
            j = i
            print(i)
            print("*"*100)
            while j+1 < n and (temperatures[j] > temperatures[j+1]) :
                j+=1
            print(j,i)
            output.append(j-i+1)
        
        return output


                
s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
out = s.dailyTemperatures(temperatures)
print(out)