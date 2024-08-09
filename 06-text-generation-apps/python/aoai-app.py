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
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "user", "content": prompt}]
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
