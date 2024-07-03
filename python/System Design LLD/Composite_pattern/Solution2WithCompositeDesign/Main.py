from Number import Number
from Expression import Expression
from Operation import Operation

def main():
    # 2 * (1 + 7)
    '''
                *
              /   \
            2      +
                  / \
                 1   7
    '''

    two = Number(2)
    one = Number(1)
    seven = Number(7)
    
    add_expression = Expression(one, seven, Operation.ADD)
    parent_expression = Expression(two, add_expression, Operation.MULTIPLY)
    
    print(parent_expression.evaluate())

if __name__ == "__main__":
    main()
