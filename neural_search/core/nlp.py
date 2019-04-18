import numpy as np
from flair.embeddings import Embeddings, Sentence
from sklearn.metrics.pairwise import cosine_similarity


def embedding(sentence: str, embedder: Embeddings) -> np.ndarray:
    tokens = Sentence(sentence)
    embedder.embed(tokens)
    if len(tokens) == 1:
        return np.array(tokens[0].embedding.numpy())
    return np.mean([token.embedding.numpy() for token in tokens], axis=0)


def compute_cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return cosine_similarity(a[np.newaxis, :], b[np.newaxis, :])[0][0]
