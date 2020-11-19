#Abrir tela inicial
#Clique em qualquer botão para começar

player = {'level':1, 'hp':25, 'maxhp':25, 'atk':10, 'defn':5, 'exp':0, 'proxlv':100}
ling = {'hp':10, 'atk':8, 'defn':6, 'exppt':20}
queen = {'hp':50, 'atk':18, 'defn':12, 'exppt':100}
coordenadas = [0,0]
ambudrone = 3
#Pontos de reparo: [0,7], [6,0]
#Ponto de resgate: [0,9]
#Ponto de evacuação: [10,7]

#Posicao_jogador = coordenadas


class movimento():
    def __init__ (self, coordenadas):
        import random
        self.coord = coordenadas
        self.spawn = spawn
    def direita(self):
        #Botão Direita
        self.coord[0] += 1
        coordenadas = self.coord
        self.spawn += random.randint(1,1,1,1,1,1,1,1,1,10)
        if self.spawn >= 10:
            self.spawn = 0
            #Abrir ling_battle
        else:
            pass
    def esquerda(self):
        #Botão Esquerda
        self.coord[0] -= 1
        coordenadas = self.coord
        self.spawn += random.randint(1,1,1,1,1,1,1,1,1,10)
        if self.spawn >= 10:
            self.spawn = 0
            #Abrir ling_battle
        else:
            pass
    def cima(self):
        #Botão Cima
        self.coord[1] += 1
        coordenadas = self.coord
        self.spawn += random.randint(1,1,1,1,1,1,1,1,1,10)
        if self.spawn >= 10:
            self.spawn = 0
            #Abrir ling_battle
        else:
            pass
    def baixo(self):
        #Botão Baixo
        self.coord[1] -= 1
        coordenadas = self.coord
        self.spawn += random.randint(1,1,1,1,1,1,1,1,1,10)
        if self.spawn >= 10:
            self.spawn = 0
            #Abrir ling_battle
        else:
            pass


        
class ling_battle(movimento):
    def __init__ (self, coordenadas, parametros_player = player, parametros_ling = ling):
        #Abrir batalha
        #'Você encontrou um Ling!'
        movimento.__init__(self, coordenadas)
        self.player = parametros_player
        self.ling = parametros_ling
        
    def attack (self):
        #Botão Attack
        dano = (self.player['atk']-self.ling['defn'])
        self.ling['hp'] -= dano
        #'Ling recebeu x de dano!'
        if self.ling['hp'] <= 0:
            #'Ling foi derrotado!'
            self.player['exp'] += self.ling['exppt']
            if self.player['exp'] >= self.player['proxlv']:
                #'Você passou de nível!'
                self.player['level'] += 1
                self.player['maxhp'] += 5
                self.player['hp'] = self.player['maxhp']
                self.player['atk'] += 3
                self.player['defn'] += 2
                self.player['exp'] = 0
                self.player['proxlv'] += 50
            else:
                pass
            player = self.player
            #Fim da batalha
        else:
            #'Ling te atacou! Você recebeu x de dano!'            
            self.player['hp'] -= max(1, (self.ling['atk'] - self.player['defn'])
            if self.player['hp'] <= 0:
                #Fim de jogo
            else:
                #Retorna ao inicio da batalha
                pass
    
    def item(self):
        #Botão Item
        if ambudrone > 0:
            ambudrone -= 1
            self.player['hp'] = self.player['maxhp']
            #Retorna ao inicio da batalha
        else:
            #'Sem mais ambudrones!'
            #Retorna ao inicio da batalha
            pass     
            
    def run(self):
        #Botão Run
        if self.ling['hp']=10:
            #'Você foge antes que o Ling o note.'
            #Fim da batalha
            pass
        else:
            #'Ling está te perseguindo!'
            #Retorna ao inicio da batalha
            pass

class queen_battle(movimento):
    #Abre automaticamente se coordenadas = [10,7]
    #'Você chegou ao ponto de evacuação, mas ele está sendo ocupado por uma Queen! Derrote-a para que a nave de resgate possa se aproximar!'
    def __init__ (self, coordenadas, parametros_player = player, parametros_queen = queen):
        movimento.__init__(self, coordenadas)
        #Abrir batalha
        self.player = parametros_player
        self.queen = parametros_queen
        
    def attack (self):
        #Botão Attack
        dano = (self.player['atk']-self.queen['defn'])
        self.queen['hp'] -= dano
        #'Queen recebeu x de dano!'
        if self.queen['hp'] <= 0:
            #'Queen foi derrotada!'
            self.player['exp'] += self.queen['exppt']
            if self.player['exp'] >= self.player['proxlv']:
                #'Você passou de nível!'
                self.player['level'] += 1
                self.player['maxhp'] += 5
                self.player['hp'] = self.player['maxhp']
                self.player['atk'] += 3
                self.player['defn'] += 2
                self.player['exp'] = 0
                self.player['proxlv'] += 50
            else:
                pass
            player = self.player
            #Fim da batalha
            #'Você chegou ao ponto de evacuação!'
            #Fim de jogo
        else:
            #'Queen te atacou! Você recebeu x de dano!'
            self.player['hp'] -= max(1, (self.queen['atk'] - self.player['defn']))
                if self.player ['hp'] <= 0:
                    #Fim de jogo
                    pass
                else:
                    pass
            #Retorna ao inicio da batalha

    def item(self):
        #Botão Item
        if ambudrone > 0:
            ambudrone -= 1
            self.player['hp'] = self.player['maxhp']
            #Retorna ao inicio da batalha
        else:
            #'Sem mais ambudrones!'
            #Retorna ao inicio da batalha
            pass     
            
