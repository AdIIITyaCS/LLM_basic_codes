
-----------------------------------

File 1: 01_basic_generation.py

Description
This script demonstrates the "Hello World" of the Google GenAI SDK. It shows how generate_content works in its simplest form: Stateless Interaction.

Key Concept
- No Memory: If you run this code, tell the model your name, and then ask "What is my name?" in a separate call, it will not know.
- Every call to the API is treated as a brand new conversation.

-----------------------------------

File 2: 02_manual_context.py

Description
This script solves the "memory loss" problem by manually constructing the conversation history. It shows how the LLM actually understands context—by receiving the entire previous conversation history every time you send a new prompt.

Key Concept
- Context Injection: We manually build a list containing role: "user" and role: "model" parts.
- Stateless Protocol: This proves that the API itself doesn't "remember" you; you must remind it of who you are by sending the full history with every request.

-----------------------------------

File 3: 03_manual_chat_loop.py

Description
This script automates the process from File 2. Instead of hardcoding the history, we use a Python while loop and a list (chat_history) to dynamically save what you type and what the model replies.

Key Concept
- The "Chatbot" Logic:
  1. Take user input.
  2. Append input to the chat_history list.
  3. Send the entire list to the model.
  4. Append the model's response to the list.
- Limitation: This requires writing a lot of boilerplate code to manage the list manually.

-----------------------------------

File 4: 04_sdk_chat_session.py

Description
This is the professional and most efficient way to handle conversations. It utilizes the SDK's built-in chats.create method.

Key Concept
- Automatic History Management: You no longer need to manually append to a list. The chat object handles the memory for you.
- Method: Uses chat.send_message() instead of generate_content().
- Benefit: The code is cleaner, easier to read, and less prone to errors.

-----------------------------------
