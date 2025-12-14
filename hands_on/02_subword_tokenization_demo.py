# 02_subword_tokenization_demo.py

words = ["unhappiness", "tokenization", "preprocessing"]

# Simple manual subword split (demo purpose)
subword_tokens = []
for word in words:
    if word.startswith("un"):
        subword_tokens.append("un")
        subword_tokens.append(word[2:])
    else:
        subword_tokens.append(word)

print("Subword Tokens:", subword_tokens)
