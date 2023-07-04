#Author: Luís Sá

#Chamar a função filtro2 no menu para a executar
def filtro2(path, img):
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
    
    #Guardar a nova imagem com o nome branco_preto.jpg para pudermos ver o resultado final deste algoritmo
    nova_imagem.save(path + "branco_preto.jpg")