import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

#from api import API_KEY

genai.configure(api_key='AIzaSyClTOyWii44VqJAzliYWqyqHZ6sh7-oRdw')

 # Define the path to the pre-trained model you want to use
modelPath = "sentence-transformers/all-MiniLM-l6-v2"
# Create a dictionary with model configuration options, specifying to use the CPU for computations
model_kwargs = {'device':'cpu'}
# Create a dictionary with encoding options, specifically setting 'normalize_embeddings' to False
encode_kwargs = {'normalize_embeddings': False}
# Initialize an instance of HuggingFaceEmbeddings with the specified parameters
embeddings = HuggingFaceEmbeddings(
    model_name=modelPath,     # Provide the pre-trained model's path
    model_kwargs=model_kwargs, # Pass the model configuration options
    encode_kwargs=encode_kwargs # Pass the encoding options
     )


# choose any model from hugging face, and start with a tokenizer to preprocess text and a question-answering model to provide answers based on input text and questions.
db = FAISS.load_local("faiss_index", embeddings)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history = [])

def marcusInitial():
  response = chat.send_message("Act like you are a friend to me. I'll ask you questions and give you some context from productivity and self-help books. Talk to me, answer my questions with your own knowledge and quoting from the context I provide. Begin by saying 'Hi, I am M.A.R.C.U.S.! What's on your mind?' and then I'll start asking questions. Remember to interact with me in an encouraging, supportive and helpful tone. Try talking in a friend\'s brief conversational tone. Ask me questions or opinions as well'")
  return response.text

def marcusChat(query):
  docs = db.similarity_search(query)
  if 'bye' in query.lower():
    response = chat.send_message('Thank you. Bye!')
    return response.text
  try:
    response = chat.send_message('Question: '+query+' Content": '+'. '.join([docs[i].page_content for i in range(4)]))
  except:
    return "Sorry, something went wrong. Please try again!"
  return response.text
