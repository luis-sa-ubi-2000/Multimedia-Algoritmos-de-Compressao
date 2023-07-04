#Not Working

from PIL import Image
import cv2

img = Image.open("img.jpg")

# Creating a copy for traversing original values and updating in new matrix
img2 = img.copy()
for i in range(2,258):
    for j in range(2,258):
        
        # for a 5x5 window sliding
        vector_sum = 0
        n=0
        # Fetch all neighbours for middle element of a 5x5 matrix
        for k in range(i-2,i+3):
            for l in range(j-2,j+3):
                n+=1
                #Calculate sum of 
                vector_sum+= img[k,l].astype(int)
        #Finding average of neigbours, excluding centre element
        vector_mean = (vector_sum - img[i,j]) / (n-1)
        img2[i,j] = vector_mean

cv2.imwrite('average_neighbor_operation.jpg', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()