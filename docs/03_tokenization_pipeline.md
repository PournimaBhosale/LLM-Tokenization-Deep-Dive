# Tokenization Pipeline

Tokenization in modern NLP and Large Language Models (LLMs) is not a
single step. It is a **pipeline of transformations** that converts raw,
human-readable text into numerical tokens that a model can understand.

Each step in the pipeline plays a critical role in ensuring consistency,
efficiency, and correctness.

---

##  Overview of the Pipeline

The tokenization pipeline typically follows these steps:

1. Text normalization  
2. Pre-tokenization  
3. Subword segmentation  
4. Token-to-ID mapping  
5. Post-processing  

---

## 1️⃣ Text Normalization

Text normalization prepares raw text for tokenization by applying
standard rules.

### What happens here
- Lowercasing (optional)
- Unicode normalization
- Removing or standardizing special characters

### Example

**Input**
"HELLO World!!"

**After normalization**
"hello world"


> Normalization ensures that the same word is tokenized consistently.

---

## 2️⃣ Pre-tokenization

Pre-tokenization splits text into **basic units** using simple rules
such as spaces and punctuation.

### What happens here
- Splitting on whitespace
- Separating punctuation

### Example

**Input**
"Hello, world!"

**After pre-tokenization**
["Hello", ",", "world", "!"]


> This step reduces complexity for subword algorithms.

---

## 3️⃣ Subword Segmentation

This step breaks words into **subword units** using algorithms such as
BPE, WordPiece, or Unigram.

### Why this step is important
- Handles unseen words
- Controls vocabulary size
- Preserves semantic meaning

### Example

**Input**
"unhappiness"


**After subword tokenization**
["un", "happy", "ness"]


---

## 4️⃣ Token-to-ID Mapping

Once tokens are generated, each token is mapped to a **unique integer
ID** using the tokenizer’s vocabulary.

### Example

**Tokens**
["un", "happy", "ness"]


**Token IDs**
[312, 1456, 908]


> Models operate on these numerical IDs, not text.

---

## 5️⃣ Post-processing

Post-processing prepares token IDs for model input.

### What happens here
- Adding special tokens (`[CLS]`, `[SEP]`, `<EOS>`)
- Padding shorter sequences
- Truncating long sequences

### Example

**Before post-processing**
[312, 1456, 908]


**After post-processing**
[101, 312, 1456, 908, 102]

---

## Why the Tokenization Pipeline Matters

Small changes in any step of the pipeline can significantly affect:

- Token count
- Context window usage
- Inference cost
- Model output quality

A mismatch between training and inference tokenization can lead to
unexpected model behavior.

---

## 🎯 Key Takeaway

The tokenization pipeline is a **foundational component** of LLMs.
Understanding each step helps you:
- Debug model behavior
- Optimize costs
- Design better NLP systems
