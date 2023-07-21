import numpy as np
import numpy.random
from PIL import Image
from numpy import asarray
import os
from skimage import io
import skimage
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

# image = io.imread('Dataset_1/45.jpg')
#
# # plotting the original image
# i, (im1, im2, im3, im4) = plt.subplots(1, 4, sharey=True)
# i.set_figwidth(20)
#
# im1.imshow(image)  # Original image
# im2.imshow(image[:, :, 0])  # Red
# im3.imshow(image[:, :, 1])  # Green
# im4.imshow(image[:, :, 2])  # Blue
# i.suptitle('Original & RGB image channels')

oldpwd = os.getcwd()

os.chdir('Dataset_1')

files = os.listdir()

data_x = []

#формирование x
for index in range(100):
    image = io.imread(files[index])

    arr = np.array(image)
    data_x.append(np.reshape(arr, (1, 400 * 400 * 3))[0])

os.chdir(oldpwd)

# формирование y
data_y = numpy.random.randint(0, 10, 100)
data_y = data_y.astype(int)
print(data_y)

X_train, X_test, y_train, y_test = train_test_split(data_x, data_y, test_size=0.25)

bst = XGBClassifier(n_estimators=50, max_depth=10, learning_rate=0.01, objective='multi:softprob')
bst.fit(X_train, y_train)

y_pred = bst.predict(X_test)
predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))