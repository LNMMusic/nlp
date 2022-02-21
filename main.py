# LIBS
import src
import handlers
import spacy;       from spacy.matcher import Matcher


def main():
    # App
    # nlp = spacy.load("en_core_web_sm");         handlers.add_pipelines(nlp)
    # doc = nlp(handlers.loadTxt("data.txt"))
    
    # # Match
    # matcher = Matcher(nlp.vocab)
    # for key, value in handlers.loadJson("patterns.json",["patterns","B"]).items():
    #     matcher.add(key, value)

    # # Service
    # handlers.doc_metadata(doc, matcher(doc))

    # App
    nlp = src.nlp(model="en_core_web_sm")
    print(nlp.pipe_names)
    
    # matchers and pipelines
    

    # doc
    doc = handlers.loadTxt("data.txt")


main()