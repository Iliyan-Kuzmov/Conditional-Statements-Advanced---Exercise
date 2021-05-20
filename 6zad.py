N1 = int(input())
N2 = int(input())
operator = input()
if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = N1 + N2
    elif operator == "-":
        result = N1 - N2
    elif operator == "*":
        result = N1 * N2
    if result % 2 == 0:
        chetno_nechetno = "even"
    else:
        chetno_nechetno = "odd"
    print(f"{N1} {operator} {N2} = {result} - {chetno_nechetno}")
elif operator == "/" or operator == "%":
    if N2 == 0:
        print(f"Cannot divide {N1} by zero")
    elif N2 != 0:
        if operator == "/":
            result = N1 / N2
            print(f"{N1} / {N2} = {result:.2f}")
        elif operator == "%":
            result = N1 % N2
            print(f"{N1} % {N2} = {result}")
