from PIL import Image

import numpy as np
im = Image.open('inamo.png')
im2arr = np.array(im) # im2arr.shape: height x width x channel
arr2im = Image.fromarray(im2arr)
for ele in im2arr:
    print(ele)
