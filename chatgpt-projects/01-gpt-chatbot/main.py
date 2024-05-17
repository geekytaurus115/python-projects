# import os
# from openai import OpenAI

# from dotenv import load_dotenv

# load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
# )

import openai

openai.api_key = ""
def chat_with_gpt(prompt):

    response = openai.chat.completions.create(
       # model="gpt-3.5-turbo",
        model = "gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
    