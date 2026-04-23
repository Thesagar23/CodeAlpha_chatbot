print("simple chatbot")
print("type 'bye' to exit the chat \n")

while True:
    user = input("You:").lower()

    if user == "hello" or user =="hi":
        print("bot: hello! How can i help you?")

    elif user == "How are you?":
        print(" bot: I am fine,Thank you")
        
    elif user == "what is your name?":
        print(" bot: I am a simple python chatbot.")
        
    elif user == "bye":
        print(" bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry , I don't understand that.")
        