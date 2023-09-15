import jogo_forca
import jogo_adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca\n(2) Adivinhação")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca")
        jogo_forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhação")
        jogo_adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()