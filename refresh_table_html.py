import bs4
import requests

#date du lundi pour la semaine a scrapper !!!! semaine de cours obligatoirement !!!! (format mm/jj/aaaa)
date = "10/10/2022"

#eleve selon la personne pour qui on veut recuperer l'emploi du temps (format prenom.nom)
#eleve = "alexandre.tison"
eleve="loic.robin"


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

print(lstJours)
print(lstHoraire)
print(lstCours)
print(lstProf)



"""
path = "C:/Users/loicr/Desktop/EPSI/python/code_perso/edt_no_replace.txt"

f = open(path, "w")

f.close()
"""


html="""<html>
<head>
    <title>Mon super emploi du temps</title>
    <style type='text/css'>
        caption /* Titre du tableau */
        {
           margin: auto; /* Centre le titre du tableau */
           font-family: Arial, Times, 'Times New Roman', serif;
           font-weight: bold;
           font-size: 1.2em;
           color: #009900;
           margin-bottom: 20px; /* Pour éviter que le titre ne soit trop collé au tableau en-dessous */
        }

        table /* Le tableau en lui-même */
        {
           margin: auto; /* Centre le tableau */
           border: 4px outset green; /* Bordure du tableau avec effet 3D (outset) */
           border-collapse: collapse; /* Colle les bordures entre elles */
           width:100%;
        }
        th /* Les cellules d'en-tête */
        {
           background-color: #006600;
           color: white;
           font-size: 1.1em;
           font-family: Arial, 'Arial Black', Times, 'Times New Roman', serif;
           border:1px solid red;
        }

        td /* Les cellules normales */
        {
           font-size:0.8em;
           border: 1px solid black;
           font-family: Verdana, 'Trebuchet MS', Times, 'Times New Roman', serif;
           text-align: center; /* Tous les textes des cellules seront centrés*/
           padding: 5px; /* Petite marge intérieure aux cellules pour éviter que le texte touche les bordures */
           height:25px;
           width:200px;
        }
        td.time
        {
            font-size:1em;
            height:50px;
            width:100px;
        }
    </style>

</head>
<body>
<table>
"""


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
for i in range(0,len(lstCours)-1):
    dic = {}
    dic["Jour"] = lstSemaine[i]
    dic["Cours"] = lstCours[i]
    dic["Horaire"] = lstHoraire[i]
    dic["Prof"] =  lstProf[i]
    lstLesCours.append(dic)

complet = ""
for cours in lstLesCours:
    content = "<td>"+cours["Jour"]+"\n"+cours["Cours"]+"\n"+cours["Horaire"]+"\n"+cours["Prof"]+"</td>"
    complet = complet + content

tab = "<thead><th>EDT</th></thead><tbody><tr>"
fin="</tr></tbody></table></body></html>"

html_complete = html+tab+complet+fin

f = open('EDT.html', 'w')

f.write(html_complete) 
  
f.close() 
