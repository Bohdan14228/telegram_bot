s = 0
d = 1

# while d != 0:
#     d = int(input('Введите целое число: '))
#     if d % 2 == 0:
#         continue
# если доходим до оператора continue то всё что стоит ниже него не срабатывает, а переходим к следуущей итерации while

# s += d
# print('s = ', str(s))

a = 0
i = 1

while i < 100:
    if i == 101:
        break
    a += 1 / i
    i += 1
else:
    print('сумма вычислена корректно')
# блок else отрабатывает только когда while не заканчиваеться по break
# print(a)

L = eval(input('Input list: '))
print(L)