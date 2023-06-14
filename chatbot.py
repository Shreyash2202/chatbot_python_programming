import random

# Define a dictionary of possible user inputs and corresponding bot responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you!", "I'm great! How about you?"],
    "what's your name": ["My name is ChatBot.", "You can call me ChatBot!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?"]
}

# Function to generate bot response based on user input
def generate_response(user_input):
    # Convert user input to lowercase
    user_input = user_input.lower()

    # Check if user input matches any known responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    # If no match found, return a default response
    return random.choice(responses["default"])

# Main loop to simulate a conversation with the chatbot
while True:
    # Get user input
    user_input = input("User: ")

    # Generate and print bot response
    bot_response = generate_response(user_input)
    print("ChatBot:", bot_response)

    # Check if user wants to exit
    if user_input.lower() == "bye":
        break
