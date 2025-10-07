def plus(num_1 : int, num_2 : int) -> int:
    return num_1 + num_2

def minus(num_1 : int, num_2 : int) -> int:
    return num_1 - num_2

def mult(num_1 : int, num_2 : int) -> int:
    return num_1 * num_2

def share(num_1 : int, num_2 : int) -> float:
    return num_1 / num_2

print("Введите 2 числа:")
num_1, num_2 = int(input()), int(input())
print("Введите операцию:")
oper = input()

if oper == "+":
    print(plus(num_1, num_2))
elif oper == "-":
    print(minus(num_1, num_2))
elif oper == "*":
    print(mult(num_1, num_2))
elif oper == "/" or oper == ":":
    print(share(num_1, num_2))


