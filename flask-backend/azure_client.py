import os
import json
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def create_azure_nlp_client(endpoint, api_key):
    credential = AzureKeyCredential(api_key)
    return TextAnalyticsClient(endpoint=endpoint, credential=credential)
