# 04_token_count_analysis.py

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")

texts = [
    "Short text.",
    "This is a longer sentence to see how token count changes."
]

for text in texts:
    token_ids = tokenizer.encode(text)
    print(f"Text: {text}")
    print(f"Token count: {len(token_ids)}")
    print(f"Token IDs: {token_ids}\n")
