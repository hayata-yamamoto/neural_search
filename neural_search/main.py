import numpy as np
import pandas as pd
from fastapi import FastAPI, Query
from flair.embeddings import BertEmbeddings

from neural_search.core.nlp import embedding, compute_cosine_similarity
from neural_search.core.path_manager import PathManger

app = FastAPI()
bert = BertEmbeddings()
data = pd.read_json(PathManger.DATA_DIR / "vector.json")
data.vector = data.vector.apply(np.array)


@app.get("/search/")
async def search(q: str = Query(...)):
    vector = embedding(sentence=q, embedder=bert)
    data['similarity'] = data.vector.apply(compute_cosine_similarity, b=vector)
    return data.nlargest(5, 'similarity')['description'].to_dict()

