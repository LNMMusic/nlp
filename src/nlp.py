# LIBS
import spacy;   from spacy.matcher import Matcher, PhraseMatcher
from .handlers  import json
from .pipelines import pipelines


# NLP
def nlp(model:str) -> object:
    # nlp
    nlp = spacy.load(model)
    
    # matcher
    matcher = new_matcher(
        nlp = nlp,
        mode= "phrase",
        patterns= json.loadJson('patterns.json', ['patterns', 'B']),
    )

    # pipelines
    for pipe in pipelines:
        nlp.add_pipe(**pipe)

    return nlp

def new_matcher(nlp:object, mode:str, patterns:dict) -> object:
    if mode == "phrase":
        matcher = PhraseMatcher(nlp.vocab)

        for name, pattern in patterns:
            matcher.add(name, list(nlp.pipe(pattern)))

    elif mode == "single":
        matcher = Matcher(nlp.vocab)

        for name, pattern in patterns:
            matcher.add(name, pattern)
    
    return matcher