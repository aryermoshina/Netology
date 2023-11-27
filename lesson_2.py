#Задание 1
word = 'test'
if len(word) % 2 == 0:
    print(word[int(len(word)/2-1)], word[int(len(word)/2)], sep='')
else:
    print(word[int(len(word)//2)])

word = 'testing'
if len(word) % 2 == 0:
    print(word[int(len(word)/2-1)], word[int(len(word)/2)], sep='')
else:
    print(word[int(len(word)//2)])

#Задание 2
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard'] 
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'] 
if len(boys) == len(girls):
    for i in range(len(boys)):
        print(sorted(boys)[i], 'и', sorted(girls)[i])
else:
    print('Внимание, кто-то может остаться без пары!')

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'] 
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha'] 
if len(boys) == len(girls):
    for i in range(len(boys)):
        print(sorted(boys)[i], 'и', sorted(girls)[i])
else:
    print('Внимание, кто-то может остаться без пары!')
