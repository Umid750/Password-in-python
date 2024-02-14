login = input('Enter your nickname: ')
password = int(input('Enter your password: '))

if login == 'Butterfly' and password == 1234:
    while True:
        print('Gongratulations!')
        name = input('Enter your name: ')
        number = int(input('Enter number: '))
        for i in range(number):
            print(name)
        if name == 'stop' and number == 1:
            break
elif login == 'Umbrella' and password == 1111:
    print('Gongratulations!')
    while True:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(num1 + num2)
        if num1 == 1 and num2 == 1:
            break
else:
    print('Error!!!')