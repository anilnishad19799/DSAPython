class Solution:
    def isValid(self, s: str) -> bool:
        
        openparnthesis = ["(", "[", "{"]
        closeparnthesis = [")", "]", "}"]

        bracketcount = 0
        squarebrackertcount = 0
        curlybracketcount = 0

        for i in s:
            if i in openparnthesis:
                # count+=1
                if i == "(":
                    bracketcount+=1
                elif i == "[":
                    squarebrackertcount+=1
                elif i == "{":
                    curlybracketcount+=1

            elif i in closeparnthesis:
                if i == ")":
                    bracketcount-=1
                elif i == "]":
                    squarebrackertcount-=1
                elif i == "}":
                    curlybracketcount-=1
            else:
                pass

        if bracketcount == 0 and squarebrackertcount ==0 and curlybracketcount == 0:
            return True
        else:
            return False

        