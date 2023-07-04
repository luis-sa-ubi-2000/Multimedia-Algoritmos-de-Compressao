import cv2

video_name = "video.mp4" # or any other extension like .avi etc

#my_clip = mp.VideoFileClip(video_name)
#audio = my_clip.audio.write_audiofile("my_result.mp3")

vidcap = cv2.VideoCapture(video_name)
frames = int(vidcap.get(cv2.CAP_PROP_FPS))

success,image = vidcap.read()
height, width, size = image.shape
size = (width,height)
i = 0
img_array = []

print("image: ", image)
print("end image")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #Retorna uma matriz

print("Gray: ", gray)
print("end")
while success:
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  img_array.append(gray) 
  success,image = vidcap.read()
  img = img_array[i]
  i += 1

print('Read a number of %d frames!' % i)

out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), frames, (width, height), 0)
 
for i in range(len(img_array)):
  out.write(img_array[i])

print("\nThe total number of frames in this video is ", frames)

out.release()

