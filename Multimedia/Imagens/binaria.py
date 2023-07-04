#Author: Luís Sá

#Chamar a função logica1 no menu para a executar
def logica1(path, img):
    #Biblioteca para manipular a imagem
    from PIL import Image
    
    #Abrir a imagem para a puder trabalhar
    imagem = Image.open(img)
    
    #Processar imagem 
    guadar = imagem.getdata()
    
    #Criar uma lista vazia para posteriormente ser preenchida 
    pixel = []
    
    #Ciclo repetitivo para carregar a lista
    for i in guadar:
            
            #Lista é carregada com os valores para converter a imagem do tipo RGB para "grayscale"
            pixel.append(0.2989 * i[0] + 0.5870 * i[1] + 0.1140 * i[2])
    
    #Criar uma nova imagem para guardar as alterações que serão aplicadas à imagem original
    nova_imagem = Image.new("L", imagem.size)
    
    #Implementar os valores guardados na lista à nova imagem criada
    nova_imagem.putdata(pixel)
    
    #Criar um valor limite 
    limite = 100

    #Limitar um valor qualquer de nome lambda para estar entre 100 e 255 com o objetivo de a alteração na imagem ser visível (operação lógica)
    nova_imagem2 = nova_imagem.point(lambda p: p > limite and 255)
    
    #Guardar a nova imagem com o nome binaria.jpg para pudermos ver o resultado final deste algoritmo
    nova_imagem2.save(path + "binaria.jpg")