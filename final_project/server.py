from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """Enghlish to French translator method"""
    text_to_translate = request.args.get('textToTranslate')
    translation = translator.language_translator.translate(
    text=text_to_translate,
    model_id='en-fr').get_result().get("translations")[0].get("translation")
    return translation

@app.route("/frenchToEnglish")
def french_to_english():
    """French to English translator method"""
    text_to_translate = request.args.get('textToTranslate')
    translation = translator.language_translator.translate(
    text=text_to_translate,
    model_id='fr-en').get_result().get("translations")[0].get("translation")
    return translation

@app.route("/")
def render_index_page():
    """Render Index Method"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
