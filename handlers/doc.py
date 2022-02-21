def metadata_token(doc: object):
    for token in doc:
        print("token -> {:<12} - pos -> {:<10} - dependency -> {:<10} - head -> {}".format(
            token.text,
            token.pos_,
            token.dep_,
            token.head
        ))
def metadata_entities(doc: object):
    for ent in doc.ents:
        print(ent)


def doc_metadata(doc: object, matches: object):
    print("Tokens:")
    metadata_token(doc)

    print("\nEntities:")
    metadata_entities(doc)

    print("\nMatches:")
    for match_id, start, end in matches:
        span = doc[start:end]
        print("id -> {:<30} - span -> {}".format(
            match_id,
            span
        ))