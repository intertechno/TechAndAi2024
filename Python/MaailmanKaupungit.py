import pandas as pd

kaupungit = pd.read_csv("worldcities.csv")

# print(kaupungit[:10])

# print(kaupungit)
# print("---------------")
# print(kaupungit.country)
# print("---------------")
# print(kaupungit[2:5])
# print("---------------")

# kymmenen suurinta kaupunkia
# print(kaupungit[:10].city)
# print("---------------")
# print(kaupungit.nlargest(10, "population").city)


# kaupungit joissa 500K..1M asukasta
print("===============")
for indeksi, rivi in kaupungit.iterrows():
     if rivi["population"] >= 500000 and rivi.population <= 1000000:
         print(rivi.city, rivi.population)

# tapa 2
print("===============")
vaihe1 = kaupungit[kaupungit["population"] >= 500000]
vaihe2 = vaihe1[vaihe1["population"] <= 1000000]
print(vaihe2.sort_values(["population"], ascending=False))
