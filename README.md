# MARCUS bot

## demo examples 

![Microsoft prompt](https://github.com/HarshSingh18/Github/assets/32611475/0dffbf4a-7e13-4815-80b2-3603ccea699d)

When can we 


## Working architecture 

![RAG working](https://miro.medium.com/v2/resize:fit:828/format:webp/1*KPTfB3CyLuKpg8Rfs4jaIQ.png)

* We split 21 documents into smaller chunks such that it can fit our embeddings model and give results accurately and clearly.​

​* We created the embeddings using the sentence transformer model 'all-MiniLM-l6-v2' and stored those embeddings using FAISS as database.  
It is used for storing and searching purpose. We can retrieve the embedding vectors which will be “most similar” through FAISS. 

* We  used  Google's 'gemini-pro' for the purpose of question-answering as well as retrieval from our database.​

* The chatbot ultimately generates answers to user queries after performing similarity search on the database object as well as the model augments the answers whenever necessary.​

* Streamlit was utilized to create our UI interface platform, incorporating a custom background image, image for the bot and user profile, alongside seamless integration within our chatbot system.

