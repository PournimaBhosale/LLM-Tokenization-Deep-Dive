# 🧩 Tokenization Basics

Tokenization is the process of converting raw text into smaller units
called **tokens** that a language model can process.

Since neural networks operate on numbers, tokenization acts as the bridge
between human-readable text and numerical representations.

---

## 🔹 What Is a Token?

A token can represent:
- A word (`apple`)
- Part of a word (`play`, `##ing`)
- A character
- A byte
- A symbol or emoji 

---

## 🔹 Vocabulary and Token IDs

Each tokenizer maintains a **vocabulary**:
- Every token has a unique integer ID
- Models operate on these IDs, not raw text

Example:  "hello" → ["he", "llo"] → [1534, 9821]


---

## 🔹  Why Tokenization Matters

- Controls context window usage
- Impacts inference cost 
- Affects multilingual handling 
- Determines robustness to unseen words
