## In this file I'll store all the data processed

import csv
from process import *

all_data = list()
all_data.append(['ID', 'Name', 'Rating', 'Price - pounds', 'Price - euros', 'Image URL', 'Text - English' , 'Text - Spanish', 'Text - Catalan'])

for b in library:
    all_data.append(b.get_all_info())

with open('books_info.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(all_data)

