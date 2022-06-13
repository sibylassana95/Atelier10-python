str_fumeur = input ("Fumeur (oui / non) :")
age_fumeur = int (input ("Age du fumeur :"))
if (str_fumeur == "oui"):
 facteur_f = 2
else :
 facteur_f = 0
if (age_fumeur > 60):
 facteur_a = 1
else :
 facteur_a = 0
niveau_de_risque = facteur_f + facteur_a
if niveau_de_risque == 0:
 print ("Le risque est nul !")
if niveau_de_risque != 0:
 print ("Il y a un risque !")
if niveau_de_risque >= 3:
 print ("Risque élevé !")
