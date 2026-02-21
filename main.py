from utils import operation_fun

print("""
        ######################
           Simple Calculator
        ######################
        """
)

num1 = float(input("enter num 1: "))
num2 = float(input("enter num 2: "))

op   = input("enter the operation: ")

result = operation_fun(num1, num2, op)

print("The answer is: ", result)
