from Question import Question

question_prompts = [
{
	"1": "Laquelle des fonctions suivantes prend une entrée console Python ?",
	"2": "Lequel des éléments suivants doit exécuter un code Python ?",
	"3": "La méthode ajoute de la valeur à la liste à la ?",
	"4": "Lequel des éléments suivants est exécuté dans le navigateur (côté client) ?",
	"5": "Lequel des mots-clés suivants est utilisé pour créer une fonction dans Python ?",
	"6": "Pour déclarer une variable globale en Python, nous utilisons le mot-clé ?"},
{
	"1": ["get()", "input()", "gets()", "scan()"],
	"2": ["TURBO C", "Py Interpreter", "Notepad","IDE"],
	"3":["custom location", "end", "center", "beginning"],
	"4":["perl", "css", "python", "java"],
	"5":["function", "void", "fun", "def"],
	"6":["all", "val", "let", "global"]
}]

questions = [
	Question(question_prompts[0], "input ()"),
	Question(question_prompts[1], "IDE"),
	Question(question_prompts[2], "center"),
	Question(question_prompts[3], "css"),
	Question(question_prompts[4], "def"),
	Question(question_prompts[5], "global"),
]

def run_test(questions):
	score = 0
	for question in questions:
		answer = input(question_prompt)
		if answer ==question.answer:
			score+=1
	print("You got " + str(len(questions)) + " Correct")

run_test(questions)

