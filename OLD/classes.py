from stringcolor import cs

def escolhaPericia(classe):
    r1 = 0
    r2 = 2
    if classe == 'BÁRBARO' or classe == 'BARBARO':
        perBarb = {'1':16,'2':8,'3':13,'4':18,'5':19,'6':23}
        per = input(f'''Escolha duas perícias para serem treinadas (exemplo: 1 e 3):

{cs('Adestrar animais (1)','purple')}, {cs('Atletismo (2)','red')}, {cs('Intimidação (3)','orange')},
{cs('Natureza (4)','blue')}, {cs('Percepção (5)','purple')} e {cs('Sobrevivência (6)','purple')}''')
        # fazer um split por caractere e ignorar caracteres que n sao numeros
        # utilizar try
        escolha1 = per[0]
        escolha2 = per[4]
        if escolha1 == escolha2:
            return None
        else:
            p1 = perBarb[escolha1]
            p2 = perBarb[escolha2]
            fim=[p1,p2,classe,r1,r2]
            return fim
            
def escolhaClasse(classe):
    
    if classe in ['BÁRBARO','BARBARO']:
        escolhaPericia(classe)