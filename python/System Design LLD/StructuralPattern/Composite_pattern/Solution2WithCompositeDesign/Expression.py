from ArithmeticExpression import ArithmeticExpression
from Operation import Operation

class Expression(ArithmeticExpression):
    
    def __init__(self, left_part, right_part, operation):
        self.left_expression = left_part
        self.right_expression = right_part
        self.operation = operation
    
    def evaluate(self):
        value = 0
        if self.operation == Operation.ADD:
            value = self.left_expression.evaluate() + self.right_expression.evaluate()
        elif self.operation == Operation.SUBTRACT:
            value = self.left_expression.evaluate() - self.right_expression.evaluate()
        elif self.operation == Operation.DIVIDE:
            value = self.left_expression.evaluate() / self.right_expression.evaluate()
        elif self.operation == Operation.MULTIPLY:
            value = self.left_expression.evaluate() * self.right_expression.evaluate()
        
        print(f"Expression value is: {value}")
        return value
