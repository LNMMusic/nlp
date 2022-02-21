# LIBS
from spacy.language import Language


# Pipelines
@Language.component("custom_component")
def custom_component_function(doc):
    
    print("Doc Length:", len(doc))

    return doc

def add_pipelines(nlp: object):
    nlp.add_pipe("custom_component", first=True)