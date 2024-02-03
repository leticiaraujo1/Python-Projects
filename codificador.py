print('---Bem vindo ao Codificador Python---')

def caesar():
    shift = int(input('Diga o número de vezes que o texto será deslocado: '))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newText = ''
    
    for char in text:
        if char == ' ':
            newText += char
        else:
            index = int(alphabet.find(char))
            newIndex = (index + shift) % 26
            newText += alphabet[newIndex]
    
    print('Texto codificado:', newText)

def vigenere():
    customKey = input('Diga qual chave será utilizada: ')
    keyIndex = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newText = ''

    for char in text.lower():
        if char == ' ':
            newText += char
        else:
            keyChar = customKey[keyIndex % len(customKey)]
            keyIndex += 1
            offset = alphabet.index(keyChar)
            index = alphabet.find(char)
            newIndex = (index + offset) % len(alphabet)
            newText += alphabet[newIndex]
    
    print('Texto codificado:', newText)


while True:
    print('---O que você deseja?---')
    print('[1] Codificar')
    print('[2] Sair')
    opcao = input('')
    
    if opcao == '1':
        print('Qual codificação você deseja utilizar?')
        print('[1] Cifra de cesar')
        print('[2] Cifra de Vigenere')
        cod = input('')
        text = input('Digite o texto a ser codificado: ').lower()
        
        if cod == '1':
            caesar()
        elif cod == '2':
            vigenere()
        
        else:
            print('Codificação invalida, tente novamente!')
            
    else:
        print('Obrigada por utilizar o Codificador Python')
        break

