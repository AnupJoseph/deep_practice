from typing import Dict
import re

import requests
from pathlib import Path


def load_text_file(outpath="./data/verdict.txt"):
    URL = "https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt"

    if not Path(outpath).exists():
        response = requests.get(URL)
        with open(outpath, "w") as outfile:
            outfile.write(response.text)
    with open("./data/verdict.txt", encoding="utf-8") as f:
        raw_text = f.read()
    return raw_text


class Tokenizer_v1:
    def __init__(self, vocab: Dict[str, int]):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        result = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in result if item.strip()]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self,ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text
