import json

# Load questions from JSON file
with open("data/questions.json", "r") as file:
    questions_data = json.load(file)

print("🤖 Welcome to InterviewBot!")

# Choose interview category
print("\nChoose your interview:")
print("1. Java")
print("2. Python")
print("3. DSA")
print("4. DBMS")
print("5. Computer Networks")

choice = input("Enter your choice: ")

categories = {
    "1": "Java",
    "2": "Python",
    "3": "DSA",
    "4": "DBMS",
    "5": "Computer Networks"
}

if choice not in categories:
    print(" Invalid choice!")
    return None

return categories[choice]


def choose_category():  
    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Intermediate")
    print("3. Advanced")

    choice= input("Enter difficulty: ")

    difficulties = {
        "1": "Easy",
        "2": "Intermediate",
        "3": "Advanced"
}

    if choice not in difficulties:
        print("❌ Invalid difficulty!")
        return None

    return difficulties[choice]


def conduct_interview(questions):
    score = 0

    print("\nLet's begin the interview!")
    print("Type 'exit' anytime to end.\n")

    for question in questions:

        print("Bot:", question["question"])

        answer = input("You: ").lower()

        if answer == "exit":
            print("Bot: Interview ended. Goodbye! 👋")
            break

        matched_keywords = 0

        for keyword in question["keywords"]:
            if keyword.lower() in answer:
                matched_keywords += 1

        if matched_keywords >= 2:
            print("Bot: ✅ Good answer!")
            score += 1
        else:
            print("Bot: ⚠️ Your answer needs improvement.")

        print()
    return score


def show_result(category, difficulty, score, total_questions):
    print("--------------------------------")
    print("       INTERVIEW RESULT")
    print("--------------------------------")
    print("Category:", category)
    print("Difficulty:", difficulty)
    print("Score:", score, "/", total_questions)
    print("--------------------------------")


def main():
    print("🤖 Welcome to InterviewBot!")

    category = choose_category()

    if category is None:
        return

    difficulty = choose_difficulty()

    if difficulty is None:
        return

    questions = questions_data[category][difficulty]

    print("\n--------------------------------")
    print("Interview Started")
    print("Category:", category)
    print("Difficulty:", difficulty)
    print("--------------------------------")

    score = conduct_interview(questions)

    show_result(category, difficulty, score, len(questions))


if __name__ == "__main__":
    main()