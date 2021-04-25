import os

with open ('fichier.txt', 'w') as f:
    f.write("Lourd est mon crime d'avoir à ce point tourmenté ton coeur, La défaite est dans la fuite, point dans la retraite. Savoir se retirer au bon moment fait aussi parti du chemin qui mène à la victoire")
with open ('fichier.txt', 'r') as f:
	print(f.read())
