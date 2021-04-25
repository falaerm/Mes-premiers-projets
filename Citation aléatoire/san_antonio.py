print("Yo")
import random
import json

quotes= ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "Lourd est mon crime d'avoir à ce point tourmenté ton coeur"]

characters=["parn", "Onizuka", "K", "Guts", "Momo"]

#read values from a Json file
def read_value_from_json():
	values = []

	with open('character.json') as f:
	  data = json.load(f)
	  for entry in data:
		  values.append(entry['character'])
	  return values



def get_random_item(my_list):
	rand_numb = random.randint(0, len(my_list) - 1)
	
	# get a random number
	item = my_list[rand_numb]
	return item

def random_character():
	all_values = read_value_from_json
	return get_random_item(all_values)

def capitalize(words):
	for word in words:
		word.capitalize()

def message(character, quote):
	capitalize(character)
	capitalize(quote)
	return"{} a dit : {}".format(character, quote)

user_answer=input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

	
while user_answer != "B":
  print(message(get_random_item(characters), get_random_item(quotes)))
  user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

