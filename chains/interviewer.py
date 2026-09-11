from memory.conversation import create_memory
from chains.interviewer import create_interviewer_chain_with_memory
from langchain_core.messages import HumanMessage, AIMessage

def run_interview_with_memory():
    # Create memory instance
    memory = create_memory()

    # Create chain with memory
    interviewer = create_interviewer_chain_with_memory(memory)

    config = {
        "interview_type": "technical Python",
        "level": "senior",
        "focus_area": "Python fundamentals and design patterns",
    }

    print("=" * 50)
    print("AI Interview Coach - With Memory")
    print("=" * 50)
    print("Type 'quit' to exit, 'history' to see conversation\n")

    # Initial prompt
    user_input = "Please start the interview."

    while True:
        # Get response
        response = interviewer.invoke({
            **config,
            "input": user_input
        })

        # Save to memory
        memory.chat_memory.add_user_message(user_input)
        memory.chat_memory.add_ai_message(response)

        print(f"\nInterviewer: {response}\n")

        # Get next input
        user_input = input("You: ")

        if user_input.lower() == 'quit':
            break
        elif user_input.lower() == 'history':
            print("\n--- Conversation History ---")
            for msg in memory.chat_memory.messages:
                role = "You" if isinstance(msg, HumanMessage) else "Interviewer"
                print(f"{role}: {msg.content[:100]}...")
            print("--- End History ---\n")
            user_input = input("You: ")

    print("\nInterview complete!")
    return memory

if __name__ == "__main__":
    run_interview_with_memory()