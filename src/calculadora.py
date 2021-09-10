import pymongo
mongo = pymongo.MongoClient('mongodb://localhost:27017/')

def calculate():
    operation = input('''
Por favor escolha a operação desejada:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Por favor insira o primeiro numero: '))
    number_2 = int(input('Por favor insira o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não selecionou uma operação valida, abra o programa novamente.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Quer fazer outra operação?
Pressione Y para SIM ou N para NÂO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até a proxima.')
    else:
        again()

calculate()