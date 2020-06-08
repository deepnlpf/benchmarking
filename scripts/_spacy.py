"""[SpaCy]
"""

import spacy
import load_file

from tqdm import tqdm

def run(corpus):
    #tasks = ['pos', 'tag', 'shape', 'is_alpha', 'is_title', 'like_num', 'label']

    experience_1_analise_lexica_spacy = ['pos', 'tag', 'shape', 'is_alpha', 'is_title', 'like_num', 'label']

    tasks=experience_1_analise_lexica_spacy

    nlp = spacy.load('en_core_web_sm')

    sentences_list = []

    for index, sentence in enumerate(tqdm(corpus)):
        # generated document spacy.
        doc = nlp(sentence)

        data_tokens_list = []

        # Analisys in Nivel Token
        for idx, token in enumerate(doc):
            data_token = {}
            
            data_token['idx'] = idx
            data_token['text'] = token.text
            
            if "pos" in tasks:
                data_token['pos'] = token.pos_
            if "tag" in tasks:
                data_token['tag'] = token.tag_
            if "shape" in tasks:
                data_token['shape'] = token.shape_
            if "is_alpha" in tasks:
                data_token['is_alpha'] = token.is_alpha
            if "is_title" in tasks:
                data_token['is_title'] = token.is_title
            if "like_num" in tasks:
                data_token['like_num'] = token.like_num

            data_tokens_list.append(data_token)

        item_sent = {
            "idx": index,
            "text": sentence,
            "tokens": data_tokens_list
        }

        sentences_list.append(item_sent)

    return sentences_list

if __name__ == "__main__":
    path_corpus = '/home/fasr/Mestrado/Workspace/deepnlpf/deepnlpf/profile_analysis/data/in/corpus/semeval_2010/corpus8000sentences.txt'
    path_out = '/home/fasr/Mestrado/Workspace/deepnlpf/deepnlpf/profile_analysis/data/out/corpus8000sentences/spacy/corpus8000sentences.txt'
    
    corpus = load_file.load(path_corpus)
    
    result = run(corpus)

    load_file.save(path_out, str(result))