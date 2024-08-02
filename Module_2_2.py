first = int(input('Enter the first namber: '))
second = int(input('Enter the second namber: '))
third = int(input('Enter the third namber: '))
if first == second and third == first and second == third:
    print('3')
elif first != second and first != third and second != third:
    print('0')
elif first == second or first == third or second == third:
    print('2')

