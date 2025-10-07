import math as m

class Calculation:

    def __init__(self, num_1 : int, num_2 : int, oper, operation, corner : int):
        self.num_1 = num_1
        self.num_2 = num_2
        self.oper = oper
        self.operation = operation
        self.corner = corner

    def calculate_ingener(self) -> int:
        if operation == "cos":
            return m.cos(corner)
        elif operation == "sin":
            return m.sin(corner)

    def calculate_main(self) -> int:
        if oper == "+":
            return num_1 + num_2
        if oper == "-":
            return num_1 - num_2
        if oper == "*":
            return num_1 * num_2
        if oper == "/" or oper == ":":
            return num_1 // num_2


print("Выберите тип Main/Ingener")
type = input()
if type == "Main":
    print("Введите 2 числа:")
    num_1, num_2 = int(input()), int(input())
    print("Введите операцию:")
    oper = input()
    answer = Calculation(num_1, num_2, oper, 0, 0)
    print(answer.calculate_main())
elif type == "Ingener":
    print("Введите операцию")
    operation = input()
    print("Введите угол")
    corner = int(input())
    answer = Calculation(0, 0, 0, operation, corner)
    print(answer.calculate_ingener())
