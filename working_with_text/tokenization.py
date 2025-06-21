import requests
from  pathlib import Path

def load_text_file(outpath="./data/verdict.txt"):
    URL = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"

    if not Path(outpath).exists():
        response = requests.get(URL)
        with open(outpath,"w") as outfile:
            outfile.write(response.text)
    with open("./data/verdict.txt", encoding="utf-8") as f:
        raw_text = f.read()
    return raw_text
