import bs4
import requests

#url selon le connecté sur l'edt my learning box
url = "https://mylearningbox.reseau-cd.fr/revigs/WebPsDyn.aspx?action=posEDTBEECOME&serverID=C&Tel=loic.robin&date=2022-01-09&hashurl=7ae0bcb53e64aed5d6672096bc3bdce6e05854a4671d225036b157148cbefcc08e8ba162718ff27bc1f1d7ed25680fbe761d366d06c4cf259b29c1070a80aadf/"
reponse = requests.get(url)

soup = bs4.BeautifulSoup(reponse.text, features='html.parser')

#print(soup.text)

path = "C:/Users/loicr/Desktop/EPSI/python/code_perso/edt_no_replace.txt"

f = open(path, "w")

"""
for td in soup.find_all('td'):
    f.write(td.text+"\n")
    print(td.text.replace(":", " "))
"""
lst = []
for td in soup.find_all('td'):
    for fin in str(td.text).splitlines():
        lst.append(fin)
        f.write(fin+"\n\n")

jours = list(lst[-5:])
print(jours)
cours = list(lst[10:-5])


dic = {}
lstDic = []
for i in range(0,len(jours)):
    for j in range(0,len(cours)):
        dic["jour"] = jours[i]
        dic["cour"] = cours[j]
        lstDic.append(dic)

print(lstDic)

f.close()

"""
for div in soup.find_all('div'):
    print(div)
"""

