"""
    Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
    Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
    В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1
"""
"""
n = int(input('Введите количество элементов списка А: '))
a  = input("Введите элементы массива через пробел от [1..N]: ").split()
x = int(input("Введите число [x], которое необходимо найти в списке: "))
count = 0 
list_numbers = list(map(int,a))
if len(list_numbers) != n:
  print("Введенные элементы не соответствуют заявленному количеству!")
else:
   for i in range(n):
        if list_numbers[i] == x:
            count += 1
print(count)
"""
"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5    
"""
"""
n = int(input('Введите количество элементов списка А: '))
a  = input("Введите элементы массива через пробел от [1..N]: ").split()
x = int(input("Введите число [x], которое необходимо найти в списке: "))
count = 0 
list_numbers = list(map(int,a))
if len(list_numbers) != n or n == 0:
  print("Введенные элементы не соответствуют заявленному количеству!")
else:
    min = x - list_numbers[0]
    index = 0 
    for i in range(1, n):
        count = x - list_numbers[i]
        if count < min:
            min = count
            index = i
print(list_numbers[index])
"""
"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

ноутбук
    12
"""
"""
eng = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
rus = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
N = int(input("Введите число1, если играем на английском , либо 0, если на русском: "))
word = input('Введите слово: ').upper()
if N == 1:
	print("Сумма очков слова", sum([k for i in word for k, v in eng.items() if i in v]))
elif N == 0:
	print("Сумма очков слова", sum([k for i in word for k, v in rus.items() if i in v]))
else:
    print("Вы играете не по правилам игры! ")
"""
    
    



