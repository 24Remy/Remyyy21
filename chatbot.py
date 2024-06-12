class ChatBot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there!",
            "how are you": "I'm just a program, but I'm functioning well. How can I help you?",
            "bye": "Goodbye!",
            "thanks": "You're welcome!",
            "default": "I'm sorry, I didn't understand that."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        for key, value in self.responses.items():
            if key in user_input:
                return value
        return self.responses["default"]

def main():
    chatbot = ChatBot()
    print("Hi, I'm a chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chatbot.get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()