print("Anna merkkijono jota käsitellään:")
syöte = input()

print("Syötit: " + syöte)

# Tulosta merkkijonon pituus ruudulle
print(len(syöte))

# Tulosta merkkijono kokonaan isoin kirjaimin (all caps)
print(syöte.upper())

# Tulosta merkkijono kolmannesta merkistä eteenpäin
print(syöte[2:])

# Tulosta merkkijono viidenteen merkkiin saakka
print(syöte[:5])

# Tulosta merkkijonon joka toinen kirjain
print(syöte[::2])

# Vertaile, onko merkkijono sama myös väärinpäin, eli palindromi
väärinpäin = syöte[::-1]
print(väärinpäin)
on_palindromi = syöte == väärinpäin
# if on_palindromi:
#     print("Merkkijono on palindromi!")
# else:
#     print("Merkkijono ei ole palindromi.")

print("Onko merkkijono palindromi?", on_palindromi)
