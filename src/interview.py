from src.evaluator import Evaluator


class Interview:

    def __init__(self, category, difficulty, questions):
        self.category = category
        self.difficulty = difficulty
        self.questions = questions
        self.score = 0
        self.evaluator = Evaluator()

    def conduct_interview(self):

        print("\nLet's begin the interview!")
        print("Type 'exit' anytime to end.\n")

        for question in self.questions:

            print("Bot:", question["question"])

            answer = input("You: ")

            if answer.lower() == "exit":
                print("Bot: Interview ended. Goodbye! 👋")
                break

            correct = self.evaluator.evaluate(
                answer,
                question["keywords"]
            )

            if correct:
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