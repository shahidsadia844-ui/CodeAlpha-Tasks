def simple_chatbot():
    print("Chatbot: Hello! I am a simple rule-based chatbot. Type 'bye' to exit.")
    
    while True:
        # User se input lena aur lowercase mein convert karna
        user_input = input("You: ").lower().strip()
        
        # Rule 1: Exit condition
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
            
        # Rule 2: Greetings
        elif user_input in ['hello', 'hi', 'hey']:
            print("Chatbot: Hi! How can I help you today?")
            
        # Rule 3: Health/Status check
        elif user_input == 'how are you':
            print("Chatbot: I'm fine, thanks! How about you?")
            
        # Rule 4: Name check
        elif user_input in ['what is your name', 'who are you']:
            print("Chatbot: I am a basic rule-based chatbot built in Python.")
            
        # Rule 5: Default response
        else:
            print("Chatbot: Sorry, I am a simple chatbot and didn't quite catch that. Can you try again?")

# Program chalane ke liye
if __name__ == "__main__":
    simple_chatbot()
