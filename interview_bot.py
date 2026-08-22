print("🤖 Welcome to InterviewBot!")
print("Choose your interview:")
print("1. Java")
print("2. Python")
print("3. DSA")
print("4. DBMS")
print("5. Computer Networks")

choice = input("Enter your choice: ")

if choice == "1":
    questions = [
        "What is Java?",
        "What is OOP?",
        "What is inheritance in Java?",
        "What is the difference between == and equals()?",
        "What is an ArrayList?"
    ]

elif choice == "2":
    questions = [
        "What is Python?",
        "What is a list in Python?",
        "What is a tuple?",
        "What is a dictionary?",
        "What is OOP in Python?"
    ]

elif choice == "3":
    questions = [
        "What is an array?",
        "What is a linked list?",
        "What is a stack?",
        "What is a queue?",
        "What is binary search?"
    ]

elif choice == "4":
    questions = [
        "What is DBMS?",
        "What is a primary key?",
        "What is a foreign key?",
        "What is normalization?",
        "What is SQL?"
    ]

elif choice == "5":
    questions = [
        "What is a computer network?",
        "What is an IP address?",
        "What is the difference between TCP and UDP?",
        "What is DNS?",
        "What is HTTP?"
    ]

else:
    print("❌ Invalid choice!")
    exit()

print("\nLet's begin the interview!")
print("Type 'exit' anytime to end.\n")

for question in questions:

    print("Bot:", question)

    answer = input("You: ")

    if answer.lower() == "exit":
        print("Bot: Interview ended. Goodbye! 👋")
        break

    print("Bot: Thank you for your answer!\n")

print("Bot: Interview completed! 🎉")