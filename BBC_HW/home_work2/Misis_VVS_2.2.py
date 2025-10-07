print("Введите текст")
s : str = input()

if (s.find("круто")):
    s = s.replace("круто", "замечательно", 1)
    print(s)
    print(s.count("о"))
else:
    print("Нет 'круто' в слове")
    print(s.count("о"))