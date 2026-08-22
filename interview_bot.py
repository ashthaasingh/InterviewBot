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
        {
            "question": "What is Java?",
            "keywords": ["programming", "object", "oriented"]
        },
        {
            "question": "What is OOP?",
            "keywords": ["object", "class", "inheritance"]
        },
        {
            "question": "What is inheritance in Java?",
            "keywords": ["class", "parent", "child", "inherit"]
        },
        {
            "question": "What is an ArrayList?",
            "keywords": ["dynamic", "array", "collection"]
        },
        {
            "question": "What is a constructor?",
            "keywords": ["class", "object", "initialize"]
        }
    ]

elif choice == "2":
    questions = [
        {
            "question": "What is Python?",
            "keywords": ["programming", "language", "interpreted"]
        },
        {
            "question": "What is a list in Python?",
            "keywords": ["ordered", "mutable", "collection"]
        },
        {
            "question": "What is a tuple?",
            "keywords": ["ordered", "immutable", "collection"]
        },
        {
            "question": "What is a dictionary?",
            "keywords": ["key", "value", "pair"]
        },
        {
            "question": "What is OOP in Python?",
            "keywords": ["object", "class", "inheritance"]
        }
    ]

elif choice == "3":
    questions = [
        {
            "question": "What is an array?",
            "keywords": ["elements", "index", "memory"]
        },
        {
            "question": "What is a linked list?",
            "keywords": ["nodes", "pointer", "data"]
        },
        {
            "question": "What is a stack?",
            "keywords": ["lifo", "push", "pop"]
        },
        {
            "question": "What is a queue?",
            "keywords": ["fifo", "enqueue", "dequeue"]
        },
        {
            "question": "What is binary search?",
            "keywords": ["sorted", "divide", "half"]
        }
    ]

elif choice == "4":
    questions = [
        {
            "question": "What is DBMS?",
            "keywords": ["database", "management", "system"]
        },
        {
            "question": "What is a primary key?",
            "keywords": ["unique", "identify", "record"]
        },
        {
            "question": "What is a foreign key?",
            "keywords": ["table", "reference", "primary"]
        },
        {
            "question": "What is normalization?",
            "keywords": ["redundancy", "data", "tables"]
        },
        {
            "question": "What is SQL?",
            "keywords": ["query", "database", "language"]
        }
    ]

elif choice == "5":
    questions = [
        {
            "question": "What is a computer network?",
            "keywords": ["devices", "communication", "network"]
        },
        {
            "question": "What is an IP address?",
            "keywords": ["address", "device", "network"]
        },
        {
            "question": "What is the difference between TCP and UDP?",
            "keywords": ["connection", "reliable", "fast"]
        },
        {
            "question": "What is DNS?",
            "keywords": ["domain", "name", "ip"]
        },
        {
            "question": "What is HTTP?",
            "keywords": ["protocol", "web", "communication"]
        }
    ]

else:
    print(" Invalid choice!")
    exit()

print("\nLet's begin the interview!")
print("Type 'exit' anytime to end.\n")

score = 0

for question in questions:

    print("Bot:", question["question"])

    answer = input("You: ").lower()

    if answer == "exit":
        print("Bot: Interview ended. Goodbye! 👋")
        break

    matched_keywords = 0

    for keyword in question["keywords"]:
        if keyword in answer:
            matched_keywords += 1

    if matched_keywords >= 2:
        print("Bot:  Good answer!")
        score += 1
    else:
        print("Bot: ⚠️ Your answer needs improvement.")

    print()

print("--------------------------------")
print("       INTERVIEW RESULT")
print("--------------------------------")
print("Score:", score, "/", len(questions))
print("--------------------------------")