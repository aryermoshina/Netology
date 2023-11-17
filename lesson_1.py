# Задание 1

a = int(input("Введи год"))
if a % 4 == 0
    print('Високосный год')
else:
    print('Обычный год')
    
# Задание 2

str_a = list(input('Введи 6-ти значный номер билета'))
nums_a = list(map(int, str_a))
if sum(nums_a[0:3]) == sum(nums_a[3:6]):
  print('Счастливый билет')
else:
    print('Несчастливый билет')