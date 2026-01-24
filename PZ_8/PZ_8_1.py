#Извлеките ключи ["name", "salary"] из sample_dict.

#Выданый нам словарь
sample_dict = {
 "name": "Kelly",
 "age":25,
 "salary": 8000,
 "city": "New york"
}

#Вывод
result = {key: sample_dict[key] for key in ["name", "salary"]}
print(result)
