print("Введите 2 числа:")
num_1, num_2 = int(input()), int(input())
print("Введите операцию:")
oper = input()

if oper == "+":
    print(f"Результат: {num_1 + num_2}")
elif oper == "-":
    print(f"Результат: {num_1 - num_2}")
elif oper == "*":
    print(f"Результат: {num_1 * num_2}")
elif oper == "/":
    print(f"Результат: {num_1 / num_2}")

