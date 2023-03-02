import webbrowser
import requests

print("Recherchons un ancien site web.")
site = input("Taper l'URL du site : ")
era = input("Taper l'année, le mois, le jour, formaté comme ceci AAAAMMJJ : ")
url = "http://archive.org/wayback/available?url=%s&%timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print ("Trouvé dasn cette copie : ", old_site)
    print("Elle devrait apparaitre dans votre naviguateur maintenant.")
    webbrowser.open(old_site)
except:
    print("Désolé , pas d'archive de ce site web")