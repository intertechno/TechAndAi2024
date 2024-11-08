import numpy as np
import matplotlib.pyplot as plt

# 1. Alusta NumPy:llä taulukko, jossa on 100 kpl satunnaisia lukuja välillä 1..20.
random_numbers = np.random.randint(1, 21, size=100)
print(random_numbers)

# 2. Laske satunnaisten lukujen keskiarvo.
average = np.mean(random_numbers)

# Tulosta keskiarvo
print("Keskiarvo:", average)

# 3. Laske tilastolliset frekvenssit luvuille.
unique_numbers, counts = np.unique(random_numbers, return_counts=True)
frequencies = dict(zip(unique_numbers, counts))

# Tulosta frekvenssit
print("Frekvenssit:")
for number, count in frequencies.items():
    print(f"Luku {number}: {count} kpl")

# 4. Käytä Matplotlib-kirjastoa tulostaaksesi frekvensseistä pylväskaavion.
plt.bar(frequencies.keys(), frequencies.values(), color='blue')
plt.xlabel('Luku')
plt.ylabel('Frekvenssi')
plt.title('Satunnaislukujen frekvenssit')
plt.show()
