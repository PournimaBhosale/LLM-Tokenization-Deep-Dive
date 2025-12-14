# Tokenizers in LLMs

- GPT: Byte-level BPE
- BERT: WordPiece
- LLaMA: SentencePiece (Unigram)

## 🧩 Tokenizers in Large Language Models (LLMs)

A tokenizer is the **bridge between human language and machine
understanding**. Large Language Models (LLMs) do not read text directly;
they operate on **tokens represented as numbers**. The tokenizer defines
how text is split, encoded, and reconstructed.

Choosing the right tokenizer directly affects model performance,
efficiency, and cost.

---

## What Is a Tokenizer?

A tokenizer is a system that:
1. Splits text into tokens
2. Converts tokens into numerical IDs
3. Handles special symbols and formatting
4. Reconstructs text during decoding

Without a tokenizer, an LLM cannot process text.

---

##  Core Components of a Tokenizer

Every tokenizer used in LLMs consists of the following components:

### 1️⃣ Vocabulary

- A fixed list of tokens known to the model
- Each token has a unique ID
- Vocabulary size impacts memory and efficiency

Example:
"hello" → 15496
"world" → 2159


---

### 2️⃣ Tokenization Algorithm

Defines **how text is split into tokens**.

Common algorithms:
- Byte Pair Encoding (BPE)
- WordPiece
- Unigram Language Model

This algorithm decides how words are broken into subwords.

---

### 3️⃣ Special Tokens

Special tokens guide model behavior.

Common examples:
- `[CLS]` – Classification token (BERT)
- `[SEP]` – Sentence separator
- `<BOS>` – Beginning of sequence
- `<EOS>` – End of sequence
- `<PAD>` – Padding token

---

### 4️⃣ Encoder and Decoder

- **Encoder**: Converts text → tokens → IDs
- **Decoder**: Converts IDs → tokens → text

This ensures that the process is reversible.

---

## 🔹 Tokenizers Used in Popular LLMs

Different models use different tokenization strategies.

---

### 🔸 GPT Family (GPT-2, GPT-3, GPT-4)

**Tokenizer Type:** Byte Pair Encoding (BPE)  
**Key Feature:** Byte-level tokenization

Example: "ChatGPT" → ["Chat", "G", "PT"]


Why GPT uses BPE:
- Handles any Unicode input
- No unknown tokens
- Efficient for open-domain text

---

### 🔸 BERT

**Tokenizer Type:** WordPiece  
**Key Feature:** Subword tokens with `##` prefix

Example:"playing" → ["play", "##ing"]

Why BERT uses WordPiece:
- Strong handling of rare words
- Optimized for bidirectional context

---

### 🔸 LLaMA

**Tokenizer Type:** SentencePiece (Unigram)  
**Key Feature:** Language-agnostic tokenization

Example:"unbelievable" → ["un", "believ", "able"]


Why LLaMA uses SentencePiece:
- Works without whitespace
- Suitable for multilingual models

---

## Byte-Level vs Word-Level Tokenizers

| Feature | Byte-Level | Word-Level |
|------|-----------|-----------|
| Unknown words | Never | Frequent |
| Vocabulary size | Moderate | Large |
| Multilingual support | Strong | Weak |
| Used in LLMs | ✅ Yes | ❌ No |

Modern LLMs strongly prefer **byte or subword tokenizers**.

---

## Common Tokenization Pitfalls

- Different tokenizers produce different token counts
- Tokenization mismatches break fine-tuning
- Special tokens must match model training

> Always use the tokenizer shipped with the model.

---

## 🎯 Key Takeaways

- Tokenizers define how LLMs understand language
- Subword tokenization is the industry standard
- Tokenizer choice impacts cost, accuracy, and latency
- Model and tokenizer must always stay aligned
