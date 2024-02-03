import random

print('Bem vindo a Batalha Pokemon!')
print('[1] Charmander')
print('[2] Squirtle')
print('[3] Bulbasaur')
pokemon = int(input('Escolha seu pokemon: '))

vida = 0
danoAtaque = 0
defesa = False

vidaInimigo = 35
danoInimigo = 3
defesaInimigo = False

def chosePokemon(pokemo):
    global vida
    global danoAtaque
    
    if pokemo==1:
        vida += 30
        danoAtaque += 5
    elif pokemo==2:
        vida += 25
        danoAtaque += 7
    elif pokemo==3:
        vida += 35
        danoAtaque += 3
    else:
        aleatorio = random.randint(1,3)
        chosePokemon(aleatorio)

chosePokemon(pokemon)
print('Sua vida é ' + str(vida) + ' e seu dano de ataque é ' + str(danoAtaque))

def batalha():
    global vida
    global danoAtaque
    global vidaInimigo
    global defesa
    global defesaInimigo
    
    print('\nAções:')
    print('[1] Atacar')
    print('[2] Defender')
    print('Sua vida atual é ' + str(vida))
    
    acao = int(input('Escolha sua próxima ação: '))
    
    defesa = False
    
    if vida!=0 and vidaInimigo!=0:
        if acao==1:
            if defesaInimigo==False:
                vidaInimigo -= danoAtaque
                print(f'Você atacou. A vida atual do inimigo é {vidaInimigo}')
                batalhaInimigo()
            else: 
                print('O inimigo defendeu!')
                batalhaInimigo()
        elif acao==2:
            defesa = True
            batalhaInimigo()
        else:
            print('Por favor escolha uma opção válida.')
            batalha()
    elif vida==0:
        print('FIM DE BATALHA! Você perdeu.')
    elif vidaInimigo==0:
        print('FIM DE BATALHA! Você venceu.')

def batalhaInimigo():
    global vida
    global vidaInimigo
    global danoInimigo
    global defesa
    global defesaInimigo
    
    defesaInimigo = False
    
    acaoInimigo = random.randint(1,2)
    
    if vida!=0 and vidaInimigo!=0:
        if acaoInimigo==1:
            if defesa==False:
                vida -= danoInimigo
                batalha()
            else:
                print('Você defendeu o ataque!')
                batalha()
        elif acaoInimigo==2:
            defesaInimigo = True
            batalha()
    elif vida==0:
        print('FIM DE BATALHA! Você perdeu.')
    elif vidaInimigo==0:
        print('FIM DE BATALHA! Você venceu.')

    
batalha()