import machinetranslation
from flask import Flask, render_template, request

app = Flask(__name__)
translator = machinetranslation.Translator()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/englishToFrench", methods=['GET'])
def e_2_f():
    engtext = request.args.get('engtext')
    frentext = translator.english_to_french(engtext)
    return frentext

@app.route("/frenchToEnglish", methods=['GET'])
def f_2_e():
    frenchtext = request.args.get('frenchtext')
    engtext = translator.french_to_english(frenchtext)
    return engtext
    
if __name__ == "__main__":
    app.run(debug=True)
