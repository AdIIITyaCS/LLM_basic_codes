# # #here we are initially using the simple working of LLM where no memory is setup and answers we get only on the same context

# from google import genai
# client = genai.Client(api_key="AIzaSyDSWHHlp875BoZR6KDos5fxEG_lMTMXSYY")
# response = client.models.generate_content(
#     model="gemini-2.5-flash", contents="Okay,I am Aditya.Now can you tell what is my name?"
# )
# print("-----------------------------------")
# print(response.text)
# print("-----------------------------------")






# #Every time for a single query if we run the code it becomes hectic also the memory of previous query skipped. So now we want to achieve the same action as any chatgpt like tool does everytime pass the whole stuff to the model by saving the previous memory here. 

# from google import genai
# from google.genai import types
# # 1. Initialize the Client (Replace with your key)
# client = genai.Client(api_key="AIzaSyDSWHHlp875BoZR6KDos5fxEG_lMTMXSYY")

# # 2. Define the function (Synchronous version is standard in Python)
# def main():
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=[
#             {
#                 "role": "user",
#                 "parts": [
#                     {"text": "Hi, I am Aditya"}
#                 ]
#             },
#             {
#                 "role":"model",
#                 "parts":[
#                     {"text":"Hi Aditya! It's nice to meet you. How can I help you today?"}
#                     ]
#             },
#             {
#                 "role": "user",
#                 "parts": [
#                     {"text": "What is my name"}
#                 ]
#             }

#         ]
#     )
    
#     # 3. Print the result
#     print(response.text)

# # 4. Run the function
# if __name__ == "__main__":
#     main()





# # But in above every time we are pasting the answer from output to the content:role,parts in code.Now we will automate this.
# # REMEMBER,Oh after running this code we are maintaining the history. but when we quit the code, the history is deleted.

# from google import genai
# # 1. Initialize the Client
# client = genai.Client(api_key="AIzaSyDSWHHlp875BoZR6KDos5fxEG_lMTMXSYY")

# # 2. Initialize an empty list to maintain chat history manually
# chat_history = []

# print("--- Manual Chat History (Type 'quit' to exit) ---")

# # 3. Define the Chatting Function
# def chat_with_model(user_query):
#     # Add the user's question to the history
#     chat_history.append({
#         "role": "user",
#         "parts": [{"text": user_query}]
#     })

#     # Send the ENTIRE history to the model
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=chat_history
#     )

#     # Print the model's response
#     print(f"Gemini: {response.text}")

#     # Add the model's response to the history
#     chat_history.append({
#         "role": "model",
#         "parts": [{"text": response.text}]
#     })

# # 4. Main Loop to Take Input
# if __name__ == "__main__":
#     while True:
#         user_input = input("\nYou: ")
        
#         if user_input.lower() in ["quit", "exit"]:
#             break
        
#         chat_with_model(user_input)





# # #now we are trying that our code itself stores the history not like above storing done by in LLM 
from google import genai

# 1. Setup Client
client = genai.Client(api_key="AIzaSyDSWHHlp875BoZR6KDos5fxEG_lMTMXSYY")

# 2. Create the Chat Session (This object holds the memory/history automatically)
#    This is the equivalent of: const chat = ai.chats.create(...)
chat = client.chats.create(
    model="gemini-2.0-flash",
    history=[]  # Starts empty, but fills up automatically as you talk
)

print("--- Auto-History Chat (Type 'quit' to stop) ---")

while True:
    # 3. Take Input (Equivalent to readlineSync.question)
    user_input = input("\nAsk me anything --> ")

    if user_input.lower() in ["quit", "exit"]:
        break
    # 4. Send Message
    # The 'chat' object automatically saves this question AND the answer to 'history'
    response = chat.send_message(user_input)
    
    # 5. Print Answer
    print(f"Gemini: {response.text}")
