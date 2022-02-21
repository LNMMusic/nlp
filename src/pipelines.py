# LIBS
from spacy.language import Language
from spacy.tokens   import Span


# Pipelines
@Language.component("animal_component")
def animal_component_function(doc):
    matches = matcher(doc)
    
    # new entities
    spans = [Span(doc, s, e, label="ANIMAL") for _, s, e in matches]
    doc.ents = spans
    return doc

# Export
pipelines = [
    {"name": "custom_component", "after":"ner"}
]