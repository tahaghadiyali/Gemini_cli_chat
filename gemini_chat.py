import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv
import argparse

def main():
    load_dotenv() # Load variables from .env file
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not found.")
        print("Please create a .env file with GOOGLE_API_KEY='YOUR_API_KEY'")
        sys.exit(1) # Exit if key is missing

    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring Gemini API: {e}")
        sys.exit(1)

    # --- 2. Argument Parser (Optional: for initial prompt) ---
    parser = argparse.ArgumentParser(description="Chat with Google Gemini via CLI.")
    parser.add_argument(
        "initial_prompt",
        nargs="?", # Makes the argument optional
        type=str,
        help="Optional initial prompt to start the conversation."
    )
    args = parser.parse_args()

    # --- 3. Model and Chat Initialization ---
    try:
        # Choose the model - 'gemini-pro' is a common choice for chat
        model = genai.GenerativeModel('gemini-2.5-pro-preview-03-25')

        # Start a chat session (this keeps track of history)
        chat = model.start_chat(history=[])

        print("------------------------------------")
        print(" Gemini CLI Chat Tool ")
        print("------------------------------------")
        print("Connected to Gemini model: gemini-2.5-pro-preview-03-25")
        print("Type 'quit' or 'exit' to end the chat.")
        print("------------------------------------")

    except Exception as e:
        print(f"Error initializing Gemini model or chat: {e}")
        sys.exit(1)


    # --- 4. Handle Initial Prompt (if provided) ---
    if args.initial_prompt:
        print(f"\nYou: {args.initial_prompt}")
        send_and_receive(chat, args.initial_prompt)


    # --- 5. Interactive Chat Loop ---
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()

            if user_input.lower() in ["quit", "exit"]:
                print("\nGoodbye!")
                break

            if not user_input: # Handle empty input
                continue

            send_and_receive(chat, user_input)

        except KeyboardInterrupt: # Handle Ctrl+C gracefully
            print("\nGoodbye!")
            break
        except EOFError: # Handle Ctrl+D gracefully
             print("\nGoodbye!")
             break
        except Exception as e: # Catch other potential errors during loop
            print(f"\nAn error occurred: {e}")
            # Optionally decide whether to break or continue
            # break

def send_and_receive(chat_session, prompt):
    """Sends prompt to Gemini and prints the response."""
    try:
        print("Gemini: Thinking...", end="\r", flush=True) # Indicate processing
        # Send message to Gemini (includes history automatically)
        response = chat_session.send_message(prompt, stream=False) # stream=True for streaming response

        # Clear "Thinking..." message
        print("                     ", end="\r", flush=True)

        # Print Gemini's response
        # Access the text content safely
        if response.parts:
             print(f"Gemini: {response.text}")
        else:
             print("Gemini: (Received an empty response)")
        # Safety ratings check (optional but good practice)
        # print(f"Safety Ratings: {response.prompt_feedback}")

    except Exception as e:
        print(f"\nError sending message or receiving response: {e}")
        # Consider how to handle API errors (e.g., rate limits, content filtering)

# --- Entry Point ---
if __name__ == "__main__":
    main()