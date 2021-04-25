import os


with open ('fichier3.txt', 'a',-1, None, None, '\n') as f:
	mot = input("insérer un mot: ")
	mot2 = str(len(mot))
	mot3 = ["blabla", "parn", "eikishi"]
	mot4 = mot3.append(input("insérer un mot: "))
	f.write(mot + mot2 + str(mot3))
	
	print (len(mot))

