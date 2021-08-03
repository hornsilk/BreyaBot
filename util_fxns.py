import numpy as np

def areImgsSimilar(img1, img2, cutoff=10000):
    
    pixel_distance = np.sqrt(sum(np.square(img1.ravel() - img2.ravel()))) 

    # print(pixel_distance)

    if pixel_distance < cutoff:
        return True
    else:
        return False
