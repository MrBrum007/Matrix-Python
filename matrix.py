# Importando as bibliotecas
import pygame
from pygame.locals import *
from sys import exit
from random import randrange, choice

# Setando o início das funções da biblioteca 'pygame'
pygame.init()

# CRIANDO AS VARIAVEIS

# Definindo as cores
preto = (0, 0, 0)
verde = (0, 255, 0)
branco = (255, 255, 255)

# Definindo o tamanho da janela de animação
larguraTela = 1080
alturaTela = 720

# Definindo as variaveis de objetos (linhas de texto)
listaObjetos = []
listaPosicaoObjetos = []
numeroObjetos = 20
gerar = False

# Criando a lista de letras e definindo a fonte
letras = ["0", "1"]
tamanhoFonte = 12
fonte = pygame.font.SysFont(None, tamanhoFonte, True, True)

# Criando a janela de animação
tela = pygame.display.set_mode((larguraTela, alturaTela)) # não tenho certeza do por que dos 2 parenteses, mas funcionou assim então vida q segue
pygame.display.set_caption("Animação Matrix")

# Definindo o FPS
FPS = 15
tempo = pygame.time.Clock()
tempoInicial = 0
tempoAtual = 0

# Criando a classe principal e as funções
class linhasMatrix:
    def __init__(self):
        self.fill = 1 # define a quantidade de linhas por coluna
        self.listaPosicaoLetrasEixoY = []  # armazena as posições Y de cada letra na linha
        self.listaLetrasLinha = [] # armazena as letras de cada linha
        self.posicaoEixoX = randrange(tamanhoFonte, larguraTela + tamanhoFonte, tamanhoFonte) # eixoX e eixoY definem as posições iniciais da linha
        self.posicaoEixoY = randrange(0, alturaTela + tamanhoFonte, tamanhoFonte)
        self.listaPosicaoLetrasEixoY.append(self.posicaoEixoY)
        # No final de tudo cada coluna tem 'fill' linhas, sendo a linha estando em uma posição 'eixoX, eixoY' na janela , com as letras 'listaLetras' estando em uma posição 'listaPosicaoLetrasEixoY' na linha.

    # Criando a função para desenhar as linhas com letras
    def desenharLinhas(self):
        letrasAleatorias = choice(letras) # escolhe uma letra na lista de letras 
        self.listaLetrasLinha.append(letrasAleatorias) # adiciona a letra escolhida na lista de letras da linha

        # Para cada  letra na lista de letras da linha, na posição  'eixoX' e 'listaPosicaoLetrasEixoY' na janela
        for msg, y in zip(self.listaLetrasLinha, self.listaPosicaoLetrasEixoY):
            mensagem = f"{msg}" #  mensagem é a combinação de letras escolhida
            texto = fonte.render(mensagem, True, verde) # texto  é a combinação de letras escolhida, sendo renderizada na janela
            tela.blit(texto, (self.posicaoEixoX, y)) #  texto é desenhado na janela, na posição  'eixoX' e 'eixoY'

    # Criando a função para deslocar as linhas para baixo
    def deslocarLinhas(self):
        if self.posicaoEixoY > alturaTela or len(self.listaPosicaoLetrasEixoY) > 20: # se a posição Y da linha for maior q a altura da tela, a linha chegou no fim OU se o tamanho da lisa for maior que 20
            mensagem = " " # cria uma mensagem em branco
            texto = fonte.render(mensagem, True, branco) # renderiza como um texto branco
            tela.fill(preto, (self.posicaoEixoX, self.listaPosicaoLetrasEixoY[0], texto.get_width() + tamanhoFonte, texto.get_height() * self.fill)) # cria um retangulo preto q apaga a linha da tela
            if texto.get_height() * self.fill > len(self.listaPosicaoLetrasEixoY) * texto.get_height(): # calcula  a altura da linha de texto atual e a altura total da lista de letras
                self.listaLetrasLinha.clear() # se for verdade, apaga a linha
            else:
                self.fill += 1 # senão, aumenta a quantidade de letras por linha

        else:
            self.posicaoEixoY += tamanhoFonte # aumenta  a posição Y da linha em 'tamanhoFonte', o que significa mais uma letra na linha
            self.listaPosicaoLetrasEixoY.append(self.posicaoEixoY) # adiciona essa posição adicionada na lista de posições
            mensagem = f"{self.listaLetrasLinha[-1]}" # cria uma mensagem com a ultima letra da linha
            texto = fonte.render(mensagem, True, branco) # renderiza como um texto branco
            tela.fill(preto, (self.posicaoEixoX, self.listaPosicaoLetrasEixoY[-1], texto.get_width() + tamanhoFonte, texto.get_height())) # cria um retangulo preto que vai apagar essa letra
            tela.blit(texto, (self.posicaoEixoX, self.listaPosicaoLetrasEixoY[-1])) # desenha uma nova letra na nova posição Y

# Criando a função para executar varias vezes
def criarMultiplosObjetos(listaObjetos, numeroObjetos, gerar):
    if gerar: # checa se 'gerar' é verdadeiro
        for i in range(numeroObjetos): # a função vai rodar 'numeroObjetos' vezes,
            objeto = linhasMatrix()    # criando varios objetos, sendo eles uma instancia da função 'linhasMatrix()'
            if objeto.posicaoEixoX in listaPosicaoObjetos or objeto.posicaoEixoY > alturaTela: # se o objeto já constar na lista de posições de objetos OU se a posição Y do objeto for maior que a altura da tela
                listaPosicaoObjetos.remove(objeto.posicaoEixoX) # remove o objeto duplicado
                del objeto  # apaga o objeto pra liberar espaço
            else:
                listaObjetos.append(objeto) # se a condição acima não acontecer, adicionamos o objeto a lista de objetos
                listaPosicaoObjetos.append(objeto.posicaoEixoX) # adiciona a posição do objeto na lista de posições de objetos
        for i in listaObjetos: # encontra os objetos na lista de objetos
            i.desenharLinhas() # desenha a linha do objeto, com a função 'desenharLinhas()'
            i.deslocarLinhas() # desloca a linha do objeto, com a função 'deslocarLinhas()'

# Executando a janela de animação efetivamente
while True:
    tempo.tick(FPS) # define o jogo para rodar a 15 fps
    tela.fill((preto)) # deixa a tela preta para começar o jogo

    for event in pygame.event.get(): # checa se algum evento foi acionado
        if event.type == QUIT:  # se o evento for o fechamento da janela
            pygame.quit()  # fecha a janela
            exit()         # sai do jogo

    tempoAtual = pygame.time.get_ticks() # conta o tempo desde que 'pygame.init()' foi chamado (ou seja, desde que o programa está efetivamente rodando)

    if tempoAtual - tempoInicial > 200: # checa se tem no mínimo 200 milisegundos que o último objeto foi gerado
        gerar = True # se  for verdadeiro, gera um novo objeto (a variavel se torna True e a função anterior é chamada)
        tempoInicial = pygame.time.get_ticks() #  atualiza o tempo inicial para o momento atual, para o loop poder rodar novamente

    criarMultiplosObjetos(listaObjetos, numeroObjetos, gerar) # chama a função para gerar os objetos
    pygame.display.flip() # como se fosse um botão de atualizar, faz o uptade da tela a cada frame para o jogo rodar normalmente