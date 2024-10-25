# 1. Виведення print
print "Python 2: Hello, World!" 
# 2. Поділ цілих чисел
print "Python 2:", 7 / 2  
# 3. Функція input()
x = raw_input("Python 2: Введіть щось: ") 
y = input("Python 3: Введіть щось: ") 
print("Python 3: Ви ввели:", y)

# 4. xrange() і range()
for i in xrange(3):  # xrange існує лише в Python 2
    print "Python 2: число", i
for i in range(3):  # У Python 3 range поводиться як xrange
    print("Python 3: число", i)

# 5. Unicode за замовчуванням
# Python 2
print "Python 2:", type(u"текст")  # <type 'unicode'>
print "Python 2:", type("текст")  # <type 'str'>
# Python 3
print("Python 3:", type("текст"))  # <class 'str'>, всі строки за замовчуванням Unicode

# 6. Методи для ітераторів dict()
# Python 2
d = {"a": 1, "b": 2, "c": 3}
print "Python 2:", d.keys()  # Повертає список
# Python 3
print("Python 3:", list(d.keys()))  # Повертає ітератор, тому обгортаємо у list

# 7. Розподіл змінних
# Python 2
a, b, c = (1, 2, 3)
print "Python 2:", a, b, c
# Python 3
a, *b, c = (1, 2, 3, 4)  # Розширений розподіл
print("Python 3:", a, b, c)

# 8. Exception handling
# Python 2
try:
    1 / 0
except ZeroDivisionError, e:  # Без дужок навколо змінної
    print "Python 2: Exception =", e
# Python 3
try:
    1 / 0
except ZeroDivisionError as e:  # Потрібен оператор as
    print("Python 3: Exception =", e)

# 9. Порівняння типів
print "Python 2:", cmp(3, 4)  # cmp повертає -1, 0 або 1


# 10. Підтримка довгих цілих чисел
# Python 2
print ("Python 2:", long(5.0))
