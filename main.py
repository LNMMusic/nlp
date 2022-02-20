# LIBS
import handlers
from app            import nlp, matcher
from app.handlers   import doc_metadata


def main():
    # App
    doc = nlp(handlers.loadTxt("data.txt"))
    matches = matcher(doc)

    # Service
    doc_metadata(doc, matches)

main()