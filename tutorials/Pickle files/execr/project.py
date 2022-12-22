import requests
import pickle

# getting iris data
r = requests.get(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

# storing iris data in txt file for requests
with open("pickle files/execr/iris.txt", 'w+') as file:
    file.write(r.text)

# converting to list of list and dump into pickle
with open("pickle files/execr/iris.txt") as f:
    all = f.readlines()
    ls = [[item] for item in all if item != '\n']
    # print(ls)
    forpickling = open("pickle files/execr/pickling file.pkl", 'wb')
    pickle.dump(ls, forpickling)
    forpickling.close()


# Depickling
my_iris_data = open("pickle files/execr/pickling file.pkl", 'rb')
print("data is depickling form pkl file:", pickle.load(my_iris_data))
