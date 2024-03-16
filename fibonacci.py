num = int(input('Digite um número: '))

def isFibonacci(n):
    list = [0,1]

    while list[-1] <= n:
        next_num = list[-1] + list[-2]
        list.append(next_num)

    if n in list:
        print(f'O número {n} pertence a sequência fibonacci')
    else:
        print(f'O número {n} não pertence a sequência fibonacci')

isFibonacci(num)