first = 0
second = 1
i = 0
length = int(input('Enter sequence lenght: '))
my_list = []

while i < length:
    my_list.append(first)
    my_list.append(second)
    first = first + second
    second = first + second
    i += 1


print(*my_list, sep=', ')