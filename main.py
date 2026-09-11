from dotenv import load_dotenv

from chains.interviewer import create_interviewer_with_history


load_dotenv()


def run_interview():

    interviewer = create_interviewer_with_history()

    config = {
        "interview_type": "technical Python",
        "level": "senior",
        "focus_area": "Python fundamentals and design patterns",
    }

    session_id = "interview_001"

    print("=" * 50)
    print("AI Interview Coach")
    print("=" * 50)
    print("Type 'quit' to exit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "quit":
            break

        response = interviewer.invoke(
            {
                **config,
                "input": user_input,
            },
            config={
                "configurable": {
                    "session_id": session_id
                }
            },
        )

        print(f"\nInterviewer: {response}\n")


if __name__ == "__main__":
    run_interview()