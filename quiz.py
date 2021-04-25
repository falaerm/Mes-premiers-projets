import json
import tkinter
from tkinter import *
import random
with open('.data.json', encoding="utf8") as f: donnees = json.load(f)
questions = [valeur for valeur in donnees[0].values()]
choix_reponse = [valeur for valeur in donnees[1].values()]
reponses = [1,1,1,1,3,3]
reponse_utilisateur = []
indexes = []
def generer (): 
	global indexes
while(len(indexes) < 5):
x = random.randint(0,9)
	if x in indexes:
	continue
	else:
	indexes.append(x)
def montrer_resultat(score):
lblQuestion.destroy()
reponse_1.destroy()
reponse_2.destroy()
reponse_3.destroy()
reponse_4.destroy()
label_image = label(root, background = "#ffffff", border = 0)
label_image.pack(pady =(50,30))
label_resultat_text = Label(root, font = ("Consoloas", 20), background = "#ffffff",)
	if score >=20:
	image = PhotoImage(file = "great.png")
	label_image.configure(image = image)
	label_resultat_text.configure(text="Vous êtes excellent !!")
elif (score >= 10 and score < 20):
	image = PhotoImage (file ="ok.png")
	label_image.configure(image = image)
	label_image.image = image
	label_resultat_text.configure(text ="vous pouvez faire mieux!!")
else:
	image = PhotoImage(file = "bad.png")
	label_image.configure(image = image)
	label_image.image = image
	label_resultat_text.configure(text ="vous devez faire plus d'effort !!")
	def calculer():
		global indexes, reponse_utilisateur, reponses
		x = 0
		score = 0
		for i in indexes:
			if reponse_utilisateur[x] == reponses [i]:
				score = score + 5
				x += 1
				print(score)
				montrer_resultat(score)
				ques = 1
				def selected():
					global radiovar, reponse_utilisateur
					global lblQuestion, reponse_1, reponse_2, reponse_3, reponse_4
					global ques
					x = radiovar.get()
					reponse_utilisateur.append(x)
					radiovar.set(-1)
			if ques < 5:
				lblQuestion.config(text = questions[indexes[ques]])
				response_1['text'] = choix_reponse[indexes[ques]][0]
				response_2['text'] = choix_reponse[indexes[ques]][1]
				response_3['text'] = choix_reponse[indexes[ques]][2]
				response_4['text'] = choix_reponse[indexes[ques]][3]
				ques += 1
			else:
				calculer()
				commencer_quizz():
				global lblQuestion, reponse_1,reponse_2, reponse_3, response_4
				lblQuestion = Label (root, text = questions[indexes[0]], font = ("Consolas", 16), width = 500, justify = "center", wraplength = 400, background = '#ffffff", )'
				lblQuestion.pack(pady = (100,30))
				global radiovar
				radiovar = IntVar()
				radiovar.set(-1)
				reponse_1 = Radiobutton(root, text = choix_reponse[indexes[0]][0], font = ("Times", 12), value = 0, variable = radiovar, command = selected, background = "#ffffff", )
				reponse_1.pack(pady = 5)
				reponse_2 = Radiobutton((root, text = choix_reponse[indexes[0]][1], font = ("Times", 12), value = 1, variable = radiovar, command = selected, background = "#ffffff", )
				reponse_2.pack(pady = 5)
				reponse_3 = 


