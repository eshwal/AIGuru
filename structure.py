import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s')

list_of_files = [
    "src/helpers.py",
    "src/__init__.py",
    "src/prompt.py",
    "app.py",
    "index_embeddings.py",
    "setup.py",
    "requirements.txt",
    ".env",
    "research/All_Code.ipynb"
]

def create_project_structure():
    for file in list_of_files:
        dir_path,file_name = os.path.split(Path(file))

        # Create directory/file if it does not exist
        if dir_path and not os.path.exists(dir_path):
            os.makedirs(dir_path)
            logging.info(f"Created directory: {dir_path}")
        else:
            logging.info(f"Directory already exists: {dir_path}")
        if not os.path.exists(file):
            with open(file,'w') as f:
                pass # Create an empty file
            logging.info(f"Created file: {file_name}")
        else:
            logging.info(f"File already exists: {file_name}")
        


if __name__ == "__main__":
    create_project_structure()