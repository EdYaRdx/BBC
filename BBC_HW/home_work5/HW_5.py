import pandas as pd
import numpy as nm

#-----1_задание-----


data = pd.read_csv("../../data/tested.csv")

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
print(stolb_name)
print(stolb.describe())

# кол-во столбцов и строк

print("Кол-во столбцов и строк")
print(data.shape)

# пропуски Age
print("Пропуски Age")
missing_age = data["Age"].isna().sum()
print(missing_age)

print("Среднее по столбцу")
mean_age = data["Age"].mean()
print(mean_age)

data["Age"] = data["Age"].fillna(mean_age)

print("Пропусков в Age после заполнения:", data["Age"].isna().sum())

# Сохранение файла
data.to_csv("../../data/output.csv", index=False)


#-----2_задание-----
''' 
data = pd.read_csv("../../data/tested.csv")

# Процент выживших
print("Процент выживших")
survived_by_gender = data.groupby("Sex")["Survived"].mean() * 100
print(survived_by_gender)

print("Средний возраст")
age_by_gender = data.groupby("Sex")["Age"].mean()
print(age_by_gender)

print("Средний возраст среди выживших")
sur_age_by_gender =  data[data["Survived"] == 1].groupby("Sex")["Age"].mean()
unsur_age_by_gender =  data[data["Survived"] == 0].groupby("Sex")["Age"].mean()
print(sur_age_by_gender, unsur_age_by_gender)

print("Группировка по классу и полу и вычисления")
grouped = data.groupby(["Pclass", "Sex"])
print(grouped["Age"].mean())
print(grouped["Survived"].mean())
print(grouped["Fare"].mean())

print("Фильтрация")
filtered_1 = data[(data["Age"] > 30) & (data["Sex"] == "male") & (data["Pclass"] == 1)]
print(filtered_1)
print("Кол-во таких пассажиров:", filtered_1.shape[0])

filtered_2 = data[((data["Age"] < 30) | (data["Sex"] == "female")) & (data["Survived"] == 1)]
print(filtered_2)
print("Кол-во таких пассажиров:", filtered_2.shape[0])
'''
