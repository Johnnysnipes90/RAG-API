import os
from openai import OpenAI

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

  # Use env variable instead

def generate_response(context: str, query: str) -> str:
    prompt = f"Context: {context}\nQuestion: {query}\nAnswer:"
    print("Prompt: ", prompt)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

# from openai import OpenAI
# client = OpenAI()

# completion = client.chat.completions.create(
#     model="gpt-4o",
#     messages=[{
#         "role": "user",
#         "content": "Write a one-sentence bedtime story about a unicorn."
#     }]
# )

# print(completion.choices[0].message.content)