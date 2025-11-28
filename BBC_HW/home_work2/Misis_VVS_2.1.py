from string import *

def lvl1() -> str:
    print("Введите текст")
    a : str = input()

    print("Выберите регистр -> H/L")

    reg : str = input()

    ans : str = a
    if (reg == "H"):
        print(ans.upper())
    elif (reg == "L"):
        print("Хотите сделать первую букву заглавной? Да/Нет")
        cap: str = input()
        if cap == "Да":
            print(ans.lower().capitalize())
        else:
            print(ans.lower())
    else:
        print("Wrong")

def lvl2():
    print("Введите текст")
    s: str = input()

    print("Выберите метод -> replace/count/оба")
    met : str = input()

    def replace(s):
        print("Введите слово, которое хотите заменить")
        word: str = input()

        print("Введите слово для замены")
        wordres: str = input()

        print("Вы хотите заменить первое входящее? Да/Нет")
        ans: str = input()

        if (s.find(word)):
            if ans == "Да":
                s = s.replace(word, wordres, 1)
            else:
                s = s.replace(word, wordres)
            print(s)
        else:
            print(f"Нет {word} в слове")

    def count(s):
        print("Выберите букву для подсчета")
        let: str = input()
        print(s.count(let))

    if met == "replace":
        replace(s)
    elif met == "count":
        count(s)
    elif met == "оба":
        replace(s)
        count(s)


def lvl3():
    print("Введите текст")
    s: str = input()

    print("Введите элемент для split")
    el: str = input()

    s = s.split(el)

    ans : str = " ".join(s)
    print(ans)

def lvl4():
    def idig(s):
        if s.isdigit():
            print("Строка из цифр")
        else:
            print("Строка не только из цифр")

    def ialp(s):
        if s.isalpha():
            print("Строка из букв")
        else:
            print("Строка не только из букв")

    def strp(s):
        print("Введите элемент для удаления")
        el : str = input()

        print("R/L/везде")
        st : str = input()

        if st == "везде":
            print(s.strip(el))
        if st == "R":
            print(s.rstrip(el))
        if st == "L":
            print(s.lstrip(el))

    print("Введите текст")
    s: str = input()

    print("Выберите функцию isdigit/isalpha/strip")
    f: str = input()

    if f == "isdigit":
        idig(s)
    elif f == "isalpha":
        ialp(s)
    elif f == "strip":
        strp(s)

def lvl5():
    print("Введите строку")
    s : str = "  Python;is;Awesome;  "
    print(s)
    s = s.replace(" ", "")
    s = s.split(";")
    s = " ".join(s)
    s = s.lower().capitalize()
    print(s)


print("Выберите уровень от 1 до 5:")
lvl : int = int(input())

if lvl == 1:
    lvl1()
elif lvl == 2:
    lvl2()
elif lvl == 3:
    lvl3()
elif lvl == 4:
    lvl4()
elif lvl == 5:
    lvl5()
else:
    print("Неправильно выбран уровень")

