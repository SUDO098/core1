QUESTIONS = [
 "Chest pain?",
 "Breathing difficulty?",
 "High fever?",
 "Dizziness?",
 "Vomiting?"
]

THRESHOLD = {
 'Mild': 20,
 'Severe': 40,
 'Emergency': 60
}

def expertSystem():
    score = 0
    for q in QUESTIONS:
        print(q, "(Y/N)")
        ans = input("> ")
        if ans.lower() == 'y':
            print("Severity (1-10):")
            val = int(input("> "))
            score += val

    print("\nResult:")
    if score >= THRESHOLD['Emergency']:
        print("EMERGENCY! Go to hospital")
    elif score >= THRESHOLD['Severe']:
        print("Severe condition")
    elif score >= THRESHOLD['Mild']:
        print("Mild condition")
    else:
        print("Normal")

expertSystem()