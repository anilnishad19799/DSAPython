""" Contain with most water """

# height = [1,8,6,2,5,4,8,3,7]
height = [2]

def getMaxArea(height):
    l = 0
    r = len(height)-1
    maxarea = 0
    
    while l<r:
        area = min(height[l], height[r]) * (r-l)
        maxarea = max(maxarea, area)

        if height[l] < height[r]:
            l+=1
        else:
            r-=1

    return maxarea

maxarea = getMaxArea(height)
print(maxarea) 
