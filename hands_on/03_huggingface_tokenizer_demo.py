# 03_huggingface_tokenizer_demo.py

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = "Hello world! Tokenization in GPT-2."

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
