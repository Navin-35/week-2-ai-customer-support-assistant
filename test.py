from chatbot import chat_with_ai

while True:
    question = input("Customer: ")

    if question.lower() == "exit":
        break

    response = chat_with_ai(question)

    print("\nCategory :", response["category"])
    print("Answer   :", response["answer"])
    print()