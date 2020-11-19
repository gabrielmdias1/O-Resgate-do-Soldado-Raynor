#O Resgato do Soldado Raynor - Comandos do jogo!

#Comandos - Tela inicial
#Space -> Sair da tela inicial/Começar o jogo

#Comandos - Navegação no mapa
#W -> Cima
#S -> Baixo
#A -> Esquerda
#D -> Direita
#Z -> Ver status do jogador

#Comandos - Lutas
#I -> Atacar(jogador) + Space -> Atacar(inimigo)
#O -> Usar ambudrone
#P -> Fugir da luta
#Z -> Ver status do jogador

#Objetivos do jogo
#O comandante Raynor ficou preso no centro de comando após um ataque surpresa
#do enxame zerg em nossa base de Redstone III. O traje dele está danificado e
#sem munição! Você deve chegar até a base e escoltar o comandante até o ponto
#de extração enquanto o enxame de lings bloqueia seu caminho! Nossas leituras
#indicam que há uma incubadora zerg nas proximidades do ponto de extração. Caso
#ataquemos a incubadora os zergs se concentrarão nela e o ponto de extração
#estará permanentemente bloqueado. Logo, a missão deve ser procedida da seguinte
#maneira: primeiramente o resgate e depois o ataque à incubadora.

#Imports, parâmetros e configurações iniciais
import sys, pygame , pygame.mixer
from pygame.locals import *
import time
import random
pygame.init()
pygame.display.init()
pygame.display.set_icon(pygame.image.load("terran_icon.png"))
setDisplay = pygame.display.set_mode((1024,576))
coord = [0,0]
player = {'level':1, 'hp':25, 'maxhp':25, 'atk':10, 'defn':5, 'exp':0, 'proxlv':100}
ling = {'hp':10, 'atk':8, 'defn':6, 'exppt':20}
queen = {'hp':40, 'atk':18, 'defn':12, 'exppt':100}
ambudrone = 3
title_screen_lock = 0
movement_lock = 0
attack_lock_ling = 1
attack_lock_queen = 1
ling_turn_lock = 1
queen_turn_lock = 1
spawn_rate = 0
run_lock = 0
raynor_found = 0
dano_ling = 0
dano_queen = 0
game_over = 0
game_clear = 0

#Cursor
CURSOR = (               #sized 24x24
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "         ......         ",
  "       ..oooooo..       ",
  "      .oo  XX  oo.      ",
  "     .o    XX    o.     ",
  "     .o    XX    o.     ",
  "    .o     XX     o.    ",
  "    .o     XX     o.    ",
  "XXXX.oXXXXXXXXXXXXo.XXXX",
  "XXXX.oXXXXXXXXXXXXo.XXXX",
  "    .o     XX     o.    ",
  "    .o     XX     o.    ",
  "     .o    XX    o.     ",
  "     .o    XX    o.     ",
  "      .oo  XX  oo.      ",
  "       ..oooooo..       ",
  "         ......         ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
)

cursor = pygame.cursors.compile(CURSOR)

pygame.mouse.set_cursor((24,24),(12,12),cursor[0],cursor[1])


