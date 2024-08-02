first = int(input('Enter the first number: '))
second = int(input('Enter the second number: '))
third = int(input('Enter the third number: '))
if first == second and third == first and second == third:
    print('3')
elif first != second and first != third and second != third:
    print('0')
elif first == second and first != third or first == third and first !=second or second == third and second!=first:
    print('2')

