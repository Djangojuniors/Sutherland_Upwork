import numpy as np
import pdfminer.pdfdocument
import pdfplumber
import camelot
import tabula
# import streamlit as st
import csv
from predict_table import detect_tables

KEY_WORDS = ['CONSOLIDATED RESULTS OF OPERATIONS',
             'CONSOLIDATED STATEMENTS OF OPERATIONS',
             'CONSOLIDATED STATEMENTS OF INCOME']

# st.write('**SUTHERLAND**')

table_heading = []
# uploaded_file = st.file_uploader("Choose a file", "pdf")

filename = r'10 K Docs\Starbucks.pdf'

with pdfplumber.open(filename) as _pdf:
    numd = 0
    for pages in _pdf.pages:
        _text = pages.extract_text()
        for d in KEY_WORDS:
            if d.lower() in _text.lower():
                print(d)
                print(numd)
                detect_tables(pdf_file=filename, pg=numd + 1)

                # table_heading.append(d)
                # labels_in_pages = pages.extract_text()
                print(pages)
                # st.write(labels_in_pages)
        numd+=1


