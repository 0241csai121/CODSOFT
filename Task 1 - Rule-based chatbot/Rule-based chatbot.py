def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "what is your name" in user_input:
        return "I'm simply a rule-based chatbot.You can call me Chatbot."
    elif "who created you" in user_input:
        return "I was created by a python developer!"
    elif "i need help" in user_input:
        return "Sure, I can help.Ask me anything!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that."
while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit", "bye"]:
        print("Bot: Goodbye!")
        break
    response = chatbot_response(user)
    print("Bot:", response)
    

    
    