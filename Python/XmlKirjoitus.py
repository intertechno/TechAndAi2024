import xml.etree.ElementTree as ET

# Luodaan XML:n juurielementti
tehtavat = ET.Element("tehtävät")

# Luodaan tehtävä-elementti ja sen alaelementit
tehtava = ET.SubElement(tehtavat, "tehtävä")
nimi = ET.SubElement(tehtava, "nimi")
nimi.text = "Käyttäjän nimi"  # Lisätään nimi-elementin teksti

otsikko = ET.SubElement(tehtava, "otsikko")
otsikko.text = "Tehtävän otsikko"  # Lisätään otsikko-elementin teksti

# Muutetaan rakenne tekstiksi ja tulostetaan se
xml_data = ET.tostring(tehtavat, encoding="unicode")
print(xml_data)
