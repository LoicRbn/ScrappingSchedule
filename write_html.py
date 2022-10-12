import bs4
import requests

#date du lundi pour la semaine a scrapper !!!! semaine de cours obligatoirement !!!! (format mm/jj/aaaa)
date = "10/10/2022"

#eleve selon la personne pour qui on veut recuperer l'emploi du temps (format prenom.nom)
eleve = "loic.robin"
#eleve="loic.robin"


#url selon l'edt my learning box a recuperer
url = "https://mylearningbox.reseau-cd.fr/revigs/WebPsDyn.aspx?action=posEDTBEECOME&serverID=C&Tel="+eleve+"&date="+date
print("parsing ... : ", url)
reponse = requests.get(url)

soup = bs4.BeautifulSoup(reponse.text, features='html.parser')

lstJours = []
for td in soup.find_all('div', {"class": "Jour"}):
    for fin in str(td.text).splitlines():
        lstJours.append(fin)
lstJours = list(lstJours[0:5])

lstCours = []
for td in soup.find_all('td', {"class": "TCase"}):
    for fin in str(td.text).splitlines():
        lstCours.append(fin)

lstHoraire = []
for td in soup.find_all('td', {"class": "TChdeb"}):
    for fin in str(td.text).splitlines():
        lstHoraire.append(fin)

lstProf = []
for td in soup.find_all('td', {"class": "TCProf"}):
    for fin in str(td.text).splitlines():
        lstProf.append(fin)


#print(lstJours)


lstSep = []
for i in range(0,len(lstHoraire)):
    if i+1 < len(lstHoraire):
        if lstHoraire[i+1][8:-3] in ("10","11","12"): #("08","09","10","11","12")
            lstSep.append(i)

    elif i+1 == len(lstHoraire):
        lstSep.append(i)

#print(lstSep)

lstSemaine = []
for j in range(0,len(lstCours)):
    if 0 <= j <= lstSep[0]:
        lstSemaine.append(lstJours[0])
    if lstSep[0] <= j < lstSep[1]:
        lstSemaine.append(lstJours[1])
    if lstSep[1] <= j < lstSep[2]:
        lstSemaine.append(lstJours[2])
    if lstSep[2] <= j < lstSep[3]:
        lstSemaine.append(lstJours[3])
    if lstSep[3] <= j < lstSep[4]:
        lstSemaine.append(lstJours[4])
    
#print(lstSemaine)
    

lstLesCours = []
for i in range(0,len(lstCours)):
    dic = {}
    dic["Jour"] = lstSemaine[i]
    dic["Cours"] = lstCours[i]
    dic["Horaire"] = lstHoraire[i]
    dic["Prof"] =  lstProf[i]
    lstLesCours.append(dic)

#print(lstLesCours)

path = "edt2.txt"
f = open(path, "w", encoding="utf-8")

for cours in lstLesCours:
    print("Jour : ", cours["Jour"])
    print("Cours : ", cours["Cours"])
    print("Horaire : ", cours["Horaire"])
    print("Prof : ", cours["Prof"])
    print("\n")
    f.write("Jour : "+ cours["Jour"]+"\n")
    f.write("Cours : "+ cours["Cours"]+"\n")
    f.write("Horaire : "+ cours["Horaire"]+"\n")
    f.write("Prof : "+ cours["Prof"]+"\n")
    f.write("\n")
print("Fichier ecrit avec succes")

f.close()