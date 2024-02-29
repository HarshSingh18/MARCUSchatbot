# MARCUS bot
A RAG-based question-answering bot trained on self-help books and youtube podcasts to answer all your questions about productivity and self-help.
It is powered  by Gemini pro as the LLM behind it's working.
You can use it without running code and installing dependencies [here](https://marcusbot.streamlit.app/) as it is hosted on streamlit community cloud.

## demo examples 

![Microsoft prompt](https://github.com/HarshSingh18/Github/assets/32611475/0dffbf4a-7e13-4815-80b2-3603ccea699d)

![image](https://github.com/HarshSingh18/Github/assets/32611475/8b77587f-2bbd-4f90-8ab3-f3545e3114e6)

## Working architecture 

![RAG working](https://miro.medium.com/v2/resize:fit:828/format:webp/1*KPTfB3CyLuKpg8Rfs4jaIQ.png)

* We split 21 documents into smaller chunks such that it can fit our embeddings model and give results accurately and clearly.​

​* We created the embeddings using the sentence transformer model 'all-MiniLM-l6-v2' and stored those embeddings using FAISS as database.  
It is used for storing and searching purpose. We can retrieve the embedding vectors which will be “most similar” through FAISS. 

* We  used  Google's 'gemini-pro' for the purpose of question-answering as well as retrieval from our database.​

* The chatbot ultimately generates answers to user queries after performing similarity search on the database object as well as the model augments the answers whenever necessary.​

* Streamlit was utilized to create our UI interface platform, incorporating a custom background image, image for the bot and user profile, alongside seamless integration within our chatbot system.

## Data Collection

The below image shows the markdown files collected for our project from youtube podcast videos transcript as well as E-books converted to markdown.
This data was fed to the sentence transformers model to create embeddings and store in the database.

![image](https://github.com/HarshSingh18/Github/assets/32611475/cf2e3dc3-2c3e-4d58-abd6-25ea4235d2fe)


