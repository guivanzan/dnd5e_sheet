from random import randint
from pdf import escriba
from math import floor
from stringcolor import cs
from classes import *


class Personagem:
    def __init__(self,nome,raça,atributos,classe,pv,CA):
        self.nome = nome
        self.raça = raça
        self.atributos = atributos
        self.classe = classe
        self.pv = pv
        self.CA = CA

char = Personagem('nome','raça','atributos','classe','pv','CA')

def dados():
    ATR = []
    dados = []
    while len(ATR) < 6:
        dados = [randint(1,6),randint(1,6),randint(1,6),randint(1,6)]
        list.sort(dados)
        list.reverse(dados)
        list.pop(dados)
        ATR.append(dados[0]+dados[1]+dados[2])
    return ATR


def dadosDeAtributo():
    ATR = dados()
    while ATR[0]+ATR[1]+ATR[2]+ATR[3]+ATR[4]+ATR[5] > 80 or ATR[0]+ATR[1]+ATR[2]+ATR[3]+ATR[4]+ATR[5] < 70:
        ATR = dados()
    return ATR


def escolha():
    print('''
Vamos lá, você quer usar os valores prontos (1) ou quer rolar seus valores de atributo (2)?''')
    modo = input()
    if modo == '1':
        ATRT = []
        ATR = [15,14,13,12,10,8]
        print(ATR)
        print(f'''Agora vamos alocar cada um desses dados em um atributo: {cs('Força','red')}, {cs('Destreza','yellow')}, 
{cs('Constituição','green')}, {cs('Inteligência','blue')}, {cs('Sabedoria','purple')} e {cs('Carisma','orange')}.
Nós seguiremos essa ordem! Sendo assim, escolha um valor para {cs('Força','red')}:''')
        forc = input()
        ATRT.append(int(forc))
        ATR.remove(int(forc))
        print(f'''
Ok, agora escolha um valor para {cs('Destreza','yellow')}''')
        print(ATR)
        des = input()
        ATRT.append(int(des))
        ATR.remove(int(des))
        print(f'''
Agora um para {cs('Constituição','green')}''')
        print(ATR)
        con = input()
        ATRT.append(int(con))
        ATR.remove(int(con))
        print(f'''
Escolha um para sua {cs('Inteligência','blue')}''')
        print(ATR)
        inte = input()
        ATRT.append(int(inte))
        ATR.remove(int(inte))
        print(f'''
Falta pouco! Qual valor para {cs('Sabedoria','purple')} você quer?''')
        print(ATR)
        sab = input()
        ATRT.append(int(sab))
        ATR.remove(int(sab))
        print('O último valor que sobrou, {}, será seu valor de {}!'.format(ATR[0],cs('Carisma','orange')))
        ATRT.append(ATR[0])
        
        return ATRT

    elif modo == '2':
        ATRT = []
        ATR = dadosDeAtributo()
        print(ATR)
        reroll = input('''Você gostou dos dados?
(S/N)
''').upper()
        while reroll == 'N':
            ATR = dadosDeAtributo()
            print(ATR)
            reroll = input('''Você gostou dos dados?
(S/N)
''').upper()
            if reroll == 'S':
                break
             
                
        print('''
Beleza, esses são seus dados:''')
        print(ATR)
        print(f'''Agora vamos alocar cada um desses dados em um atributo: {cs('Força','red')}, {cs('Destreza','yellow')}, 
{cs('Constituição','green')}, {cs('Inteligência','blue')}, {cs('Sabedoria','purple')} e {cs('Carisma','orange')}.
Nós seguiremos essa ordem! Sendo assim, escolha um valor para {cs('Força','red')}:''')
        forc = input()
        ATRT.append(int(forc))
        ATR.remove(int(forc))
        print(f'''
Ok, agora escolha um valor para {cs('Destreza','yellow')}''')
        print(ATR)
        des = input()
        ATRT.append(int(des))
        ATR.remove(int(des))
        print(f'''
Agora um para {cs('Constituição','green')}''')
        print(ATR)
        con = input()
        ATRT.append(int(con))
        ATR.remove(int(con))
        print(f'''
Escolha um para sua {cs('Inteligência','blue')}''')
        print(ATR)
        inte = input()
        ATRT.append(int(inte))
        ATR.remove(int(inte))
        print(f'''
Falta pouco! Qual valor para {cs('Sabedoria','purple')} você quer?''')
        print(ATR)
        sab = input()
        ATRT.append(int(sab))
        ATR.remove(int(sab))
        print('O último valor que sobrou, {}, será seu valor de {}!'.format(ATR[0],cs('Carisma','orange')))
        ATRT.append(ATR[0])

        return ATRT

def modATR(x):
    y = floor((x-10)/2)
    return y

