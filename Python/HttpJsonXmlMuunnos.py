# pip install requests
import requests
import xml.etree.ElementTree as ET

käyttäjät = requests.get('https://jsonplaceholder.typicode.com/users').json()
tehtävät = requests.get('https://jsonplaceholder.typicode.com/todos').json()

# for tehtävä in tehtävät:
#     käyttäjä_id = int(tehtävä["userId"])
#     käyttäjä_nimi = käyttäjät[käyttäjä_id - 1]["name"]
#     print(käyttäjä_nimi, tehtävä["title"], käyttäjä_id)

# Luodaan XML:n juurielementti
tehtavat_xml = ET.Element("tehtävät")

# Käydään läpi jokainen tehtävä JSON-datassa
for tehtävä in tehtävät:
    # Hae käyttäjän nimi userId:n perusteella
    käyttäjä_id = int(tehtävä["userId"])
    käyttäjä_nimi = käyttäjät[käyttäjä_id - 1]["name"]
    
    # Luodaan tehtävä-elementti ja sen alaelementit
    tehtava_elem = ET.SubElement(tehtavat_xml, "tehtävä")
    nimi_elem = ET.SubElement(tehtava_elem, "nimi")
    nimi_elem.text = käyttäjä_nimi
    
    otsikko_elem = ET.SubElement(tehtava_elem, "otsikko")
    otsikko_elem.text = tehtävä["title"]

# Muutetaan XML-rakenne tekstimuotoon ja tulostetaan
xml_data = ET.tostring(tehtavat_xml, encoding="unicode")
# print(xml_data)

# Voit myös tallentaa XML:n tiedostoon
tree = ET.ElementTree(tehtavat_xml)
with open("Tehtävät.xml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)

print("XML-tiedosto kirjoitettu.")
