first = int(input('Enter the first namber: '))
second = int(input('Enter the second namber: '))
third = int(input('Enter the third namber: '))
if first == second and third == first and second==third:
    print('3')
elif first != second and first!=third and second!= third :
    print('0')
elif first == second:
    print('2')
elif first == third:
    print('2')
elif second == third:
    print('2')

