import numpy as np
from PIL import Image

def get_avg_color(pixels):
    flt = pixels.flatten()
    flt = flt.reshape(len(flt) // 4, 4) 
    return np.floor_divide(np.sum(flt, 0), flt.shape[0])


image = Image.open("./plut.png")
im = np.asarray(image)
sf = int(input("Enter scale: "))

COLORS = ["cec2ff","b3b3f1","dcb6d5","cf8ba9","b15e6c"]

for row in range(0, im.shape[0] - sf, sf):
    for col in range(0, im.shape[1] - sf, sf):
        sub = im[row:row+sf, col:col + sf]

        colors = get_avg_color(sub)
        colored = np.full((sf, sf, 4), colors)
        im[row:row+sf, col:col + sf] = colored
        

        
        
    


final = Image.fromarray(im)
final.show()


print(im)




