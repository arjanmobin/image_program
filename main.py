import sys
import numpy as np
from PIL import Image
from tqdm import tqdm
import random

def get_avg_color(pixels):
    flt = pixels.flatten()
    flt = flt.reshape(len(flt) // 4, 4) 
    return np.floor_divide(np.sum(flt, 0), flt.shape[0])

def closest_color(pixel):
    min_color = None
    min_dist = 9999999999
    for rgb in RGBs:
        dist = np.linalg.norm(pixel[:3] - rgb)
        if dist < min_dist:
            min_dist = dist
            min_color = rgb
    
    return (min_color[0], min_color[1], min_color[2], 255)

def rand_colors(qty):
    for _ in range(qty):
        RGBs.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


        

    
color_cache = {}

image = Image.open("./plut.png")
im = np.asarray(image)
sf = int(input("Enter scale: "))

# COLORS = ["cec2ff","b3b3f1","dcb6d5","cf8ba9","b15e6c",  "a5503e", "a5843e", "93a53e", "60a53e", "3ea550", "3ea584"]
COLORS = ["000000", "ffffff", "474a4f", "ff0000", "00ff00", "0000ff"]
RGBs = [tuple(int(h[i:i+2], 16) for i in (0, 2, 4)) for h in COLORS]

rand_colors(1000)
cnt = 0
for row in tqdm(range(0, im.shape[0] - sf + 1, sf)):
    for col in range(0, im.shape[1] - sf + 1, sf):
        sub = im[row:row+sf, col:col + sf]
        cnt += 1

        colors = tuple(get_avg_color(sub))

        if colors not in color_cache:
            color_cache[colors] = closest_color(np.asarray(colors))
        
        colored = np.full((sf, sf, 4), color_cache[colors])
        im[row:row+sf, col:col + sf] = colored
        


        
        
    


final = Image.fromarray(im)
print(len(color_cache), cnt)
final.show()