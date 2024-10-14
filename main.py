import argparse
from dotenv import dotenv_values
import openai

# Load the API key from the .env file
config = dotenv_values("apikey.env")
openai.api_key = config.get("OPENAI_API_KEY")

def bold(text):
    return f"\033[1m{text}\033[0m"

def blue(text):
    return f"\033[34m{text}\033[0m"

def red(text):
    return f"\033[31m{text}\033[0m"

def main():
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT-4"
    )
    parser.add_argument(
        "--personality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="friendly and helpful",
    )
    args = parser.parse_args()

    # Initial system message
    initial_prompt = f"You are a conversational chatbot. Your personality is: {args.personality}"
    messages = [{"role": "system", "content": initial_prompt}]

    while True:
        try:
            # Get user input
            user_input = input(bold(blue("You: ")))

            if user_input.lower() in ["exit", "quit"]:
                print("Exiting...")
                break

            # Add user's message
            messages.append({"role": "user", "content": user_input})

            # Get response from OpenAI
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Or "gpt-3.5-turbo"
                messages=messages,
                max_tokens=100,
            )

            # Extract and print the assistant's response
            assistant_response = response.choices[0].message.content
            print(bold(red("Assistant: ")), assistant_response)

            # Add the assistant's response to the message history
            messages.append({"role": "assistant", "content": assistant_response})

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
