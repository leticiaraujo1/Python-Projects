my_str = input('Digite a string a ser invertida: ')

def invert(str):
    new_str = ''

    for i in range(len(str)-1,-1,-1):
        new_str += str[i]
    
    return new_str
    
print(invert(my_str))