#Arquivos da galeria a serem usados
pygame.display.set_caption('O Resgate do Soldado Raynor')
titulo = pygame.image.load('titulo_prototipo.jpg')
raynor = pygame.image.load('raynor.edit.png')
batalha_ling = pygame.image.load('batalha_fundo_prot.jpg')
batalha_ling_tiro = pygame.image.load('batalha_fundo_prot_tiro.jpg')
batalha_queen = pygame.image.load('batalho_queen_prot.jpg')
batalha_queen_tiro = pygame.image.load('batalho_queen_prot_tiro.jpg')
marine = pygame.image.load('marine_icon.png')
mapa = pygame.image.load('floor_map.png')
game_over_pic = pygame.image.load('game_over.jpg')
game_clear_pic = pygame.image.load('game_clear.jpg')
caixa_texto = pygame.image.load('text_box2.png')
caixa_opcoes = pygame.image.load('text_choice.png')
ambudrone_pic = pygame.image.load('ambudrone.edit.png')
bgm_titulo = pygame.mixer.Sound('wings_of_liberty.wav')
bgm_map1 = pygame.mixer.Sound('terran01.wav')
bgm_map2 = pygame.mixer.Sound('terran02.wav')
bgm_map4 = pygame.mixer.Sound('terran04.wav')
bgm_map5 = pygame.mixer.Sound('terran05.wav')
bgm_luta = pygame.mixer.Sound('battle_dangeralert.wav')
marine01 = pygame.mixer.Sound('marine01.wav')
marine02 = pygame.mixer.Sound('marine02.wav')
marine03 = pygame.mixer.Sound('marine03.wav')
marine04 = pygame.mixer.Sound('marine04.wav')
marine05 = pygame.mixer.Sound('marine05.wav')
marine07 = pygame.mixer.Sound('marine07.wav')
marine08 = pygame.mixer.Sound('marine08.wav')
marineshot1 = pygame.mixer.Sound('marine_shot02.wav')
marineshot1 = pygame.mixer.Sound('marine_shot1.wav')
marineshot2 = pygame.mixer.Sound('marine_shot2.wav')
ling1 = pygame.mixer.Sound('ling_cry01.wav')
ling2 = pygame.mixer.Sound('ling_cry02.wav')
ling4 = pygame.mixer.Sound('ling_cry04.wav')
ling5 = pygame.mixer.Sound('ling_cry05.wav')
queen1 = pygame.mixer.Sound('queen_cry01.wav')
queen2 = pygame.mixer.Sound('queen_cry02.wav')
queen3 = pygame.mixer.Sound('queen_cry03.wav')
queen4 = pygame.mixer.Sound('queen_cry04.wav')
raynor1 = pygame.mixer.Sound('raynor01.wav')
raynor2 = pygame.mixer.Sound('raynor02.wav')
raynor3 = pygame.mixer.Sound('raynor03.wav')
raynor4 = pygame.mixer.Sound('raynor04.wav')
raynor5 = pygame.mixer.Sound('raynor05.wav')
raynor6 = pygame.mixer.Sound('raynor06.wav')
raynor7 = pygame.mixer.Sound('raynor07.wav')
map_bgm_set = [bgm_map1,bgm_map2,bgm_map4,bgm_map5]


#Tela Inicial
setDisplay.blit(titulo,(0,0))
raynor5.play()
bgm_titulo.play(-1)

pygame.display.flip()




#Classe para a batalha com lings (Protótipo)(Não utilizada)
class ling_battle:
    def __init__ (self, parametros_player, parametros_ling):
        #'Você encontrou um Ling!'
        self.player = parametros_player
        self.ling = parametros_ling
    def battle_start(self):
        movement_lock += 1
        attack_lock = 0
        spawn_rate == 0
        pygame.mixer.stop()
        bgm_luta.play(-1)
        setDisplay.blit(ling_battle,(0,0))
        setDisplay.blit(text_choice,(347,0))
        ling1.play()
        pygame.display.flip()
    def attack (self):
        marine02.play()
        ling4.play()
        dano = (self.player['atk']-self.ling['defn'])
        self.ling['hp'] -= dano
        #'Ling recebeu %d de dano!'.format(dano)
        if self.ling['hp'] <= 0:
            marine04.play()
            ling5.play()
            #'Ling foi derrotado!'
            self.player['exp'] += self.ling['exppt']
            if self.player['exp'] >= self.player['proxlv']:
                marine05.play()
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
            marine03.play()
            random.choice(map_bgm_set).play(-1)
            setDisplay.blit(mapa,(0,0))
            setDisplay.blit(marine,coord)
            pygame.display.flip()
        else:
            dano_ling = max(1, (self.ling['atk'] - self.player['defn']))
            self.player['hp'] -= dano_ling
            ling2.play()
            #'Ling te atacou! Você recebeu %d de dano!'.format(dano_ling)
            if self.player['hp'] <= 0:
                pygame.mixer.stop()
                setDisplay.blit(teste,(0,0))
                pygame.display.flip()
            else:
                setDisplay.blit(ling_battle,(0,0))
                pygame.display.flip()
                
    def item(self):
        #Botão Item
        if ambudrone > 0:
            #'Você usou um ambudrone para reparar seu traje!'
            ambudrone -= 1
            self.player['hp'] == self.player['maxhp']
            setDisplay.blit(ling_battle,(0,0))
            pygame.display.flip()
        else:
            #'Sem mais ambudrones!'
            setDisplay.blit(ling_battle,(0,0))
            pygame.display.flip()
                
            
    def run(self):
        #Botão Run
        if self.ling['hp']==10:
            #'Você foge antes que o Ling o note.'
            #Fim da batalha
            pass
        else:
            #'Ling está te perseguindo!'
            #Retorna ao inicio da batalha
            pass

