import os

print('---Calculadora Python---')

while True:
    print('O que você deseja? [1] Calcular [2] Sair')
    choice = input('')

    if choice == '1':
        print('Qual operação você deseja fazer? [1] Adição [2] Subtração [3] Multiplicação [4] Divisão')
        math_operation = int(input(''))
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        
        match math_operation:
            case 1:
                op = 'soma'
                res = n1 + n2
            case 2:
                op = 'subtração'
                res = n1 - n2
            case 3:
                op = 'multiplicação'
                res = n1 * n2
            case 4:
                if n2 == 0:
                    print('A divisão não pode ser por zero, digite outro número!')
                    n2 = float(input('Digite o segundo número:'))
                op = 'divisão'
                res = n1 / n2
            case _:
                print('A operação foi invalida, tente novamente!')
        
        if math_operation>=1 and math_operation<=4:
            print('O resultado da', op, 'entre', n1, 'e', n2, 'é', res)



    elif choice == '2':
        os.system('cls')
        print('Obrigada por utilizar a Calculadora Python!')
        break

