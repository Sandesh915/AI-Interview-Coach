from dotenv import load_dotenv

from chains.interviewer import (
    create_interviewer_chain,
    INTERVIEWER_STYLES,
)


load_dotenv()


def run_basic_interview():

    interviewer = create_interviewer_chain()

    config = {
        "interview_type": "technical Python",
        "level": "senior",
        "focus_area": "Python fundamentals, OOP, and best practices",
        "total_questions": 5,
        "interviewer_style": INTERVIEWER_STYLES["friendly"],
    }

    print("=" * 50)
    print("AI Interview Coach")
    print("=" * 50)
    print("Type 'quit' to exit.\n")

    # First question
    response = interviewer.invoke({
        **config,
        "question_number": 1,
        "input": "Start the interview with your first question.",
    })

    print(f"\nInterviewer: {response}\n")

    question_num = 1

    while question_num < config["total_questions"]:

        answer = input("You: ")

        if answer.lower() == "quit":
            break

        question_num += 1

        response = interviewer.invoke({
            **config,
            "question_number": question_num,
            "input": (
                f"The candidate answered:\n{answer}\n\n"
                f"Acknowledge the answer briefly and ask "
                f"question {question_num}."
            ),
        })

        print(f"\nInterviewer: {response}\n")

    print("Interview complete!")


if __name__ == "__main__":
    run_basic_interview()