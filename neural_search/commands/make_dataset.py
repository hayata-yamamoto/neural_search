from argparse import ArgumentParser

import pandas as pd
from flair.embeddings import BertEmbeddings
from tqdm import tqdm

from neural_search.core.path_manager import PathManger
from neural_search.core.nlp import embedding


def main():
    tqdm.pandas()
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', help='source file name', required=True)
    parser.add_argument('-o', '--output', help='output filename', default=PathManger.DATA_DIR / 'vector.json')

    args = parser.parse_args()
    df = pd.read_csv(args.file)[['title', 'description']]
    bert = BertEmbeddings()
    df['vector'] = df.description.progress_apply(embedding, embedder=bert)
    df.to_json(args.output)


if __name__ == '__main__':
    main()
