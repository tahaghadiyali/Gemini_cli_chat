import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv
import argparse

def main():
    load_dotenv()  # grab env vars
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not found.")
        print("Please create a .env file with GOOGLE_API_KEY='YOUR_API_KEY'")
        sys.exit(1)  # bail out if no key

    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring Gemini API: {e}")
        sys.exit(1)


    parser = argparse.ArgumentParser(description="Chat with Google Gemini via CLI.")
    parser.add_argument(
        "initial_prompt",
        nargs="?",  # optional arg
        type=str,
        help="Optional initial prompt to start the conversation."
    )
    args = parser.parse_args()

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        chat = model.start_chat(history=[])

        print("------------------------------------")
        print(" Gemini CLI Chat Tool ")
        print("------------------------------------")
        print("Connected to Gemini model: gemini-1.5-flash-latest")
        print("Type 'quit' or 'exit' to end the chat.")
        print("------------------------------------")

    except Exception as e:
        print(f"Error initializing Gemini model or chat: {e}")
        sys.exit(1)


    if args.initial_prompt:
        print(f"\nYou: {args.initial_prompt}")
        send_and_receive(chat, args.initial_prompt)


    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["quit", "exit"]:
                print("\nGoodbye!")
                break

            if not user_input:  # skip empty inputs
                continue

            send_and_receive(chat, user_input)

        except KeyboardInterrupt:  # catch ctrl+c
            print("\nGoodbye!")
            break
        except EOFError:  # catch ctrl+d
             print("\nGoodbye!")
             break
        except Exception as e:  # catch everything else
            print(f"\nAn error occurred: {e}")
            # might want to break here depending on error

def send_and_receive(chat_session, prompt):
    """Sends prompt to Gemini and prints the response."""
    try:
        print("Gemini: Thinking...", end="\r", flush=True)  # show something's happening
        response = chat_session.send_message(prompt, stream=False)  # could enable streaming later

        # clear the "Thinking..." text
        print("                     ", end="\r", flush=True)

        if response.parts:
             print(f"Gemini: {response.text}")
        else:
             print("Gemini: (Received an empty response)")
        # Uncomment to see safety stuff
        # print(f"Safety Ratings: {response.prompt_feedback}")

    except Exception as e:
        print(f"\nError sending message or receiving response: {e}")
        # might need retry logic for rate limits

if __name__ == "__main__":
    main()