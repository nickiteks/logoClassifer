import pandas as pd

dataframe = pd.read_csv('data/dataset_2.csv', names=['label', 'style', 'noice', 'place'])

print(dataframe.describe())

dataframe = dataframe.dropna(axis= 0)

print(dataframe.describe())

print(dataframe.size)

market_labels = dataframe.label.unique()

label = dataframe[dataframe.label == market_labels[0]]

print(label['style'].mean())

dataframe_new = pd.DataFrame(columns=dataframe.columns)

for name_img in market_labels:
    data = [name_img]
    for column in ['style', 'noice', 'place']:
        data.append(int(dataframe[dataframe['label'] == name_img][column].mean()))
    dataframe_new.loc[len(dataframe_new)] = data

print(dataframe_new)
dataframe_new.to_csv('data/preprocess_data.csv', index=False)
