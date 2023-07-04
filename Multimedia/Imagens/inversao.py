#Author: Luís Sá

#Chamar a função aritmetica2 no menu para a executar
def aritmetica2(path, img):
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
    
    if y < x:

        print("Não é possível inverter verticalmente esta imagem devido às suas dimensões. Por favor, escolha outra imagem.\n")
        exit()
        
    else:
    #Ciclo repetitivo para correr todo o tamanho da imagem e fazer as respetivas modificações
        for i in range(0, x):
            for j in range(0, y):

            
                #Guardar o limite da imagem invertida para que este não seja ultrapassado posteriormente no seu processamento (operação aritmética)
                dimensao = x - j - 1

                #Desenhar a imagem no sentido contrário, invertendo-a, neste caso, verticalmente
                desenha.point((i,j), carrega[dimensao, i])
    
    #Guardar a nova imagem com o nome inversao.jpg para pudermos ver o resultado final deste algoritmo
    nova_imagem.save(path + "inversao.jpg")
    
    return x,y

    