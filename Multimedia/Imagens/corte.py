#Author: Luís Sá

#Chamar a função aritmetica1 no menu para a executar
def aritmetica1(path, img):
    #Biblioteca para manipular a imagem
    from PIL import Image

    #Abrir a imagem para a puder trabalhar
    imagem = Image.open(img)

    #Variáveis que guardam o tamanho da imagem
    w, z = imagem.size
    
    #Variáveis secundárias tanto para ler como multiplicar o valor guardado nas variáveis w e z e diminuir o seu tamanho a metade (operação aritmética)
    x = int(w * 1/2)
    y = int(z * 1/2)
    
    #Criar uma nova imagem para guardar as alterações que serão aplicadas à imagem original (Nota: Fazemos size = (x,y) para pudermos ver o corte em específico)
    nova_imagem = Image.new(imagem.mode, size = (x,y))
    
    #Ciclo repetitivo para correr todo o tamanho da imagem e fazer as respetivas modificações
    for i in range(0, x):
        for j in range(0, y):

            #Processar os píxeis da imagem original ajustados ao seu novo tamanho
            corte = imagem.getpixel((i,j))

            #Colocar esses píxeis que foram processados anteriormente à nova imagem
            nova_imagem.putpixel((i,j),corte)

    #Guardar a nova imagem com o nome corte.jpg para pudermos ver o resultado final deste algoritmo
    nova_imagem.save(path + "corte.jpg")