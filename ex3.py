import random

def escolher_palavra():
    palavras = ["python", "programacao", "jogo", "desenvolvimento", "computador", "aula", "linguagem"]
    return random.choice(palavras).lower()

def mostrar_palavra_oculta(palavra, letras_adivinhadas):
    return ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])

def jogar_jogo():
    palavra_oculta = escolher_palavra()
    tentativas_restantes = random.randint(6, 11)
    letras_adivinhadas = set()
    print("Bem-vindo ao Jogo da Forca!")
    print("A palavra tem", len(palavra_oculta), "letras.")
    while tentativas_restantes > 0:
        print("\nPalavra atual:", mostrar_palavra_oculta(palavra_oculta, letras_adivinhadas))
        print("Tentativas restantes:", tentativas_restantes)
        palpite = input("Digite uma letra: ").lower()
        if palpite in letras_adivinhadas:
            print("Você já tentou essa letra. Tente novamente.")
        elif palpite in palavra_oculta:
            print("Letra correta!")
            letras_adivinhadas.add(palpite)
        else:
            print("Letra incorreta. Tente novamente.")
            tentativas_restantes -= 1
        if set(palavra_oculta) == letras_adivinhadas:
            print("\nParabéns! Você adivinhou a palavra:", palavra_oculta)
            break
    if tentativas_restantes == 0:
        print("\nFim de jogo. Você não conseguiu adivinhar a palavra. A palavra era:", palavra_oculta)
jogar_jogo()