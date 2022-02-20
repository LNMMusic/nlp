from spacy.tokens import Doc, Span

# Data Example
data = {
    "words": ["Hello", "world", "!"],
    "spaces":[True, False, False],
    
    "spans":[
        {"label":"GREETING", "index":(0, 2)}
    ]
}

# Document
def DocumentCreate(nlp: object, data: dict) -> object:
    # doc
    doc = Doc(nlp.vocab, words=data["words"], spaces=data["spaces"])

    # spans
    for s in data["spans"]:
        span = Span(doc, s["index"][0], s["index"][1], label=s["label"])
        doc.ents = [span]

    return doc