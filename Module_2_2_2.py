first = int(input('Enter the first namber: '))
second = int(input('Enter the second namber: '))
third = int(input('Enter the third namber: '))
a = [first, second, third]
if a[0] == a[1] == a[2]:
    print(3)
elif a[0] == a[1] or a[0] == a[2] or a[1] == a[2]:
    print(2)
elif a[0] != a[1] != a[2]:
    print(0)
