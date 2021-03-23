import os
import spacy
import math
import numpy as np
import pprint


def is_token_word(token):
    return token.is_alpha and not (
        token.is_punct or token.is_space or token.is_stop or token.like_num
    )


def lemmatize_token(token):
    return token.lemma_.lower()


def doc_to_lemmas(doc):
    return np.array([lemmatize_token(t) for t in doc if is_token_word(t)])


def load_data_files(data_dir):
    if not os.path.exists(data_dir):
        raise Exception(f"Dir given does not exist: ({data_dir})")

    docstrs = []
    for doc_dir in os.listdir(data_dir):
        with open(f"{data_dir}/{doc_dir}") as f:
            docstrs.append(f.read())

    return docstrs


# def load_docs(data_dir, nlp_model):
#     if not os.path.exists(data_dir):
#         raise Exception(f"Dir '{data_dir}' does not exist.")

#     docs = []
#     for doc_dir in os.listdir(data_dir):
#         with open(f"{data_dir}/{doc_dir}") as f:
#             docstring = f.read()
#             docs.append(doc_to_lemmas(nlp_model(docstring)))
#     return docs


def calc_max_tf_in_doc(doc):
    return max(np.unique(doc, return_counts=True)[1])


def tf(term, doc, k=0.5):
    uniques, counts = np.unique(doc, return_counts=True)
    counter_dict = dict(zip(uniques, counts))
    raw_tf = counter_dict[term]
    max_tf_count = max(counts)



def idf(term, corpus):
    return math.log((len(corpus) / (1 + len([d for d in corpus if term in d]))))


def tfidf(term, doc, corpus):
    return tf(term, doc) * idf(term, corpus)


def main():
    nlp = spacy.load("en_core_web_sm")
    raw_data = load_data_files("./data")
    data_models = np.array([nlp(dset) for dset in raw_data])
    data_corpus = np.array([doc_to_lemmas(doc_model) for doc_model in data_models])
    doc = data_models[0]
    raw_doc = doc_to_lemmas(doc)
    weights_table = {lemmatize_token(term): tfidf(lemmatize_token(term), raw_doc, data_corpus) if is_token_word(term) else 0 for term in doc}
    sentences = doc.sents
    weights_table_ranked = sorted([(w, v) for w, v in weights_table.items()], key=lambda x: x[1])
    print(pprint.pformat(weights_table_ranked))
    ranked_sents = sorted(
        sentences,
        key=lambda sentence: sum(weights_table[lemmatize_token(term)] for term in sentences if is_token_word(term)) / len(sentence),
        # reverse,
    )
    print('TOTAL # OF SENTS: ', len(ranked_sents))
    print(ranked_sents[:100])
    
    # N-Grams
    # Triplets and doubles
    # Apply tf idf 

    # 

if __name__ == "__main__":
    main()