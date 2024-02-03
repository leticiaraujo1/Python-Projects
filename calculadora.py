print('---Bem vindo a Calculadora Python---')

while True:
    print('---O que você deseja?---')
    print('[1] Calcular')
    print('[2] Sair')
    opcao = input('')

    if opcao == '1':
        print('Qual operação você deseja fazer?')
        print('[1] Adição')
        print('[2] Subtração')
        print('[3] Multiplicação')
        print('[4] Divisão')
        operacao = input('')
        n1 = float(input('Digite o primeiro número:'))
        n2 = float(input('Digite o segundo número:'))
        
        match operacao:
            case "1":
                res = n1 + n2
                print('O resultado da soma entre', n1, 'e', n2, 'é', res)
            case "2":
                res = n1 - n2
                print('O resultado da subtração entre', n1, ' e ', n2, 'é ', res)
            case "3":
                res = n1 * n2
                print('O resultado da multiplicação entre', n1, ' e ', n2, 'é ', res)
            case "4":
                if n2 == 0:
                    print('A divisão não pode ser por zero, digite outro número!')
                    n2 = float(input('Digite o segundo número:'))
                res = n1 / n2
                print('O resultado da divisão entre', n1, ' e ', n2, 'é ', res)
            case _:
                print('A operação foi invalida, tente novamente!')
            
    elif opcao == '2':
        print('Obrigada por utilizar a Calculadora Python!')
        break

