def operation_fun(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a/b
    elif op == "*":
        return a*b
    elif op == "%":
        return a%b
    else:
        return "Invalid operator"