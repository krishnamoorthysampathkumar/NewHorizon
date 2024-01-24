from sentence_transformers import SentenceTransformer
import pandas as pd
import torch

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')

df = pd.read_csv("data.csv")

df["embeddings"] = df["runbook_title"].apply(lambda x: torch.tensor(model.encode(x)))
