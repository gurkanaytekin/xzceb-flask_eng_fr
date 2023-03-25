from machinetranslation import translator
from flask import Flask, render_template, request
from ibm_watson import LanguageTranslatorV3
import json
import logging

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.language_translator.translate(
    text=textToTranslate,
    model_id='en-fr').get_result()
    return translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.language_translator.translate(
    text=textToTranslate,
    model_id='fr-en').get_result()
    return translation

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    translation = translator.language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-es').get_result()
    return translation

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
