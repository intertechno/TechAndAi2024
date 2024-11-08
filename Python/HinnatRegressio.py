import pandas as pd
from sklearn.linear_model import LinearRegression
# from sklearn import linear_model

hinnat = pd.read_csv("Hinnat.csv")
print(hinnat)

malli = LinearRegression()
vuodet = hinnat.drop("hinta", axis="columns")
# print(vuodet)
malli.fit(vuodet, hinnat.hinta)
print("Regressiomalli luotu.")

ennuste = malli.predict([[2020]])
print("Vuoden 2020 hintaennuste:", ennuste)

ennuste = malli.predict([[2021]])
print("Vuoden 2021 hintaennuste:", ennuste)

ennuste = malli.predict([[2022]])
print("Vuoden 2022 hintaennuste:", ennuste)
