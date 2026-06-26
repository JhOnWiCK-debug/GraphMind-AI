import spacy

nlp = spacy.load(
    "en_core_web_sm"
)

def extract_entities(text):

    doc = nlp(text)

    entities = []

    for ent in doc.ents:

        entities.append(
            (
                ent.text,
                ent.label_
            )
        )

    return entities
def extract_question_entity(
    graph,
    question
):

    question = question.lower()

    for node in graph.nodes:

        if str(node).lower() in question:

            return node

    return None
    