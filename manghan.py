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
wrongLetters = []

while len(wrongLetters) < 5:
    guess = str(input("guess your letter:")).lower()
    if guess in pick and guess not in correct:
        correct.append(guess)
    elif guess not in pick and guess not in wrongLetters:
        wrongLetters.append(guess)
    
    temp = ""
    for e in pick:
        if e in correct:
            temp = temp +e
            print(e,end="")
        else:
            print("_",end="")
    print("\t",wrongLetters)
   
    print(temp, pick)
    if temp == pick:
        print("Gewonnen")
        break
    
if len(wrongLetters) >= 5:
    print("verloren",pick)