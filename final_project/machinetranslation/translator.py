import os
import logging
from ibm_watson import LanguageTranslatorV3 #Watson Module
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator #IBM Cloud Auth SDK
from dotenv import load_dotenv #Envoirement for Python module

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def get_translate(text_to_translate, model_id):
    """Abstraction for translate method"""
    return language_translator.translate(
    text=text_to_translate,
    model_id=model_id).get_result()

logging.info("Ready")
