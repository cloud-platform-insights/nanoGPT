import os
import tiktoken
import numpy as np
import pandas as pd

df = pd.read_csv('data/movie_quotes/movie_quotes.csv')
data = df['quote'].str.cat(sep='\n')

n = len(data)
train_data = data[:int(n*0.9)]
val_data = data[int(n*0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile('data/movie_quotes/train.bin')
val_ids.tofile('data/movie_quotes/val.bin')

# train.bin has 301,966 tokens
# val.bin has 36,059 tokens