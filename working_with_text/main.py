from working_with_text.tokenization import load_text_file

from rich import print

import re

text = load_text_file()

print(text)

result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
preprocessed = [item.strip() for item in result if item.strip()]

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

vocab = {token: idx for idx, token in enumerate(all_words)}
print(list(vocab.items())[:50])