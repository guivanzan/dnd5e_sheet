from races import anao

class playableCharacter:
    def __init__(self, nome = 'nome', nivel = '1', vida = 12):
        
        self.nome = nome
        self.nivel = nivel
        self.vida = vida
        self.classe = ''
        self.atributos = {'for': 10, 'des': 10, 'con': 10,
                          'int': 10, 'sab': 10,'car': 10}
        
        # fazer round down
        self.modificadores = {'for': (self.atributos['for'] - 10)/2,
                              'des': (self.atributos['des'] - 10)/2,
                              'con': (self.atributos['con'] - 10)/2,
                              'int': (self.atributos['int'] - 10)/2,
                              'sab': (self.atributos['sab'] - 10)/2,
                              'car': (self.atributos['car'] - 10)/2,}

        self.pericias = {'acrobacia':self.modificadores['des'],
                         'arcanismo':self.modificadores['int'],
                         'atletismo':self.modificadores['for'],
                         'atuacao':self.modificadores['car'],
                         'enganacao':self.modificadores['car'],
                         'furtividade':self.modificadores['des'],
                         'historia':self.modificadores['int'],
                         'intimidacao':self.modificadores['car'],
                         'intuicao':self.modificadores['sab'],
                         'investigacao':self.modificadores['int'],
                         'adestrar':self.modificadores['sab'],
                         'medicina':self.modificadores['sab'],
                         'natureza':self.modificadores['int'],
                         'percepcao':self.modificadores['sab'],
                         'persuasao':self.modificadores['car'],
                         'prestidigitacao':self.modificadores['des'],
                         'religiao':self.modificadores['int'],
                         'sobrevivencia':self.modificadores['sab']}
        
        self.proficiencia = 2
        
        self.percepcaopassiva = 10 + self.modificadores['sab']

    def escolhaClasse(self, classe):
        self.classe = classe

