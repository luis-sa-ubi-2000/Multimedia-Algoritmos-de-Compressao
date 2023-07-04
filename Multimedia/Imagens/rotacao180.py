#Author: Luís Sá

#Chamar a função logica2 no menu para a executar
def logica2(path, img):
    #Biblioteca para manipular a imagem
    from PIL import Image , ImageDraw

    #Abrir a imagem para a puder trabalhar
    imagem = Image.open(img)

    #Carregar imagem 
    carrega = imagem.load()

    #Variáveis que guardam o tamanho da imagem
    w, z = imagem.size

    #Variáveis secundárias para ler o valor guardado nas variáveis w e z 
    x = int(w)
    y = int(z)

    #Criar uma nova imagem para guardar as alterações que serão aplicadas à imagem original (Nota: Fazemos size = (x,y) para pudermos ver o corte em específico)
    nova_imagem = Image.new(imagem.mode, size = (x,y))

    #Desenhar a nova imagem na variável desenha para posteriormente ser manipulada
    desenha = ImageDraw.Draw(nova_imagem)

    #Ciclo repetitivo para correr todo o tamanho da imagem e fazer as respetivas modificações
    for i in range(0, x):
        for j in range(0, y):
            
            #Fazer teste para garantir que x e y sejam diferentes de zero e conseguir fazer a rotação na imagem (operação lógica) 
            if x != 0 and y != 0:

                    #Inverter o sentido da leitura da variável j que representa o eixo de sentido vertical
                    inversao = - j
                    
                    #Desenhar a imagem de baixo para cima verticalmente, rodando-a 180 graus 
                    desenha.point((i,j), carrega[i, inversao])

    #Guardar a nova imagem com o nome rotacao180.jpg para pudermos ver o resultado final deste algoritmo
    nova_imagem.save(path + "rotacao180.jpg")