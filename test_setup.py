from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")
response = llm.invoke("Say 'Setup complete!' if you can hear me.")
print(response.content)