import random
import os
import time

tentativas = 3

def atualizar_tela():

    os.system('cls')
    print ("===== JOGO DA FORCA =====")
    print (f"Dica: {dicas} ")
    input("Digite uma letra: ")
    print (f"Tentativas Restantes: ", tentativas)
    print (palavra_vazia)
    time.sleep(2)


palavras = ['thelastofus',
            'residentevil',
            'gta',
            'valorant',
            'csgo',
            'fortnite',
            'minecraft',
            'roblox',
            'mariokart',
            'godofwar']

dicas = [

    "Sobrevivência em um mundo tomado por infectados.",  
    "Vírus, monstros e uma corporação sombria.",  
    "Crimes e liberdade em cidade fictícia.",  
    "Agentes com poderes em combates táticos.",  
    "Confronto entre terroristas e contra-terroristas.",
    "Battle royale com construções rápidas.", 
    "Mundos de blocos e criaturas noturnas.", 
    "Criação e jogos feitos por usuários.",  
    "Corridas com itens e personagens famosos.",
    "Guerreiro enfrenta deuses da mitologia.", 
]

sorteio = random.randint(0, len(palavras) -1)
palavra_escolhida = palavras[sorteio]
dica_sorteada = dicas[palavras]
palavra_vazia = ['_'] * len(palavra_escolhida)











