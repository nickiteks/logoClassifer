import numpy as np
from xgboost import XGBClassifier
from skimage import io

bst = XGBClassifier(n_estimators=50, max_depth=10, learning_rate=0.01, objective='multi:softprob')
bst.load_model("xgBoostModel.json")

data_x = []

image = io.imread('Dataset_1/50.jpg')

arr = np.array(image)
data_x.append(np.reshape(arr, (1, 400 * 400 * 3))[0])

y_pred = bst.predict(data_x)

print(y_pred)