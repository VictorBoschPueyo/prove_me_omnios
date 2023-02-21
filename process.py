## In this file I'll process the data scraped

from scrape import *


### Set ID for each book and price conversion
for id, b in enumerate(library):
    euros = round(b.price['pound'] * 1.12652115125, 2)

    b.ID = id
    b.set_price('euros', euros)


### Generate text of the book







### Translate text










