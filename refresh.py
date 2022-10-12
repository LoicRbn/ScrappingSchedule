import bs4
import requests

#date du lundi pour la semaine a scrapper !!!! semaine de cours obligatoirement !!!! (format mm/jj/aaaa)
date = "02/14/2022"

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
lstJours = lstJours[0:5]

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

dicoCours = {}


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

corps = ""

fin="</table></body>"

html_complete = html+corps+fin

f = open('EDT.html', 'w') 

f.write(html_complete) 
  
f.close() 
