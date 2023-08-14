from flask import Flask, jsonify, request
# import src.functions.ner_nltk as ner
import src.functions.ner_spacy as s_ner

app = Flask(__name__)


@app.route("/ner/spacy", methods=['POST'])
def ner_spacy_analysis():
    input = request.json
    return jsonify(s_ner.ner_analysis(input["oraciones"]))


if __name__ == "__main__":
    app.run(debug=True)
