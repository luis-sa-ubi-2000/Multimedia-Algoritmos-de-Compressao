import cv2
import numpy as np
from PIL import Image
from Video.baw import black_white
from tqdm import tqdm

def vid2gray(path, vid):
  video_name = vid # or any other extension like .avi etc

  vidcap = cv2.VideoCapture(video_name)
  frames = int(vidcap.get(cv2.CAP_PROP_FPS)) # bibliotecas mais otimizadas video

  success,image = vidcap.read()
  height, width, size = image.shape
  size = (width,height)
  img_array = []
  gray_array = []
  i = 0
  imgdata = Image.fromarray(image) #Ajuda para descobrir a tupla size

  while success:
    img_array.append(image)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #Retorna uma matriz
    success,image = vidcap.read()
    i += 1
    #print(i)

  print('Read a number of %d frames!' % i)
  s = 0
  for image in tqdm(img_array):
    imgdata = Image.fromarray(image)
    gray = black_white(imgdata, imgdata.size)
    gray_array.append(gray)
    s += 1
    #print(s)

  out = cv2.VideoWriter(path + 'GrayscaleVid.avi', cv2.VideoWriter_fourcc(*'DIVX'), frames, (width, height), 0)
  
  for g in  range(len(gray_array)):
    out.write(gray_array[g])

  print("\nThe total number of frames in this video is ", frames)

  out.release()