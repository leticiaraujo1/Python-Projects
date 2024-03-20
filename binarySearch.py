print('---Busca Binária---')

def binarySearch(my_arr, key):
    start_index = 0
    end_index = len(my_arr) - 1
    
    while start_index <= end_index:
        middle_index = (start_index + end_index)//2
        
        if my_arr[middle_index] == key:
            return middle_index
        elif my_arr[middle_index] < key:
            start_index = middle_index + 1
        elif my_arr[middle_index] > key:
            end_index = middle_index - 1
    
    return -1

arr_num = [2,5,8,3,0,9]
my_key = 8

key_index = binarySearch(arr_num, my_key)

if key_index != -1:
    print(f'A chave {my_key} foi encontrada na posição {key_index}')
else:
    print(f'A chave {my_key} não foi encontrada')
