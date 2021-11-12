from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/set', methods=['POST'])
def foo():
    text = request.json
    text = text['text']
    print(text)
    # return jsonify(data)
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    from rake_nltk import Metric, Rake
    r = Rake(language="russian")
    r.extract_keywords_from_text(text)
    mas = r.get_ranked_phrases()
    set2 = set()
    for item in mas:
        if not "nan" in str(item).replace(" nan ", " "):
            set2.add(str(item).replace(" nan ", " "))
    mas = list(set2)
    print("Исходный текст:")
    print(text)
    print("Результат работы Rake:")
    print(str(mas))
    # print(mas[0])
    newmas=[]
    for item in mas:
        if len(item)>26:
            newmas.append(item)
    return jsonify(newmas), 200, {'Content-Type': 'application/json'}
if __name__ == '__main__':
    app.run(host='0.0.0.0')
app.run(host='0.0.0.0')