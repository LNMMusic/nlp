# LIBRARIES
import  spacy;        import json
from    spacy.matcher import Matcher


# MODEL
nlp = spacy.load("en_core_web_sm")

# MATCHER [recives document]
matcher = Matcher(nlp.vocab)
with open("patterns.json", mode="r") as json_file:
    patterns = json.load(json_file)["patterns"]["B"]
    for key, value in patterns.items():
        matcher.add(key, value)