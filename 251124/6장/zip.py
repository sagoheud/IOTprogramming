questions = ["name","quest","color"]
answers = ["Kim","Python","blue"]

for q,a in zip(questions,answers):
    print(f"what is your {q}? It is {a}.")

print("questions' index:", questions.index("color"))
print("questions' index:", questions.index("hobby"))