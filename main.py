import numpy as np
import numpy.random
from PIL import Image
from numpy import asarray
import os
from skimage import io
import skimage
import matplotlib.pyplot as plt
from catboost import CatBoostClassifier



image = io.imread('Logos/bat-logo-preview-400x400.png')

# plotting the original image
i, (im1, im2, im3, im4) = plt.subplots(1, 4, sharey=True)
i.set_figwidth(20)

im1.imshow(image)  #Original image
im2.imshow(image[:, : , 0]) #Red
im3.imshow(image[:, : , 1]) #Green
im4.imshow(image[:, : , 2]) #Blue
i.suptitle('Original & RGB image channels')

oldpwd = os.getcwd()

os.chdir('Logos')

files = os.listdir()

data_x = []

for index in range(100):
    image = io.imread(files[index])

    arr = np.array(image)

    data_x.append(np.reshape(arr, (1,400*400*4))[0])

data_y = numpy.random.randint(0,10,100)
data_y = data_y.astype(int)
print(data_y)

model = CatBoostClassifier(iterations=1500,
                           learning_rate=0.1,
                           depth=2,
                           loss_function='MultiClass')

model.fit(data_x, data_y)