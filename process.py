## In this file I'll process the data scraped

from scrape import *
from deep_translator import GoogleTranslator


for id, b in enumerate(library):
    ### Price conversion to €

    euros = round(b.price['pound'] * 1.12652115125, 2)
    b.set_price('euros', euros)


    ### Set ID for each book (booring way)

    # b.ID = id

    ### Set ID for each book (cool way)

    b.generate_cool_id(library)


    ### Generate text of the book

    input = "The text of " + b.name + " is:"
    print(input)
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': input,
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'
        #headers={'api-key': '458c9964-b8e7-4564-8c89-566618d88a4a'
        }
    )
    if (r.status_code == 200):
        text_en = r.json()['output']
        print("Text correct!")
    else:
        text_en = "Error getting the text..."
        print(text_en)

    b.set_text('english', text_en)

    ### Translate the text

    text_sp = GoogleTranslator(source='english', target='spanish').translate(text_en)
    b.set_text('spanish', text_sp)
    text_cat = GoogleTranslator(source='english', target='catalan').translate(text_en)
    b.set_text('catalan', text_cat)


