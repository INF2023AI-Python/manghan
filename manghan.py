import random

words = [
    "Apfel", "Banane", "Kirsche", "Orange", "Erdbeere",
    "Hund", "Katze", "Pferd", "Elefant", "Giraffe",
    "Haus", "Auto", "Flugzeug", "Boot", "Fahrrad",
    "Computer", "Smartphone", "Tablet", "Laptop", "Drucker",
    "Buch", "Zeitung", "Schule", "Universitaet", "Lehrer",
    "Musik", "Film", "Kunst", "Sport", "Reisen"
]

pick = words[random.randint(0,len(words))-1].lower()
guess = ""
correct = []
usedLetters = []

while len(usedLetters) < 5:
    guess = str(input("guess your letter:")).lower()
    if guess in pick:
        correct.append(guess)
    else:
        usedLetters.append(guess)
    
    for i,e in enumerate(pick):
        if e in correct:
            print(e,end="")
        else:
            print("_",end="")
    print("\t",usedLetters)
    temp = ""
    for e in correct:
        temp = temp + e
    print(temp, pick)
    if temp == pick:
        print("Gewonnen")
        break
    
if len(usedLetters) >= 5:
    print("verloren",pick)