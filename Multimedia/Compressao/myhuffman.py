# A Huffman Tree Node
class Node:
    def __init__(self, freq, char, left=None, right=None):
        # Frequencias do simbolo
        self.freq = freq

        # Simbolo 
        self.char = char

        # Node esquerdo
        self.left = left

        # Node Direito
        self.right = right

        # Caminho (0/1)
        self.code = ''

'''Função secundária que permite imprimir o código dos simbolos atravessando a árvore'''
codes = dict()

def Calculate_Codes(node, val=''):
    # Determina o código do node
    new_code = val + str(node.code)

    if(node.left):
        Calculate_Codes(node.left, new_code)
    if(node.right):
        Calculate_Codes(node.right, new_code)

    if(not node.left and not node.right):
        codes[node.char] = new_code
         
    return codes

''' Função secundária que determina a frequencia de um simbolo numa determinada string'''
def Calculate_Frequency(data):
    chars_frequency = dict()
    for element in data:
        if chars_frequency.get(element) == None:
            chars_frequency[element] = 1
        else: 
            chars_frequency[element] += 1
    return chars_frequency

''' Função secundária que determina a probabilidade de um simbolo numa determinada string'''
def Calculate_Probability(data):
    probability = 0
    total_chars = 0
    chars_frequency = Calculate_Frequency(data)
    chars_probability = dict()
    for element in data:
        total_chars += 1 

    for element in data:
        probability = chars_frequency[element] / total_chars
        chars_probability[element] = probability

    return chars_probability

'''Função secundária que obtem o output codificado'''
def Encode_Output(data, coding):
    encoding_output = []
    for c in data:
      #  print(coding[c], end = '')
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string

''' Função secundária que calcula a o ganho entre os dados antes e depois da compressão'''   
def Compression_Gains(data, coding):
    # Tamanho da string = Numero de caracteres * 8 (Numero de bits num caractere)
    before_compression = len(data) * 8 
    after_compression = 0
    chars = coding.keys()
    for char in chars:
        count = data.count(char)

        # Tamanho da string = Numero de caracteres * 8 (Numero de bits num caractere)
        after_compression += count * len(coding[char])

    print(f"\nTamanho da string antes da compressão: {before_compression} bits")    
    print(f"Tamanho da string depois da compressão: {after_compression} bits")
    print("Taxa de compressão: %.2f%%" % ((after_compression / before_compression) * 100))       

''' Função principal que permite comprimir os dados de uma determinada string através do algoritmo de Huffman'''
def Huffman_Encoding(data):
    char_with_freqs = Calculate_Frequency(data)
    chars = char_with_freqs.keys()
    print("teste", char_with_freqs)

    # char_with_probs = Calculate_Probability(data)
    ''' Depois de ter as frequencias dos chars
        1 - ordenar osvalore do menor para o maior
        2 - construir a arvore apartir dai'''
    nodes = []
    
    # Constroi a nodes da árvore de Huffman
    for char in chars:
        nodes.append(Node(char_with_freqs.get(char), char))
        #print("%c : %d : %.2f" % (char, char_with_freqs[char], char_with_probs[char]))
        
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their 
        nodes = sorted(nodes, key=lambda x: x.freq)
    
        # Escolhe os dois nodes com menor valor
        right = nodes[0]
        left = nodes[1]
    
        # Atribui valores(0/1) a cada ramo
        left.code = 0
        right.code = 1
    
        # Cria um novo node apartir da soma dos dois ultimos nodes
        newNode = Node(left.freq+right.freq, left.char+right.char, left, right)


        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
    
    huffman_encoding = Calculate_Codes(nodes[0])
    
    print("Letra   :  Frequencia  :  Código")
    for char in huffman_encoding:
        print("  %c     :       %d      :  %s  " % (char, char_with_freqs[char], huffman_encoding[char]))
    
    
    Compression_Gains(data, huffman_encoding)
    encoded_output = Encode_Output(data,huffman_encoding)
    return encoded_output, nodes[0]  
    
 
def Huffman_Decoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right   
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.char == None and huffman_tree.right.char == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.char)
            huffman_tree = tree_head
        
    string = ''.join([str(item) for item in decoded_output])
    return string        


""" First Test """



""" Second Test """

# f = open("demofile.txt", "r")

# data = f.read()
# print(data)
# Huffman_Encoding(data)