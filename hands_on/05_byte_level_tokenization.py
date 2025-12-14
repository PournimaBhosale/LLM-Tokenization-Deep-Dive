# 05_byte_level_tokenization.py

from transformers import GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = "I love NLP! "

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Text:", text)
print("Tokens:", tokens)
print("Token IDs:", token_ids)
