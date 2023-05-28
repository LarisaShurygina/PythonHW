# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  



poem = input("Введите стих Винни: ")
letters = ["а", "о", "у", "ы", "э", "е", "ё", "и", "ю", "я"]
poem_low = poem.lower().split()


def find_letters(poem_low, letters):
    _list = []
    for i in poem_low:
        count = 0
        for j in i:
            if j in letters:
                count += 1
        _list.append(count)
    if len(set(_list)) == 1:
        print('Парам пам-пам')
    else:
        print('Пам парам')


print(poem_low)
find_letters(poem_low, letters)