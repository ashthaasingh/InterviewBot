from src.questions import load_questions
from src.interview import Interview


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
        print(" Invalid choice!")
        return None

    return categories[choice]


def choose_difficulty():

    print("\nChoose difficulty:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    choice = input("Enter difficulty: ")

    difficulties = {
        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced"
    }

    if choice not in difficulties:
        print("❌ Invalid difficulty!")
        return None

    return difficulties[choice]


def main():

    print("================================")
    print("       🤖 InterviewBot")
    print("================================")

    # Load questions
    questions_data = load_questions()

    # Choose category
    category = choose_category()

    if category is None:
        return

    # Choose difficulty
    difficulty = choose_difficulty()

    if difficulty is None:
        return

    # Get questions
    questions = questions_data[category][difficulty]

    # Create interview
    interview = Interview(
        category,
        difficulty,
        questions
    )

    # Start interview
    print("\n--------------------------------")
    print("Interview Started")
    print("Category:", category)
    print("Difficulty:", difficulty)
    print("--------------------------------")

    interview.conduct_interview()

    # Show result
    interview.show_result()


if __name__ == "__main__":
    main()