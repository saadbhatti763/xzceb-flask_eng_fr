from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    engtext = request.args.get('textToTranslate')
    # Write your code here
    frentext = translator.english_to_french(engtext)
    return frentext

@app.route("/frenchToEnglish")
def frenchToEnglish():
    frentext = request.args.get('textToTranslate')
    # Write your code here
     engtext = translator.french_to_english(frentext)
     return engtext

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
