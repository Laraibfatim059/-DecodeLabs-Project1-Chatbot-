# DecodeLabs - Project 1: Rule-Based AI Chatbot

def main():
    # 1. Responses Mapping (Dictionary for O(1) Lookup)
    responses = {
        "hello": "Hi there! Welcome to DecodeLabs AI Assistant.",
        "hi": "Hello! How can I help you today?",
        "how are you": "I am a rule-based AI script running smoothly!",
        "how are u": "I am doing well, thank you for asking!",
        "what is your name": "I am DecodeBot, built using Python control flow.",
        "who created you": "I was created as part of the DecodeLabs AI Training Kit.",
        "help": "Available commands: hello, hi, how are you, what is your name, who created you, exit."
    }

    print("==================================================")
    print("      DECODELABS RULE-BASED AI CHATBOT (V1.0)     ")
    print("==================================================")
    print("Type 'help' for available commands, or 'exit' to quit.\n")

    # 2. Infinite Loop (The Heartbeat)
    while True:
        # Input & Sanitization (Lowercasing & Whitespace Removal)
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # Exit Strategy (Kill Command)
        if clean_input in ["exit", "bye", "quit"]:
            print("Chatbot: Terminating session. Goodbye!")
            break

        # Skip empty inputs
        if not clean_input:
            continue

        # Atomic Dictionary Lookup with Fallback Response (Fixed Prefix)
        reply = responses.get(clean_input, "I'm sorry, I don't understand that. Type 'help' for options.")
        
        print(f"Chatbot: {reply}\n")

if __name__ == "__main__":
    main()