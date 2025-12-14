<img width="801" height="400" alt="image" src="https://github.com/user-attachments/assets/e7e6374a-a0c1-46c0-a429-c32c13d5c573" />

# 🧠 Types of Tokenization

Tokenization is the process of breaking text into smaller units called
tokens. Depending on the level of granularity, tokenization can be
performed in multiple ways.

As explained in standard NLP literature (including GeeksforGeeks),
tokenization broadly falls into five categories. Modern LLMs build on
these foundations.

---

## 🔹 Character Tokenization

- Each character becomes a token
- Very small vocabulary
- Extremely long sequences

Rarely used in large production models.

Examples:

Input before tokenization: ["You are helpful"]
Output when tokenized by characters: ["Y", "o", "u", " ", "a", "r", "e", " ", "h", "e", "l", "p", "f", "u", "l"]

---

## 🔹 Word Tokenization

- Each word is treated as a token
- Vocabulary grows rapidly
- Cannot handle unseen words well

Example:

Input before tokenization: ["Machine Learning is fascinating"]
Output when tokenized by words: ["Machine", "learning", "is", "fascinating"]

---

## 🔹Subword Tokenization

- Breaks words into smaller meaningful units
- Handles unseen words gracefully
- Best balance between efficiency and flexibility

Example:
"unhappiness" → ["un", "happy", "ness"]

**Why LLMs use this**
- Handles unseen words
- Controls vocabulary size
- Preserves meaning better than characters

Algorithms include:
- Byte Pair Encoding (BPE)
- WordPiece
- Unigram Language Model

Used in GPT, BERT, LLaMA, and most modern LLMs.

---

---
## 🔹 Sentence Tokenization

Sentence tokenization splits a paragraph into individual sentences.
It is often the **first preprocessing step** in NLP pipelines.

Example:

"Hello world. How are you?"
→ ["Hello world.", "How are you?"]


**Where it is used**
- Text summarization
- Document processing
- Question answering systems

**Note:**  
LLMs usually operate *after* sentence tokenization, not at this level.

---
## 🔹 N-gram Tokenization

N-gram tokenization breaks text into continuous sequences of N items (characters or words).
The value of N decides how many items are grouped together.

To keep it simple, let’s use one sentence for all examples.

Example sentence
"I love AI"

1️⃣ Unigram Tokenization (N = 1)

Each single word is a token.
["I", "love", "AI"]

This is the simplest form of tokenization.

2️⃣ Bigram Tokenization (N = 2)

Each token contains two consecutive words.
["I love", "love AI"]

Helps capture basic word relationships.

3️⃣ Trigram Tokenization (N = 3)

Each token contains three consecutive words.
["I love AI"]

Captures short phrases, but data becomes sparse.


Key Idea (Easy Summary)
- Smaller **N** → simpler and more general
- Larger **N** → more context but harder to manage
- N-grams are **foundational NLP concepts**
- Modern LLMs prefer **subword tokenization** over large N-grams
