import numpy as np
import pdfminer.pdfdocument
import pdfplumber

# import camelot
# import tabula
import streamlit as st
import csv

KEY_WORDS = ['CONSOLIDATED RESULTS OF OPERATIONS', 'Income Statement', 'INCOME STATEMENTS',
             'CONSOLIDATED STATEMENTS OF OPERATIONS',
             'CONSOLIDATED STATEMENTS OF INCOME']

# st.write('**SUTHERLAND**')

table_heading = []
# uploaded_file = st.file_uploader("Choose a file", "pdf")

filename = r'F:\Upwork\Perdita_Upwork\10 K Docs\Apple.pdf'

with pdfplumber.open(filename) as _pdf:
    for pages in _pdf.pages:
        _text = pages.extract_text()
        # print(_text)

        for d in KEY_WORDS:
            if d in _text:
                table_heading.append(d)
                labels_in_pages = pages.extract_text()
                # print(pages, labels_in_pages)
                # print(type(pages))
                # st.write(labels_in_pages)
                with open('invoice.csv', 'w') as invoice:
                    writer = csv.writer(invoice)
                    writer.writerow(labels_in_pages)




