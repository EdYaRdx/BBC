print("Введите текст")
s : str = input()

print("Введите элемент для split")
el : str = input()

s = s.split(el)

ans : str = " ".join(s)
print(ans)