# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["3","-4","+"]

operators = ["+", "-", "*", "/"]

operandstack = []

for i in tokens:
    operandstack = []
    for i in tokens:
        if i not in "*/+-":
            operandstack.append(int(i))
        else:
            firstval = operandstack.pop()
            secondval = operandstack.pop()

            if i == "*":
                out = secondval * firstval
            elif i == "/":
                out = secondval / firstval
            elif i == "+":
                out = secondval + firstval
            elif i == "-":
                out = secondval - firstval
            else:
                pass
            operandstack.append(int(out))


print(operandstack)
print(operandstack[-1])

         