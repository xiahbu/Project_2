from google.cloud import language
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/henry/Downloads/meta-chassis-364821-66f6ad6f41d5.json"


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")
def analyze_text_entities(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_entities(document=document)

    for entity in response.entities:
        print("=" * 80)
        results = dict(
            name=entity.name,
            type=entity.type_.name,
            salience=f"{entity.salience:.1%}",
            wikipedia_url=entity.metadata.get("wikipedia_url", "-"),
            mid=entity.metadata.get("mid", "-"),
        )
        for k, v in results.items():
            print(f"{k:15}: {v}")
def analyze_text_syntax(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_syntax(document=document)

    fmts = "{:10}: {}"
    print(fmts.format("sentences", len(response.sentences)))
    print(fmts.format("tokens", len(response.tokens)))
    for token in response.tokens:
        print(fmts.format(token.part_of_speech.tag.name, token.text.content))

def classify_text(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.classify_text(document=document)

    for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")

analyze_text_sentiment('Guido van Rossum is great!')
print('\n')
analyze_text_sentiment('I am sad')
print('\n')
analyze_text_sentiment('I feel great!')
print('\n')
analyze_text_sentiment('The exam was so hard')
print('\n')
analyze_text_sentiment('I am hungry')
print('\n')
analyze_text_entities('Picasso was an abstract painter, some of his work are in the Museum of Modern Art in New York')
print('\n')
analyze_text_syntax('Picasso was an abstract painter')
print('\n')
classify_text('ARKit combines device motion tracking, camera scene capture, advanced scene processing, and display'
            ' conveniences to simplify the task of building an AR experience. You can create many kinds of AR '
            'experiences with these technologies using the front or rear camera of an iOS device.')

