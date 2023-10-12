questions = {
    "Hva er hovedstaten i Norge? ": "Oslo",
    "Hva er hovedstaten i Danmark? ": "København",
    "Hva er hovedstaten i Sverige? ": "Stockholm",
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)
    
    if user_answer.lower() == answer.lower():
        print("Riktig!")
        score += 1
    else:
        print("Feil.")
        
print("Du fikk", score, "av", len(questions))
