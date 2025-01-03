import os
# import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# pdf_file = open("generativeai.pdf", "rb")
# pdf_reader = PyPDF2.PdfReader(pdf_file)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    organization="org-dHEb2RJFMlSk3AkW3EaqchuP",
    project="proj_07gI9lPK51DvCfjgw6uIGRyW"
)

# pages_summary = []
# for page_num in range(len(pdf_reader.pages)):
#     page_text = pdf_reader.pages[page_num].extract_text()
#     chat_completion = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": f"Summarize this: {page_text}"}
#         ]
#     )

#     pages_summary.append(chat_completion.choices[0].message.content)
#     print(pages_summary[page_num])

# System prompt to use in the chat completion. Tells how the AI assistant should act and what it should do.
system_prompt = {"role": "system", "content": "You are a helpful assistant that summarizes texts and data. You must take the"
                "most important key points from the original content to the summarized text, you have to make the information" 
                "on the summarized text very clear and understable for the user, and you should make topics and give examples" 
                "if necessary for a better visualization and understanding of the content for the user."}

# message_history is a list that stores the messages between users and AI in the chat completion messages parameter format.
message_history = [system_prompt]

while True:
    # Gets user input, creates prompt, stores prompt in message_history variable.
    user_input = input("\033[92mUser: \033[0m").strip()
    user_prompt = {"role": "user", "content": user_input}
    message_history.append(user_prompt)

    # Generate response (summarized text) based on user prompt
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=message_history
    )

    # Stores assistant prompt in the message_history variable
    # response.choices[0].message == {"role": "assistante", "content": "<response>"}
    message_history.append(response.choices[0].message)

    # Prints response to the terminal.
    print("\033[92mAssistant: \033[0m" + response.choices[0].message.content)

