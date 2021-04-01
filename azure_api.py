import os
import json
import requests
import random as rd
import pprint
import spacy
from helpers import load_data_files
from dotenv import load_dotenv, find_dotenv

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]
LANG = "en"


def authenticate_client(endpoint, api_key):
    ta_credential = AzureKeyCredential(api_key)
    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint, credential=ta_credential
    )
    return text_analytics_client


def key_phrase_extraction_example(client, example_doc=None):

    try:
        documents = [
            "My cat might need to see a veterinarian."
            if example_doc is None
            else example_doc
        ]

        response = client.extract_key_phrases(documents=documents)[0]

        if not response.is_error:
            print("\tKey Phrases:")
            for phrase in response.key_phrases:
                print("\t\t", phrase)
        else:
            print(response.id, response.error)

    except Exception as err:
        print("Encountered exception. {}".format(err))


# def test_azure_api(endpoint, docs):
#     documents = []
#     for ID, doc in enumerate(docs):
#         documents.append({"language": LANG, "id": ID, "text": doc})

#     res = requests.post(
#         endpoint,
#         headers={
#             "Content-Type": "application/json",
#             "Ocp-Apim-Subscription-Key": API_KEY,
#         },
#         data={
#             "documents": documents,
#         },
#     )
#     print(res)
#     return res


def filter_sents(sents):
    for sent in sents:
        if sent.text.endswith("."):
            print("#####", sent.text)

def main():
    dataset = load_data_files("./data", as_dict=True)
    nlp = spacy.load("en_core_web_sm")
    doc_name = "amazon"
    amazon_raw_doc = dataset.get(doc_name)
    if amazon_raw_doc is None:
        print(f"Problem with loading doc {doc_name}")
        return

    amazon_doc = nlp(amazon_raw_doc)

    sents = filter_sents(amazon_doc.sents)
    print(pprint.pformat(sents))

    api_endpoint = "https://dhs-coding-club-imagine-cup.cognitiveservices.azure.com/"
    client = authenticate_client(api_endpoint, API_KEY)
    # key_phrase_extraction_example(client, example_doc=amazon_raw_doc)


if __name__ == "__main__":
    main()
