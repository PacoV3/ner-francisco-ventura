import spacy
import json


def ner_analysis(sentences: list[str]) -> dict:
    # Load the NER model
    nlp = spacy.load("es_core_news_sm")

    analysis = []
    for sentence in sentences:
        entities = {}
        # Process the sentence text
        text = sentence
        doc = nlp(text)

        # Extract the named entities
        for ent in doc.ents:
            entities[ent.text] = ent.label_
        analysis.append({"oracion": sentence, "entidades": entities})

    return {"resultado": analysis}


def main():
    # Process the text
    sentences = [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera.",
    ]
    # Serializing json
    json_object = json.dumps(ner_analysis(sentences), indent=4)
    
    # Writing to sample.json
    with open("./data/processed/output_1.json", "w", encoding="latin-1") as outfile:
        outfile.write(json_object)


if __name__ == "__main__":
    main()
