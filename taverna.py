from armadura_3 import *
char = Personagem('nome','raça','atributos','classe','pv','CA')
from classes import *
__name__ = "__main__"

def aventura():
    print('''
                                 ________________________
                                |                        |
                                |      BEM-VINDO!!!      |
                                |________________________|

          ''')

    print('''Olá aventureiro(a), seja bem-vindo! É uma honra tê-lo conosco aqui na taverna.
Então quer dizer que você quer viver uma aventura é? ...Bom, veremos do que você é capaz hehehe''')

    print('''
Com qual raça você quer jogar?
( Anão / Draconato / Elfo / Gnomo / Halfling / Humano / Meio elfo / Meio orc / Tiefling )
(Para sair, digite exit)''')

    raça = input().upper()

    if raça in ['ANÃO','ANAO']: 
        char.raça = 'Anão'
        final(anao(),char.raça)

    elif raça == 'ELFO':
        char.raça = 'Elfo'
        final(elfo(),char.raça)

    elif raça == 'HUMANO':
        char.raça = 'Humano'
        final(humano(),char.raça)

    elif raça == 'GNOMO':
        char.raça = 'Gnomo'
        final(gnomo(),char.raça)

    elif raça in ['MEIO ELFO','MEIOELFO','MEIO-ELFO']:
        char.raça = 'Meio elfo'
        final(melf(),char.raça)

    elif raça in ['HALFLING','HALF LING','HALF-LING']:
        char.raça = 'Halfling'
        final(hobbit(),char.raça)

    elif raça == 'DRACONATO':
        char.raça = 'Draconato'
        final(drake(),char.raça)

    elif raça in ['TIEFLING','TIEF LING','TIEF-LING']:
        char.raça = 'Tiefling'
        final(tief(),char.raça)

    elif raça in ['MEIO ORC','MEIO-ORC','MEIOORC','MEIORC']:
        char.raça = 'Meio orc'
        final(morc(),char.raça)
    
    elif raça == "exit":
        return None

    else:
        print("Essa raça ainda não foi adicionada! Calma que logo logo ela tá por aqui, beleza?")
        aventura()

if __name__=="__main__":
    aventura()

