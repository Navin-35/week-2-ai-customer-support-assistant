from chatbot import chat_with_ai

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = chat_with_ai(question)

    print("\nAI:", answer)
    print()