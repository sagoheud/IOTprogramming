import pandas as pd

titanic = pd.read_csv("titanic.csv")
# print(titanic)
# print(titanic["Age"])

data = {'Name':['Kim','Park','Lee','Choi'],
        'Age':[20,23,21,26]}

df = pd.DataFrame(data)
print(df) 