import pandas as pd

countries = pd.read_csv("countries.csv")
print(countries)
countries["density"] = countries["population"]/countries["area"]
print(countries)
# countries.drop(index=2, axis=0, inplace=True)
# print(countries)
countries.drop(columns="area", axis=1, inplace=True)
print(countries)