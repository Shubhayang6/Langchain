import getpass
import os

try:
    from dotenv import load_dotenv
    
    load_dotenv()
except ImportError:
    pass    


if not os.environ.get('MISTRAL_API_KEY'):
    os.environ['MISTRAL_API_KEY'] = getpass.getpass("Enter the API KEY for MISTRAL AI:")
    
from langchain.chat_models import init_chat_model

model = init_chat_model('mistral-large-latest', model_provider = 'mistralai')

model.invoke('Hello, world!')
print("DOnE")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Answer the question based on best on your knowledge"),
    HumanMessage("When was the last data uploaded to you as a model?")
]

# Streaming

for token in model.stream(messages):
    print(token.content, end = '', flush = True)
# model.invoke(messages)