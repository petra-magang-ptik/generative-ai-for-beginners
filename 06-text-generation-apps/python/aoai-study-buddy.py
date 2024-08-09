from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client
client = OpenAI(
  api_key=os.environ['API_KEY'],
  base_url=os.environ['BASE_URL']
)

deployment=os.environ['CHAT_COMPLETION_MODEL']

# add your completion code
question = input("Ask your questions on python language to your study buddy: ")
prompt = f"""
You are an expert on the python language.

Whenever certain questions are asked, you need to provide response in below format.

- Concept
- Example code showing the concept implementation
- explanation of the example and how the concept is done for the user to understand better.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