def final(ATRT,raça):
    nome = input('Qual será o nome do seu aventureiro(a)? ')
    char.nome = nome[0].upper()+nome[1:]

    char.atributos = ATRT
    MODATRT = []

    for n in range(0,6):
        MODATRT.append(modATR(char.atributos[n]))

    classe = input(f'''

Agora você precisa decidir uma classe! Escolha uma da lista abaixo:
( Bárbaro / Bardo / Bruxo / Clérigo / Druida / Feiticeiro
Guerreiro / Ladino / Mago /Monge / Paladino / Patrulheiro)

''').upper()
    fim = escolhaPericia(classe)

    print('Ok, {}, seus valores de atributo são:'.format(char.nome[0].upper()+char.nome[1:]))
    print('{} de {}'.format(char.atributos[0],cs('Força','red')))
    print('{} de {}'.format(char.atributos[1],cs('Destreza','yellow')))
    print('{} de {}'.format(char.atributos[2],cs('Constituição','green')))
    print('{} de {}'.format(char.atributos[3],cs('Inteligência','blue')))
    print('{} de {}'.format(char.atributos[4],cs('Sabedoria','purple')))
    print('{} de {}'.format(char.atributos[5],cs('Carisma','orange')))
    escriba(char.nome,char.raça,char.atributos,MODATRT,fim[0],fim[1],fim[3],fim[4])

def anao():
    char.raça = 'Anão'
    ATRT = escolha()
    ATRT[2]=ATRT[2]+2   
    print('Você é um anão das montanhas (1) ou das colinas (2)?')
    print('(1/2)')
    subraça = input()

    if subraça == '1':
        ATRT[0]=ATRT[0]+2
        return ATRT

    elif subraça == '2':
        ATRT[4]=ATRT[4]+1
        return ATRT


def elfo():
    char.raça = 'Elfo'
    ATRT = escolha()
    ATRT[1]=ATRT[1]+2
    subraça = input('''você é um elfo(a) alto(a) (1), das florestas (2) ou negro(a) (3)?
(1/2/3)''')
    if subraça == '1':
        ATRT[3]=ATRT[3]+1
        return ATRT

    elif subraça == '2':
        ATRT[4]=ATRT[4]+1
        return ATRT

    elif subraça == '3':
        ATRT[5]=ATRT[5]+1
        return ATRT


def humano():
    char.raça = 'Humano'
    subraça = input(('''você quer usar as regras de humano variante?
(S/N)'''))
    subraça = subraça.upper()
    if subraça == 'N':
        #+1 em todos os atr
        ATRT = escolha()
        for n in range(0,6):
            ATRT[n] = ATRT[n]+1
        return ATRT

    elif subraça == 'S':
        ATRT = escolha()
        ATRHV = ['FOR','DES','CON','INT','SAB','CAR']
        print(ATRT)
        print(' ')
        print(ATRHV)
        decisao = input('''Escolha dois atributos para aprimorar:
(exemplo: For e Car)

''')
        AT1 = decisao[0:3].upper()
        AT2 = decisao[6:9].upper()
        if AT1 == AT2:
            return None
        else:
            while AT1 in ATRHV:
                ATRT[ATRHV.index(AT1)] = ATRT[ATRHV.index(AT1)]+1
                break
            while AT2 in ATRHV:
                ATRT[ATRHV.index(AT2)] = ATRT[ATRHV.index(AT2)]+1
                break
            return ATRT

def melf():
    char.raça = 'Meio Elfo'
    ATRT = escolha()
    ATRT[5] = ATRT[5]+2
    ATRME = ['FOR','DES','CON','INT','SAB']
    print(ATRT)
    print('')
    print(ATRME)
    decisao = input('''Escolha dois atributos para aprimorar, lembrando que não pode ser carisma!
(exemplo: For e Sab)

''')          
    AT1 = decisao[0:3].upper()
    AT2 = decisao[6:9].upper()
    if AT1 == AT2:
        return None
    elif 'CAR' == AT1 or 'CAR' == AT2:
        return None
    else:
        while AT1 in ATRME:
            ATRT[ATRME.index(AT1)] = ATRT[ATRME.index(AT1)]+1
            break
        while AT2 in ATRME:
            ATRT[ATRME.index(AT2)] = ATRT[ATRME.index(AT2)]+1
            break
        return ATRT
    
def gnomo():
    char.raça = 'Gnomo'
    ATRT = escolha()
    ATRT.insert(3,ATRT.pop(3)+2)
    print('''Você é um Gnomo da floresta (1) ou das rochas (2)?
(1/2)''')
    subraça=input()
    if subraça == '1':
        ATRT[1]=ATRT[1]+1
        return ATRT
    elif subraça == '2':
        ATRT[2]=ATRT[2]+1
        return ATRT

def hobbit():
    char.raça = 'Halfling'
    ATRT = escolha()
    ATRT[1]=ATRT[1]+2
    print('''Você é um halfling robusto (1) ou dos pés ligeiros (2)?
(1/2)''')
    subraça=input()
    if subraça == '1':
       ATRT[2]=ATRT[2]+1
       return ATRT

    elif subraça == '2':
       ATRT[5]=ATRT[5]+1
       return ATRT

def drake():
    char.raça = 'Draconato'
    ATRT = escolha()
    ATRT[0]=ATRT[0]+2
    ATRT[5]=ATRT[5]+1
    return ATRT

def tief():
    char.raça = 'Tiefling'
    ATRT = escolha()
    ATRT[3]=ATRT[3]+1
    ATRT[5]=ATRT[5]+2
    return ATRT

def morc():
    char.raça = 'Meio Orc'
    ATRT = escolha()
    ATRT[0]=ATRT[0]+2
    ATRT[2]=ATRT[2]+1
    return ATRT


