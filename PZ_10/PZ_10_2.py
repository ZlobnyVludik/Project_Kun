# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.

count_letters = 0

f1 = open("text18-8.txt", "r", encoding="utf-16")

for line in f1:
    print(line)
    for symbol in line:
        if symbol.isalpha():
            count_letters += 1

f1.close()

print("\nКоличество букв:", count_letters)

# Создание нового файла без буквы "с"

f1 = open("text18-8.txt", "r", encoding="utf-16")
text = f1.read()
f1.close()

text = text.replace("с", "").replace("С", "")

f2 = open("text18-8_new.txt", "w", encoding="utf-16")
f2.write(text)
f2.close()
