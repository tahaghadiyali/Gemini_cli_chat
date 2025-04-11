# Gemini CLI Chat

Talk to Google's Gemini models directly from your command line. No frills, just a simple chat interface.

## What You Need

1.  **Python 3:** Make sure you have Python 3 installed.
2.  **Gemini API Key:** Get one from [Google AI Studio](https://aistudio.google.com/). **Keep this key secret!**

## Quick Setup

1.  **Get the code:** Download or clone this repository.
2.  **Navigate:** Open your terminal in the project directory.
    ```bash
    cd /path/to/gemini-cli-chat
    ```
3.  **Set up environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate # Linux/macOS
    # venv\Scripts\activate # Windows
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # (Or: pip install google-generativeai python-dotenv ipython)
    ```
5.  **Add your API Key:**
    *   Create a file named `.env` in the project directory.
    *   Add *one* line to this file:
        ```
        GOOGLE_API_KEY="YOUR_ACTUAL_API_KEY_HERE"
        ```
    *   Replace `YOUR_ACTUAL_API_KEY_HERE` with your real key.
    *   **Important:** The included `.gitignore` should prevent you from accidentally committing your `.env` file, but always double-check.

## How to Use

1.  **Run the script:**
    ```bash
    python gemini_chat.py
    ```
2.  **Start chatting!** Type your message and press Enter.
3.  **To quit:** Type `quit` or `exit` and press Enter.

You can also start with an initial prompt:

```bash
python gemini_chat.py "What's the weather like on Mars?"
