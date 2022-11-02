def calc():
    try:
        x=int(input("x:"))
        y=int(input("y:"))
        operand=input("Enter the options among(+,-,*,/,**) :")
        # if operand not in ['+','-','*','/','**']:
        #     raise Exception('Invalid operand. Please choose one among(+,-,*,/,**)')
        # else:
        #     print('Valid operation')
        if operand == '*':
            return x*y
        elif operand=='+':
            return x+y
        elif operand=='-':
            return x-y
        elif operand=='/':
            return x/y
        elif operand=='**':
            return x**y
        else:
            raise Exception('Invalid operand. Please choose one among(+,-,*,/,**)')
    except Exception as e:
        return e

print(calc())