import pandas as pd
import numpy as nm

#-----1_задание-----


data = pd.read_csv("data/tested.csv")

# открытие
print(data)

# пропуски
missing = data.isna().sum()
print(missing)

# признаки и характер 

numeric = data.select_dtypes(include="number").columns
categoric = data.select_dtypes(include=["object", "category"]).columns

print("Числовые признаки")
print(numeric.tolist())

print("Категориальные признаки")
print(categoric.tolist())

# первые n строк

n = int(input("Введите номер строки\n"))

print(data.head(n))

# базовая статистика max min mean std

l = int(input("Введите номер столбца\n"))

stolb = data.iloc[:, l]
stolb_name = data.columns[l]
print(stolb.describe())

# кол-во столбцов и строк

print("Кол-во столбцов и строк")
print(data.shape)

# Сохранение файла

data.to_csv("output.csv", index=False)


#-----2_задание-----
