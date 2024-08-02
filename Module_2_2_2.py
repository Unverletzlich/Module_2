first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
third = int(input('Enter the third number: '))
a = [first, second, third]
if a[0] == a[1] == a[2]:
    print(3)
elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    print(2)
elif a[0] != a[1] != a[2]:
    print(0)
