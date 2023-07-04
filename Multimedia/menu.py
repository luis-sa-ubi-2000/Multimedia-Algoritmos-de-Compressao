#from Compressao import myhuffman
from logging import raiseExceptions
from Imagens import *
from Imagens.azul import filtro1
from Imagens.binaria import logica1
from Imagens.branco_preto import filtro2
from Imagens.corte import aritmetica1
from Imagens.inversao import aritmetica2
from Imagens.rotacao180 import logica2
from Video.video import vid2gray
from Audio.audio import *
from Compressao.myhuffman import *
import os


def listaFicheiros(path):
    files = os.listdir(path)
    print(" - - - - - - - - - -")
    for file in files:
        print(file)
    
    ficheiro = input("Escolha um ficheiro:")
    while ficheiro not in files: 
            print("O ficheiro não existe!")
            ficheiro = input("Escolha um ficheiro:")

    print(" - - - - - - - - - -")
    return path+ficheiro
    # do something

# Menu 
print("TRABALHO PRÁTICO DE MULTIMÉDIA")  
  
# Opções  
while True:  
    print("\nMENU PRINCIPAL")  
    print("1. Imagem")  
    print("2. Vídeo")
    print("3. Áudio")
    print("4. Compressão") 
    print("5. Sair")  
    escolha1 = int(input("Escolha uma opção:"))  
    
    #Imagens
    if escolha1 == 1:  
        print("\nESCOLHA QUAL DAS OPERAÇÕES QUER APLICAR À IMAGEM")  
        print("1. Operações aritméticas")  
        print("2. Operações lógicas")  
        print("3. Filtros")  
        print("4. Sair")  
        escolha2 = int(input("Escolha uma opção:"))  

        #Operações aritméticas
        if escolha2 == 1:
            print("\nDAS OPÇÕES DADAS O QUE PRETENDE FAZER?") 
            print("1. Corte")  
            print("2. Inversão da imagem verticalmente")   
            print("3. Sair")  
            escolha3 = int(input("Escolha uma opção:"))  

            if escolha3 == 1: 
                aritmetica1("Imagens/imagens/", listaFicheiros("Imagens/imagens/"))
                print("\ncorte.jpg criado com sucesso!\n")
                break

            elif escolha3 == 2:
                aritmetica2("Imagens/imagens/", listaFicheiros("Imagens/imagens/"))
                print("\ninversao.jpg criado com sucesso!\n")
                break

            elif escolha3 == 3:
                True

            else:
                print("Escolha inválida.") 

        #Operações lógicas    
        if escolha2 == 2:
            print("\nDAS OPÇÕES DADAS O QUE PRETENDE FAZER?")     
            print("1. Binária")  
            print("2. Rotação 180º")   
            print("3. Sair")  
            escolha4 = int(input("Escolha uma opção:"))  

            if escolha4 == 1:

                logica1("Imagens/imagens/", listaFicheiros("Imagens/imagens/"))
                print("\nbinaria.jpg criado com sucesso!\n")
                break

            elif escolha4 == 2:
                logica2("Imagens/imagens/", listaFicheiros("Imagens/imagens/"))
                print("\nrotacao180.jpg criado com sucesso!\n")
                break

            elif escolha4 == 3:
                True

            else:
                print("Escolha inválida.") 

        #Filtros
        if escolha2 == 3:
            print("\nDAS OPÇÕES DADAS O QUE PRETENDE FAZER?")   
            print("1. Filtro Azul")  
            print("2. Grayscale")   
            print("3. Sair")  
            escolha5 = int(input("Escolha uma opção:"))  

            if escolha5 == 1:
                filtro1("Imagens/imagens/", listaFicheiros("Imagens/imagens/"))
                print("\nazul.jpg criado com sucesso!\n")
                break

            elif escolha5 == 2:
                filtro2("Imagens/imagens/", listaFicheiros("Imagens/imagens/"))
                print("\nbranco_preto.jpg criado com sucesso!\n")
                break

            elif escolha4 == 3:
                True

            else:
                print("Escolha inválida.")  
  
        elif escolha2 == 4:  
            True  
              
        else:  
            print("Escolha inválida.")  

    #Vídeos 
    elif escolha1 == 2:  
  
        print("\nESCOLHA QUAL DAS OPERAÇÕES QUER APLICAR AO VíDEO")  
        print("1. Grayscale Video")    
        print("2. Sair")  
        escolha5 = int(input("Escolha uma opção:"))  

        #Operações aritméticas
        if escolha5 == 1:
            vid2gray("Video/videos/", listaFicheiros("Video/videos/"))
            print("\nvídeo covertido com sucesso!\n")
            break

        elif escolha5 == 2:  
            True  
              
        else:  
            print("Escolha inválida.")  

    #Áudio 
    elif escolha1 == 3:  
        print("\nESCOLHA QUAL DAS OPERAÇÕES QUER APLICAR AO ÁUDIO")  
        print("1. Operações de Edição")  
        print("2. Operações de Filtering")  
        print("3. Sair")  
        escolha6 = int(input("Escolha uma opção:"))  

        if escolha6 == 1:
            print("\nDAS OPÇÕES DADAS O QUE PRETENDE FAZER?") 
            print("1. Corte de Áudio")  
            print("2. Soma de Áudio")   
            print("3. Sair")  
            escolha7 = int(input("Escolha uma opção:"))  

            if escolha7 == 1: 
                cortaraudio("Audio/audio/", listaFicheiros("Audio/audio/"))
                print("\ncorte.wav criado com sucesso!\n")
                break

            elif escolha7 == 2:
                somaaudio("Audio/audio/",listaFicheiros("Audio/audio/"), listaFicheiros("Audio/audio/"))
                print("\naudiojunto.wav criado com sucesso!\n")
                break

            elif escolha7 == 3:
                True

            else:
                print("Escolha inválida.")

        #Filtros
        elif escolha6 == 2:
            print("\nDAS OPÇÕES DADAS O QUE PRETENDE FAZER?") 
            print("1. Aceleração do som")  
            print("2. Desaceleração do som")   
            print("3. Sair")  
            escolha8 = int(input("Escolha uma opção:"))

            if escolha8 == 1: 
                somrapido("Audio/audio/", listaFicheiros("Audio/audio/"))
                print("\nsomfast1.wav criado com sucesso!\n")
                break

            elif escolha8 == 2:
                somlento("Audio/audio/", listaFicheiros("Audio/audio/"))
                print("\nsomslow1.wav criado com sucesso!\n")
                break

            elif escolha8 == 3:
                True

            else:
                print("Escolha inválida.")

        elif escolha6 == 3:
            True

        else:
            print("Escolha inválida.") 

    #Compressão    
    elif escolha1 == 4:
        print("\nDAS OPÇÕES DADAS O QUE PRETENDE FAZER?")     
        print("1. Compressão por Codificação de Huffman")     
        print("2. Sair")  
        escolha8 = int(input("Escolha uma opção:"))  

        if escolha8 == 1:
            data = input(print("Digite uma string para codificar: "))
            Huffman_Encoding(data)
            encoding, tree = Huffman_Encoding(data)
            print("\nDados codificados: ", encoding)
            print("Dados descodificados: ", Huffman_Decoding(encoding,tree))
            break

        elif escolha4 == 2:
            True

        else:
            print("Escolha inválida.")

    elif escolha1 == 5:  
        break
       
    else:  
        print("Escolha inválida.")  
