from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import googletrans

app = Flask(__name__, template_folder='template', static_folder='static')

translator = Translator()

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        inputData = request.args.get('inputData')
        srcLanguage = request.args.get('srcLanguage')
        destLanguage = request.args.get('destLanguage')
    languages = googletrans.LANGUAGES
    languagesValues = list(googletrans.LANGUAGES.values())
    if srcLanguage != None and destLanguage != None and inputData != None:
        infos = translator.translate(inputData)
        detectSrc = languages[infos.src]
        dest = list(languages.keys())[list(languages.values()).index(destLanguage)]

        if srcLanguage == "auto":
            print(srcLanguage)
            result = translator.translate(inputData, src=infos.src, dest=dest)
        else:
            src = list(languages.keys())[list(languages.values()).index(srcLanguage)]
            if infos.src != src:
                result = translator.translate(inputData, src=infos.src, dest=dest)
            else:
                result = translator.translate(inputData, src=src, dest=dest)
                
        translation = result.text
        return jsonify({'translation': translation, 'detectSrc': detectSrc, 'src': srcLanguage})
    return render_template('index.html', languages=languagesValues)

if __name__=='__main__':
    app.run()

