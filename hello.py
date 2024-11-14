# Define quiz questions for each department
quiz_data = {
    "Accounting": [
        {
            "question": "What is the basic accounting equation?",
            "options": ["Assets = Liabilities + Equity", "Assets = Liabilities - Equity",
                        "Equity = Assets + Liabilities"],
            "answer": "Assets = Liabilities + Equity"
        },
        {
            "question": "Which financial statement shows a company’s profits or losses?",
            "options": ["Balance Sheet", "Income Statement", "Cash Flow Statement"],
            "answer": "Income Statement"
        }
    ],
    "Math": [
        {
            "question": "What is the derivative of sin(x)?",
            "options": ["cos(x)", "-sin(x)", "-cos(x)"],
            "answer": "cos(x)"
        },
        {
            "question": "What is the value of pi (π) approximately?",
            "options": ["3.14", "3.21", "2.17"],
            "answer": "3.14"
        }
    ],
    "Pharmacy": [
        {
            "question": "What does OTC stand for in pharmacy?",
            "options": ["Over-The-Counter", "On-The-Clock", "Open-To-Consult"],
            "answer": "Over-The-Counter"
        },
        {
            "question": "Which of the following is an antibiotic?",
            "options": ["Ibuprofen", "Amoxicillin", "Loratadine"],
            "answer": "Amoxicillin"
        }
    ]
}


def run_quiz(department):
    """Function to run the quiz for a specific department."""
    score = 0
    questions = quiz_data.get(department, [])

    print(f"\nStarting quiz for {department} department.\n")

    # Loop through each question
    for i, item in enumerate(questions, start=1):
        print(f"Question {i}: {item['question']}")
        for j, option in enumerate(item['options'], start=1):
            print(f"{j}. {option}")

        # Get user answer
        answer_index = input("Enter the number of your answer: ")

        # Check if answer is correct
        if item['options'][int(answer_index) - 1] == item['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {item['answer']}\n")

    # Display score
    print(f"Quiz Completed! Your score: {score}/{len(questions)}\n")


def main():
    """Main function to select department and start quiz."""
    print("Welcome to the University Quiz Application!")
    print("Please select your department:")
    print("1. Accounting")
    print("2. Math")
    print("3. Pharmacy")

    # Get user department choice
    department_choice = input("Enter the number of your department: ")
    department_map = {"1": "Accounting", "2": "Math", "3": "Pharmacy"}
    department = department_map.get(department_choice, None)

    # Check if a valid department was selected
    if department:
        run_quiz(department)
    else:
        print("Invalid department selection. Exiting the quiz.")


# Run the main function
if __name__ == "__main__":
    main()