#Classe para batalha com a Queen (Protótipo)(Não utilizada)
class queen_battle:
    #Abre automaticamente se coordenadas = [10,7]
    #'Você chegou ao ponto de evacuação, mas ele está sendo ocupado por uma Queen! Derrote-a para que a nave de resgate possa se aproximar!'
    def __init__ (self, coordenadas, parametros_player, parametros_queen):
        movimento.__init__(self, coordenadas)
        #Abrir batalha
        self.player = parametro_player
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
            #'Você usou um ambudrone para reparar seu traje!'
            ambudrone -= 1
            self.player['hp'] = self.player['maxhp']
            #Retorna ao inicio da batalha
        else:
            #'Sem mais ambudrones!'
            #Retorna ao inicio da batalha
            pass


#Comandos no teclado e interações
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        sys_font = pygame.font.SysFont ("None",60)    
        if event.type == KEYDOWN:

            if event.unicode == " ":
                if title_screen_lock == 0:
                    title_screen_lock += 1
                    bgm_titulo.stop()
                    marine01.play()
                    random.choice(map_bgm_set).play(-1)
                    setDisplay.blit(mapa,(0,0))
                    setDisplay.blit(marine,coord)
                    pygame.display.flip()
                else:
                    pass
            if event.unicode == "z" and title_screen_lock == 1:
                stats = 'Level %d, HP %d, EXP %d, ProxLv %d'%(player['level'],player['hp'],player['exp'],player['proxlv'])
                stats_render = sys_font.render(stats,0,(255,255,255))
                setDisplay.blit(stats_render,(200,200))
                pygame.display.flip()
            if event.unicode == "w" and movement_lock == 0 and title_screen_lock == 1:
                    
                coord[1] -= 32
                setDisplay.blit(mapa,(0,0))
                setDisplay.blit(marine,coord)
                pygame.display.flip()
                spawn_rate += 1
                
            if event.unicode == "d" and movement_lock == 0 and title_screen_lock == 1:
                    
                coord[0] += 32
                setDisplay.blit(mapa,(0,0))
                setDisplay.blit(marine,coord)
                pygame.display.flip()
                spawn_rate += 1
                
            if event.unicode == "a" and movement_lock == 0 and title_screen_lock == 1:
                    
                coord[0] -= 32
                setDisplay.blit(mapa,(0,0))
                setDisplay.blit(marine,coord)
                pygame.display.flip()
                spawn_rate += 1
            if event.unicode == "s" and movement_lock == 0 and title_screen_lock == 1:
                    
                coord[1] += 32
                setDisplay.blit(mapa,(0,0))
                setDisplay.blit(marine,coord)
                pygame.display.flip()
                spawn_rate += 1

            if spawn_rate >= 10 and movement_lock == 0:
                movement_lock += 1
                attack_lock_ling = 0
                spawn_rate = 0
                pygame.mixer.stop()
                bgm_luta.play(-1)
                setDisplay.blit(batalha_ling,(0,0))
                setDisplay.blit(caixa_opcoes,(379,0))
                ling1.play()
                marine02.play()
                mensagem_encontro = sys_font.render ('Voce encontrou um Ling!', 0,(255,255,255))
                setDisplay.blit(mensagem_encontro,(270, 500))
                pygame.display.flip()
            if event.unicode == "i" and attack_lock_ling == 0 and ling_turn_lock == 1:
                run_lock += 1
                marineshot1.play()
                marine07.play()
                ling4.play()
                dano = (player['atk']-ling['defn'])
                dano_ling += dano
                setDisplay.blit(batalha_ling_tiro,(0,0))
                setDisplay.blit(caixa_opcoes,(379,0))
                msg_dano = 'Ling recebeu %d de dano!'%dano
                msg_dano_render = sys_font.render (msg_dano, 0,(255,255,255))
                setDisplay.blit(msg_dano_render,(265, 500))
                pygame.display.flip()
                ling_turn_lock = 0
            if event.unicode == " " and attack_lock_ling == 0 and ling_turn_lock == 0:
                ling2.play()
                dano_player =(ling['atk']-player['defn'])
                player['hp'] -= dano_player
                setDisplay.blit(batalha_ling,(0,0))
                setDisplay.blit(caixa_opcoes,(379,0))
                msg_dano_player = 'Voce recebeu %d de dano!'%dano_player
                msg_dano_player_render = sys_font.render (msg_dano_player, 0,(255,255,255))
                setDisplay.blit(msg_dano_player_render,(265, 500))
                pygame.display.flip()
                ling_turn_lock = 1
            if event.unicode == " " and attack_lock_queen == 0 and queen_turn_lock == 0:
                queen2.play()
                dano_player =(queen['atk']-player['defn'])
                player['hp'] -= dano_player
                setDisplay.blit(batalha_queen,(0,0))
                setDisplay.blit(caixa_opcoes,(320,0))
                msg_dano_player_queen = 'Voce recebeu %d de dano!'%dano_player
                msg_dano_player_queen_render = sys_font.render (msg_dano_player_queen, 0,(255,255,255))
                setDisplay.blit(msg_dano_player_queen_render,(265, 500))
                pygame.display.flip()
                queen_turn_lock = 1
            if event.unicode == "i" and attack_lock_queen == 0 and queen_turn_lock == 1:
                run_lock += 1
                marineshot1.play()
                marine07.play()
                queen4.play()
                dano = max(1,(player['atk']-queen['defn']))
                dano_queen += dano
                setDisplay.blit(batalha_queen_tiro,(0,0))
                setDisplay.blit(caixa_opcoes,(320,0))
                msg_dano_queen = 'Queen recebeu %d de dano!'%dano
                msg_dano_queen_render = sys_font.render (msg_dano_queen, 0,(255,255,255))
                setDisplay.blit(msg_dano_queen_render,(265, 500))
                pygame.display.flip()
                queen_turn_lock = 0
            if event.unicode == "p" and attack_lock_ling == 0 and run_lock == 0:    
                attack_lock_ling += 1
                movement_lock = 0
                pygame.mixer.stop()
                marine08.play()
                msg_fuga = sys_font.render ('Voce fugiu antes que o Ling o percebesse!',0,(255,255,255))
                random.choice(map_bgm_set).play(-1)
                setDisplay.blit(mapa,(0,0))
                setDisplay.blit(marine,coord)
                setDisplay.blit(msg_fuga,(100,500))
                pygame.display.flip()
            if event.unicode == "p" and attack_lock_ling == 0 and run_lock >= 1:    
                fuga_travada = sys_font.render ('Voce nao consegue escapar!',0,(255,255,255))
                setDisplay.blit(batalha_ling,(0,0))
                setDisplay.blit(caixa_opcoes,(379,0))
                setDisplay.blit(fuga_travada,(240,500))
                pygame.display.flip()
            if coord == [992,544] and movement_lock == 0 and raynor_found == 1:
                movement_lock += 1
                attack_lock_queen = 0
                spawn_rate = 0
                pygame.mixer.stop()
                bgm_luta.play(-1)
                setDisplay.blit(batalha_queen,(0,0))
                setDisplay.blit(caixa_opcoes,(320,0))
                queen1.play()
                marine02.play()
                mensagem_encontro_queen = sys_font.render ('Uma Queen esta bloqueando o caminho!', 0,(255,255,255))
                setDisplay.blit(mensagem_encontro_queen,(100, 500))
                pygame.display.flip()
            if coord == [768,0] and movement_lock == 0 and raynor_found ==0:
                raynor_found = 1
                raynor1.play()
                setDisplay.blit(raynor,(400,70))
                raynor_found_msg1 = sys_font.render ('Voce encontrou o comandante Raynor!',0,(255,255,255))
                raynor_found_msg2 = sys_font.render ('Voce deve leva-lo ate o ponto de evacuacao!',0,(255,255,255))
                setDisplay.blit(raynor_found_msg1,(125,20))
                setDisplay.blit(raynor_found_msg2,(70,500))
                pygame.display.flip()
            if event.unicode == "p" and attack_lock_queen == 0:
                fuga_travada = sys_font.render ('Voce nao consegue escapar!',0,(255,255,255))
                setDisplay.blit(batalha_queen,(0,0))
                setDisplay.blit(caixa_opcoes,(320,0))
                setDisplay.blit(fuga_travada,(240,500))
                pygame.display.flip()
            if event.unicode == "o" and attack_lock_queen == 0:
                if ambudrone > 0:
                    ambudrone -= 1
                    player['hp'] = player['maxhp']
                    setDisplay.blit(batalha_queen,(0,0))
                    setDisplay.blit(caixa_opcoes,(320,0))
                    setDisplay.blit(ambudrone_pic,(0,0))    
                    ambudrone_msg = sys_font.render('Voce usou um ambudrone para reparar seu traje!',0,(255,255,255))
                    setDisplay.blit(ambudrone_msg,(20,500))
                    pygame.display.flip()
                else:
                    setDisplay.blit(batalha_queen,(0,0))
                    setDisplay.blit(caixa_opcoes,(320,0))
                    ambudrone_msg2 = sys_font.render('Voce nao tem mais ambudrones!',0,(255,255,255))
                    setDisplay.blit(ambudrone_msg2,(165,500))
                    pygame.display.flip()
            if event.unicode == "o" and attack_lock_ling == 0:
                if ambudrone > 0:
                    ambudrone -= 1
                    player['hp'] = player['maxhp']
                    setDisplay.blit(batalha_ling,(0,0))
                    setDisplay.blit(caixa_opcoes,(379,0))
                    setDisplay.blit(ambudrone_pic,(0,0))                    
                    ambudrone_msg = sys_font.render('Voce usou um ambudrone para reparar seu traje!',0,(255,255,255))
                    setDisplay.blit(ambudrone_msg,(20,500))
                    pygame.display.flip()
                else:
                    setDisplay.blit(batalha_ling,(0,0))
                    setDisplay.blit(caixa_opcoes,(379,0))
                    ambudrone_msg2 = sys_font.render('Voce nao tem mais ambudrones!',0,(255,255,255))
                    setDisplay.blit(ambudrone_msg2,(165,500))
                    pygame.display.flip()
            if dano_ling >= 10:
                run_lock = 0
                ling_turn_lock = 1
                pygame.mixer.stop()
                marineshot1.play()
                marine04.play()
                ling5.play()
                random.choice(map_bgm_set).play(-1)
                vitoria_ling_msg = sys_font.render('Voce derrotou o Ling!',0,(255,255,255))
                setDisplay.blit(vitoria_ling_msg,(290,400))
                movement_lock = 0
                dano_ling = 0
                pygame.display.flip()
                attack_lock_ling = 1
                player ['exp'] += ling ['exppt']
            if player ['exp'] >= player['proxlv']:
                pygame.mixer.stop()
                marineshot1.play()
                marine05.play()
                ling5.play()
                levelup_msg = sys_font.render('Voce passou de nivel!',0,(255,255,255))
                setDisplay.blit(levelup_msg,(290,300))
                pygame.display.flip()
                random.choice(map_bgm_set).play(-1)
                player['level'] += 1
                player['maxhp'] += 5
                player['hp'] = player['maxhp']
                player['atk'] += 3
                player['defn'] += 2
                player['exp'] = 0
                player['proxlv'] += 50
            if dano_queen >= 40 and game_clear == 0:
                attack_lock_queen = 1
                pygame.mixer.stop()
                marineshot1.play()
                marine04.play()
                queen4.play()
                random.choice(map_bgm_set).play(-1)
                vitoria_queen_msg = sys_font.render('Voce derrotou a Queen!',0,(255,255,255))
                setDisplay.blit(vitoria_queen_msg,(290,300))
                vitoria_queen_msg = sys_font.render('Pressione space para continuar',0,(255,255,255))
                setDisplay.blit(vitoria_queen_msg,(220,200))
                game_clear = 1
                pygame.display.flip()
            if game_clear == 1 and event.unicode == " ":
                pygame.mixer.stop()
                setDisplay.blit(game_clear_pic,(0,0))
                pygame.display.flip()
                bgm_titulo.play()
            if player['hp'] <= 0:
                attack_lock_ling = 1
                attack_lock_queen = 1
                pygame.mixer.stop()
                queen3.play()
                death_msg = sys_font.render('Voce foi morto!',0,(255,255,255))
                setDisplay.blit(death_msg,(360,300))
                death1_msg = sys_font.render('Pressione z para continuar',0,(255,255,255))
                setDisplay.blit(death1_msg,(240,200))
                pygame.display.flip()
                game_over = 1
            if event.unicode == "z" and game_over == 1:
                pygame.mixer.stop()
                setDisplay.blit(game_over_pic,(0,0))
                pygame.display.flip()
                
            
