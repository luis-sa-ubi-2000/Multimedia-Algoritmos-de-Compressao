#Author: Luís Sá

#Chamar a função filtro1 no menu para a executar
def filtro1(path, img):
    #Biblioteca para manipular a imagem
    from PIL import Image
    
    #Abrir a imagem para a puder trabalhar
    imagem = Image.open(img)
    
    #Criar uma nova imagem para guardar as alterações que serão aplicadas à imagem original
    nova_imagem = Image.new(imagem.mode, imagem.size)

    #Variáveis que guardam o tamanho da imagem
    w, z = imagem.size

    #Variáveis secundárias para ler o valor guardado nas variáveis w e z 
    x = int(w)
    y = int(z)
    
    #Ciclo repetitivo para correr todo o tamanho da imagem e fazer as respetivas modificações
    for i in range(0, x):
        for j in range(0, y):
            
            #Processar os píxeis da imagem original ajustados ao seu novo tamanho
            pixel = imagem.getpixel((i,j))

            #Atribuir aos valores R, G zero para remover todas as outras cores para além do azul, representada pelo valor B
            R = 0
            G = 0
            B = 255 - pixel[2]
    
            #Colocar esses píxeis que foram processados e alterados anteriormente à nova imagem
            nova_imagem.putpixel((i,j), (R, G, B))
    
    #Guardar a nova imagem com o nome azul.jpg para pudermos ver o resultado final deste algoritmo
    nova_imagem.save(path + "azul.jpg")