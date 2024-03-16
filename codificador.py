print('---Codificador Python---')

def caesar():
    shift = int(input('Diga o número de vezes que o texto será deslocado: '))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''
    
    for char in text:
        if char == ' ':
            new_text += char
        else:
            index = int(alphabet.find(char))
            new_index = (index + shift) % 26
            new_text += alphabet[new_index]
    
    print('Texto codificado:', new_text)

def vigenere():
    custom_key = input('Diga qual chave será utilizada: ')
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''

    for char in text.lower():
        if char == ' ':
            new_text += char
        else:
            key_char = custom_key[key_index % len(custom_key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            newIndex = (index + offset) % len(alphabet)
            new_text += alphabet[newIndex]
    
    print('Texto codificado:', new_text)


while True:
    print('O que você deseja? [1] Codificar [2] Sair')
    choice = input('')
    
    if choice == '1':
        print('Qual codificação você deseja utilizar? [1] Cifra de César [2] Cifra de Vigenere')
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

