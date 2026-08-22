print(" 🤖 Welcome to the Interview Bot!")
print("Let's get started with some java interview questions.")
print("Type 'exit' at any time to quit the interview.")

questions = [
    "What is the difference between JDK, JRE, and JVM?",
    "Explain the concept of OOP in Java.",
    "What is inheritance in Java and how does it work?",
    "What are the different types of exceptions in Java?",
    "What is an ArrayList in Java and how is it different from an array?",
    "what is the difference between '==' and 'equals()' in Java?",
    "What is the pupose of the 'final' keyword in Java?",
    "What is the diiference between 'abstract' class and 'interface' in Java?"
]

for question in questions:
    print("Bot:" , question)
    answer = input("You:")

    if answer.lower() == 'exit':
        print("Bot: Interview ended. Goodbye! 👋")
        break

    print("Bot: Thank you for your answer!\n")

print("Bot: Thank you for attending the interview!")
