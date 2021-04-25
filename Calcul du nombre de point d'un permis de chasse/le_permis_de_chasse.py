poule = float(input("insérer le nombre de poule: "))
chien = float(input("insérer le nombre de chien: ")) * 3
vache = float(input("insérer le nombre de vache: ")) * 5
humain = float(input("insérer le nombre de humain: ")) * 10
points_retirés =  int(poule + chien + vache + humain)
permis = 100 - (poule + chien + vache + humain)
print (permis)
print("le nombre de points restants sur le permis de chasse est de ", permis)
if permis <= 0:
	print ("Vous devez repayer ", points_retirés - 99, " permis")
  