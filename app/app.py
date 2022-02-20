# LIBRARIES
import  spacy
from    spacy.matcher import Matcher


class App:
    def __init__(self, nlp:str, matcher:dict, filename:str):
        # object
        self.nlp      = spacy.load(nlp)
        self.matcher  = Matcher(self.nlp.vocab)
        self.patterns = [self.matcher.add(k, v) for k, v in matcher.items()]

        self.doc      = filename


    # Constructor
    def Load(self):
        with open(self.doc, mode="r") as f:
            self.doc = self.nlp(f.read())
    
    # Methods   [matcher]
    def Matches(self) -> object:
        return self.matcher(self.doc.doc)

    #           [document]
    def __metadata_token(self):
        for token in self.doc:
            print("token -> {:<12} - pos -> {:<10} - dependency -> {:<10} - head -> {}".format(
                token.text,
                token.pos_,
                token.dep_,
                token.head
            ))
    def __metadata_entities(self):
        for ent in self.doc.ents:
            print(ent)
    
    def metadata(self, matches:object):
        print("Tokens:")
        self.__metadata_token()
        print("\nEntities:")
        self.__metadata_entities()
        print("\nMatches:")
        for match_id, start, end in matches:
            span = self.doc[start:end]
            print("id -> {:<30} - span -> {}".format(
                match_id,
                span
            ))

# VOCAB [example of its functionallity] [if detects its an string store its hash in a new map and use it on the hash map]
# nlp.vocab.strings.add("coffee")                       # map of string and hashes
# coffee_hash = nlp.vocab.strings["coffee"]             # access to hash [string encoded]       THIS IS A LEXEME
# coffee_string = nlp.vocab.strings[coffee_hash]        # use hash in map

# # App [main.py]
# from app import App


# doc = App(
#     nlp="en_core_web_sm",
#     matcher= handlers.loadJson("patterns.json", ["patterns", "B"]),
#     filename="data.txt"
# )
# doc.Load()

# doc.metadata(doc.Matches())