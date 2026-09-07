from src.evaluator import Evaluator


class Interview:

    def __init__(self, category, difficulty, questions):

        self.category = category
        self.difficulty = difficulty
        self.questions_data = questions

        self.questions = self.questions_data[difficulty]

        self.score = 0
        self.total_score = 0
        self.attempted = 0

        self.evaluator = Evaluator()

    def conduct_interview(self):

        print("\nLet's begin the interview!")
        print("Type 'exit' anytime to end.\n")

        current_difficulty = self.difficulty

        questions = self.questions_data[current_difficulty]

        for question_number, question in enumerate(questions, start=1):

            print("--------------------------------")
            print(f"Question {question_number}")
            print(f"Difficulty: {current_difficulty}")
            print("--------------------------------")

            print("Bot:", question["question"])

            answer = input("You: ")

            if answer.lower() == "exit":
                print("\nBot: Interview ended. Goodbye! 👋")
                break

            result = self.evaluator.evaluate(
                answer,
                question["keywords"]
            )

            self.attempted += 1
            self.total_score += result["score"]

            if result["correct"]:
                print("\nBot: ✅ Good answer!")
            else:
                print("\nBot: ⚠️ Your answer needs improvement.")

            print("Bot:", result["feedback"])

            print(
                "Matched keywords:",
                len(result["matched_keywords"]),
                "/",
                len(question["keywords"])
            )

            print("Score:", result["score"], "/ 10")
            print()

    def show_result(self):

        print("--------------------------------")
        print("       INTERVIEW RESULT")
        print("--------------------------------")

        print("Category:", self.category)
        print("Difficulty:", self.difficulty)
        print("Questions:", len(self.questions))
        print("Attempted:", self.attempted)

        if self.attempted > 0:
            average_score = self.total_score / self.attempted
        else:
            average_score = 0

        print("Total Score:", self.total_score)
        print("Average Score:", round(average_score, 2), "/ 10")

        # Determine performance
        if average_score >= 9:
            performance = "Excellent 🌟"
            recommendation = "You have a strong understanding of the concepts."

        elif average_score >= 7:
            performance = "Good 👍"
            recommendation = "Good performance. Practice advanced concepts to improve further."

        elif average_score >= 5:
            performance = "Average 🙂"
            recommendation = "Review the important concepts and practice more questions."

        else:
            performance = "Needs Improvement ⚠️"
            recommendation = "Focus on the fundamentals and practice regularly."

        print("Performance:", performance)

        print("\nRecommendation:")
        print(recommendation)

        print("--------------------------------")