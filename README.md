# AIGuru

# Steps on how to run

## Step 1: Clone the repository:
git clone https://github.com/eshwal/AIGuru.git

## Step 2: Create virtual environment
python -m venv <envname>

## Step 3: Activate enviornment
On Windows:
$ cd <envname>
$ Scripts\activate 

On Linux/Mac:
source virtualenv_name/bin/activate

## Step 4: Install requirements
pip install -r requirements.txt

## Step 5: Create a `.env` file in the root directory and add your Pinecone & mistralai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MISTRAL_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
## Step 6: Create pinecone index and store embeddings (Need to perform only once)
python create_store.py

## Step 7: Run the app file
python app.py

### Techstack Used
- Python
- Langchain
- Pinecone
- MistralAI
- Flask
- Bootstrap
- HTML
- CSS
- Javascript
