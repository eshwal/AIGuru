from flask import Flask, request, jsonify,render_template
from src.helpers import load_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_mistralai import ChatMistralAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from src.prompt import prompt
from dotenv import load_dotenv
import os 


app = Flask(__name__)

#  Load environment variables 
load_dotenv()
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")


index_name ='aibot'

# Load embeddings model
embeddings =load_embeddings()

# Retrieve documents from the vector store

retrieved_docs = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = retrieved_docs.as_retriever(search_type="similarity", search_kwargs={"k":3})

final_prompt = ChatPromptTemplate.from_messages([
    ("system",prompt),
    ("human","{input}")
])


# Defining the LLM
llm = ChatMistralAI(
    model_name="mistral-large-latest",
    max_tokens=500

)

# Create the chain
qa_chain = create_stuff_documents_chain(llm=llm, prompt=final_prompt)
rag_chain =create_retrieval_chain(retriever,qa_chain)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask_llm():
    ''' Endpoint to handle user queries and return responses from LLM.'''
    if request.method=='POST':
        user_query = request.get_json().get('message')
        print(user_query)
        if not user_query:
            return jsonify({'reply':'Please provide a valid query.'})
        else:
            response = rag_chain.invoke({"input": user_query})
            print(response["answer"])
            return jsonify({'reply': response["answer"]})


if __name__ == '__main__':
    app.run(debug=True)