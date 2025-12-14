# GPT vs BERT Tokenization

GPT uses byte-level BPE which handles unseen characters gracefully.

BERT uses WordPiece, which may introduce `[UNK]` tokens.
