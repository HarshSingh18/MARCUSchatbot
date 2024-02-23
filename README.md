# MARCUS

![RAG working](https://miro.medium.com/v2/resize:fit:828/format:webp/1*KPTfB3CyLuKpg8Rfs4jaIQ.png)

## Preparing the LLM Model

You can choose any model from hugging-face and start with a tokenizer to preprocess text and a question-answering model to provide answers based on input text and questions. 

I used “Intel/dynamic_tinybert” which is a fine-tuned model for the purpose of question-answering.  

Create a question-answering pipeline using your pre-trained model and tokenizer and then extend its 
functionality by creating a LangChain pipeline with additional model-specific arguments.

