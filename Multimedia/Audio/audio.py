#Author: Bernardo Claro
import wave

def cortaraudio(path, audio):
     
        start = 0 # segundos
        end = 4 # segundos
        input = wave.open(audio, "rb") #abrir ficheiro de input

        
        nchannels = input.getnchannels() # retorna o numero de canais
        sampwidth = input.getsampwidth() # retorna a largura da amostra de audio
        framerate = input.getframerate() # retorna a frequencia  de amostragem
    # Colocamos a posição do ponteiro do ficheiro onde queremos
        input.setpos(start * framerate)
    # extraimos os dados da amostra no intervalo que queremos
        data = input.readframes(int((end - start) * framerate))

# escrevemos os dados extraidos no novo ficheiro
        output = wave.open(path + "corte.wav", 'w')
        output.setnchannels(nchannels)
        output.setsampwidth(sampwidth)
        output.setframerate(framerate)

        output.writeframes(data )
        






def somaaudio(path, audio1, audio2):




    input = wave.open(audio1, "rb") # abrir primeiro ficheiro
    input2 = wave.open(audio2, "rb") # abrir segundo ficheiro


    nchannels = input.getnchannels()
    sampwidth = input.getsampwidth()
    framerate = input.getframerate()

    framerate2 = input2.getframerate()
        # Colocamos a posição do ponteiro do ficheiro onde queremos
    input.setpos(int(0))
        # le determinado numero de segundos dos inputs e soma-os
    data = input.readframes(int((input.getnframes() / input.getframerate()) * framerate)) + input2.readframes(int((input2.getnframes() / input2.getframerate()) * framerate2))
    # escreve os dados extraidos para um novo ficheiro
    output = wave.open(path + 'audiojunto.wav', 'w')
    output.setnchannels(nchannels)
    output.setsampwidth(sampwidth)
    output.setframerate(framerate)
    output.setnframes(int(len(data) / sampwidth))
    output.writeframes(data)






def somrapido(path, audio):

    input = wave.open(audio, "rb") # abre ficheiro


    nchannels = input.getnchannels()
    sampwidth = input.getsampwidth()
    framerate = input.getframerate()


        # Colocamos a posição do ponteiro do ficheiro onde queremos
    input.setpos(int(0))
        # le determinado numero de segundos dos inputs
    data = input.readframes(int((input.getnframes() / input.getframerate()) * framerate)) 
    # write the extracted data to a new file
    output = wave.open(path + 'somfast1.wav', 'w')
    output.setnchannels(nchannels)
    output.setsampwidth(sampwidth)
    output.setframerate(framerate * 2) # aumentamos a framerate para o som ficar mais rápido.
    output.setnframes(int(len(data) / sampwidth))
    output.writeframes(data)





def somlento(path, audio):

    input = wave.open(audio, "rb") # abre ficheiro


    nchannels = input.getnchannels()
    sampwidth = input.getsampwidth()
    framerate = input.getframerate()


        # Colocamos a posição do ponteiro do ficheiro onde queremos
    input.setpos(int(0))
        # le determinado numero de segundos dos inputs
    data = input.readframes(int((input.getnframes() / input.getframerate()) * framerate)) 
    # escreve os dados extraidos para o novo ficheiro
    output = wave.open(path + 'somslow1.wav', 'w')
    output.setnchannels(nchannels)
    output.setsampwidth(sampwidth)
    output.setframerate(framerate / 4) # diminui frame rate para tornar o som mais lento
    output.setnframes(int(len(data) / sampwidth))
    output.writeframes(data)