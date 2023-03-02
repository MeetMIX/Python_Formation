import webbrowser
import json
from urllib.request import urlopen

print("Recherchons un ancien site web.")
site = input("taper l'url du site : ")
era = input("Taper l'annee, le mois, le jour comme AAAAMMJJ : ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site,era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print ("trouve cette copie : ", old_site)
    print ("Elle devrait apparaitre dans votre navigateur maintenant...")
    webbrowser.open(old_site)
except:
    print("désolé, pas de copie historique du site demandé")
    