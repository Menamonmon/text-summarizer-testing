from flask import Flask, request
from azure_client import create_azure_nlp_client
from load_api_key import load_api_key

app = Flask(__name__)

API_KEY = load_api_key()
ENDPOINT = "https://dhs-coding-club-imagine-cup.cognitiveservices.azure.com/"
nlp_client = create_azure_nlp_client(ENDPOINT, API_KEY)


@app.route("/", methods=["POST"])
def index():
    return request.form
