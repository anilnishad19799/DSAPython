class Solution:

    """
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack or (i==")" and stack[-1]!="(") or (i=="]" and stack[-1]!="[") or (i=="}" and stack[-1]!="{"):
                    return False
            
                stack.pop()
        
        return True

    """

    """ Better approach"""

    def isValid(self, s: str) -> bool:
        openparenthesis = ["(", "[", "{"]
        closingparenthesis = {"}":"{", ")":"(", "]":"["}
        stack = []
        for i in s:
            if i in openparenthesis:
                stack.append(i)
            else:
                if stack and stack[-1]==closingparenthesis[i]:
                    stack.pop()
                else:
                    return False
        
        return stack==[]


        
s = Solution()
str = "()"
output = s.isValid(str)
print(output)