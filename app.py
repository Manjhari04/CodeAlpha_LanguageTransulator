from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

languages = {
    'English': 'en', 'Hindi': 'hi', 'French': 'fr', 'Spanish': 'es', 'German': 'de',
    'Japanese': 'ja', 'Chinese (Simplified)': 'zh-cn', 'Chinese (Traditional)': 'zh-tw',
    'Tamil': 'ta', 'Telugu': 'te', 'Arabic': 'ar', 'Russian': 'ru', 'Portuguese': 'pt',
    'Korean': 'ko',
}

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        src_lang = request.form['src_lang']
        dest_lang = request.form['dest_lang']
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        translated_text = translated.text
    return render_template("index.html", languages=languages, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
