import json

# Load questions from JSON file
with open("data/questions.json", "r") as file:
    questions_data = json.load(file)


class Interview:

    def __init__(self, category, difficulty, questions):
        self.category = category
        self.difficulty = difficulty
        self.questions = questions
        self.score = 0

    def conduct_interview(self):
        print("\nLet's begin the interview!")
        print("Type 'exit' anytime to end.\n")

        for question in self.questions:

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
                self.score += 1
            else:
                print("Bot: ⚠️ Your answer needs improvement.")

            print()

    def show_result(self):
        print("--------------------------------")
        print("       INTERVIEW RESULT")
        print("--------------------------------")
        print("Category:", self.category)
        print("Difficulty:", self.difficulty)
        print("Score:", self.score, "/", len(self.questions))
        print("--------------------------------")


def choose_category():

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
        print("❌ Invalid choice!")
        return None

    return categories[choice]


def choose_difficulty():

    print("\nChoose difficulty:")
    print("1. Easy")
    print("2. Intermediate")
    print("3. Advanced")

    choice = input("Enter difficulty: ")

    difficulties = {
        "1": "Easy",
        "2": "Intermediate",
        "3": "Advanced"
    }

    if choice not in difficulties:
        print(" Invalid difficulty!")
        return None

    return difficulties[choice]


def main():

    print("🤖 Welcome to InterviewBot!")

    category = choose_category()

    if category is None:
        return

    difficulty = choose_difficulty()

    if difficulty is None:
        return

    questions = questions_data[category][difficulty]

    interview = Interview(
        category,
        difficulty,
        questions
    )

    print("\n--------------------------------")
    print("Interview Started")
    print("Category:", category)
    print("Difficulty:", difficulty)
    print("--------------------------------")

    interview.conduct_interview()

    interview.show_result()


if __name__ == "__main__":
    main()