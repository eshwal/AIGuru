# AIGuru

# Steps on how to run

## Step 1: Clone the repository:
```bash
git clone https://github.com/eshwal/AIGuru.git
```

## Step 2: Create virtual environment
```bash
python -m venv <envname>
```

## Step 3: Activate enviornment
On Windows:
```bash
$ cd <envname>
$ Scripts\activate
```

On Linux/Mac:
```bash
source virtualenv_name/bin/activate
```

## Step 4: Install requirements
```bash
pip install -r requirements.txt
```

## Step 5: Create a `.env` file in the root directory and add your Pinecone & mistralai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MISTRAL_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
## Step 6: Create pinecone index and store embeddings (Need to perform only once)
```bash
python create_store.py
```

## Step 7: Run the app file
```bash
python app.py
```

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
