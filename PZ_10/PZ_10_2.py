# Из предложенного текстового файла (text18-8.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно удалив букву «с» из
# текста.

count_letters = 0

file1 = open("text18-8.txt", "r", encoding="utf-16")

for line in file1:
    print(line, end="")
    for symbol in line:
        if symbol.isalpha():
            count_letters += 1

file1.close()

print("\nКоличество букв:", count_letters)

# Создание нового файла без буквы "с"

file1 = open("text18-8.txt", "r", encoding="utf-16")
text = file1.read()
file1.close()

text = text.replace("с", "").replace("С", "")

file2 = open("text18-8_new.txt", "w", encoding="utf-16")
file2.write(text)
file2.close()
