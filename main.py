import os

# Global variables
users_file = "users.txt"
scores_file = "scores.txt"
user_data = {}

# Quiz questions
quizzes = {
    "Python": {
        1: ["What is the output of `print(2 ** 3)`?", "6", "8", "9", "10", "2"],
        2: ["Which keyword is used to define a function in Python?", "func", "define", "def", "lambda", "3"],
        3: ["What does `len()` function do?", "Returns size", "Adds elements", "Deletes elements", "Checks type", "1"],
        4: ["Which of these is a mutable data type?", "Tuple", "String", "List", "Integer", "3"],
        5: ["How do you start a loop in Python?", "loop:", "while:", "for each", "iterate:", "2"],
    },
    "DSA": {
        1: ["What is the time complexity of binary search?", "O(n)", "O(log n)", "O(n^2)", "O(1)", "2"],
        2: ["Which data structure is used in BFS?", "Stack", "Queue", "Deque", "Priority Queue", "2"],
        3: ["What is the best case time complexity of quicksort?", "O(n)", "O(n^2)", "O(log n)", "O(n log n)", "4"],
        4: ["What is a full binary tree?", "Each node has at most two children", "All levels are completely filled",
            "Nodes are either full or half", "None of the above", "2"],
        5: ["What is the in-order traversal of a binary tree?", "Root, Left, Right", "Left, Root, Right",
            "Right, Root, Left", "None of the above", "2"],
    },
    "DBMS": {
        1: ["Which SQL command is used to retrieve data?", "SELECT", "UPDATE", "DELETE", "INSERT", "1"],
        2: ["What does ACID stand for in DBMS?", "Atomicity, Consistency, Isolation, Durability",
            "Accuracy, Clarity, Integrity, Durability", "Access, Consistency, Independence, Durability",
            "None of the above", "1"],
        3: ["What is a primary key?", "A unique identifier for a table row", "A column used for sorting",
            "A foreign key reference", "None of the above", "1"],
        4: ["Which normal form removes partial dependencies?", "1NF", "2NF", "3NF", "BCNF", "2"],
        5: ["What is a foreign key?", "A key used to sort tables", "A key used to connect tables",
            "A unique identifier", "None of the above", "2"],
    },
}


# Initialize data files
def initialize_files():
    if not os.path.exists(users_file):
        with open(users_file, "w") as f:
            f.write("")
    if not os.path.exists(scores_file):
        with open(scores_file, "w") as f:
            f.write("")


def register_user():
    """Register a new user."""
    print("\n--- Registration ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(users_file, "r") as f:
        users = f.readlines()
    for user in users:
        saved_username, _ = user.strip().split("|")
        if saved_username == username:
            print("Username already exists. Try logging in.")
            return None

    with open(users_file, "a") as f:
        f.write(f"{username}|{password}\n")
    print("Registration successful!")
    return username


def login_user():
    """Login an existing user."""
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(users_file, "r") as f:
        users = f.readlines()
    for user in users:
        saved_username, saved_password = user.strip().split("|")
        if username == saved_username and password == saved_password:
            print("Login successful!")
            return username

    print("Invalid username or password. Try again.")
    return None


def attempt_quiz(username, subject):
    """Allow the user to attempt a quiz."""
    print(f"\n--- {subject} Quiz ---")
    questions = quizzes.get(subject)
    if not questions:
        print("No questions available for this subject.")
        return

    score = 0
    for q_id, question in questions.items():
        print(f"\nQ{q_id}: {question[0]}")
        print(f"1. {question[1]}  2. {question[2]}  3. {question[3]}  4. {question[4]}")
        answer = input("Your answer (1-4): ").strip()
        if answer == question[5]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was option {question[5]}")

    print(f"\n{username}, you scored {score}/{len(questions)}.")
    save_score(username, subject, score)


def save_score(username, subject, score):
    """Save user's score to the file."""
    with open(scores_file, "a") as f:
        f.write(f"{username}|{subject}|{score}\n")


def show_results():
    """Display the quiz results."""
    print("\n--- Results ---")
    if not os.path.exists(scores_file):
        print("No results found.")
        return

    with open(scores_file, "r") as f:
        results = f.readlines()

    for result in results:
        username, subject, score = result.strip().split("|")
        print(f"{username} scored {score} in {subject} quiz.")


def display_banner():
    """Display the main menu."""
    print("\n--- Welcome to the Quiz App ---")
    print("1. Register")
    print("2. Login")
    print("3. Attempt Quiz")
    print("   a. DSA")
    print("   b. DBMS")
    print("   c. Python")
    print("4. Show Results")
    print("5. Exit")
    print("------------------------------")


def main():
    """Main function to run the quiz app."""
    initialize_files()
    current_user = None

    while True:
        display_banner()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            current_user = register_user()
        elif choice == "2":
            current_user = login_user()
        elif choice == "3":
            if not current_user:
                print("You need to log in first.")
                continue

            print("\nChoose a quiz:")
            print("a. DSA")
            print("b. DBMS")
            print("c. Python")
            subject_choice = input("Enter your choice (a/b/c): ").strip().lower()

            if subject_choice == "a":
                attempt_quiz(current_user, "DSA")
            elif subject_choice == "b":
                attempt_quiz(current_user, "DBMS")
            elif subject_choice == "c":
                attempt_quiz(current_user, "Python")
            else:
                print("Invalid choice.")
        elif choice == "4":
            show_results()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
