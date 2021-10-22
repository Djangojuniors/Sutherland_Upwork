import numpy as np
import pdfminer.pdfdocument
import pdfplumber

# import camelot
import tabula
import streamlit as st
import csv

KEY_WORDS = ['CONSOLIDATED RESULTS OF OPERATIONS', 'Income Statement', 'INCOME STATEMENTS',
             'CONSOLIDATED STATEMENTS OF OPERATIONS',
             'CONSOLIDATED STATEMENTS OF INCOME']

# st.write('**SUTHERLAND**')

table_heading = []

filename = r'F:\Upwork\Perdita_Upwork\10 K Docs\Apple.pdf'


def is_bill(self, text):
    counter = 0
    for _ in self.KEY_WORDS:
        if _ in text:
            counter += 1
    return counter


def pages(self):
    try:
        with pdfplumber.open(filename) as _pdf:
            return len(_pdf.pages)
    except pdfminer.pdfdocument.PDFEncryptionError:
        return 0


def extract_all_text(self, page_number):
    with pdfplumber.open(filename) as _pdf:
        _page = _pdf.pages[page_number]
        _text = _page.extract_text()
        if _text is None:
            return ''
        else:
            return _text

def extract_all_tables(self, page_number):
    print(self.pdf_name)
    _pdf_name = self.pdf_name.split('/')[-1]
    # print(os.path.join(settings.MEDIA_ROOT, 'documents', _pdf_name))
    _tables = tabula.read_pdf(filename, pages=page_number, multiple_tables=True)
    # print(_tables[0])
    # print(type(_tables[0]))
    # print("Tables-------------------------------------")
    # if _tables[0]: return _tables[0]
    # else:
    #     return None
    # _tables[0].dropna(subset=['Premium'], inplace=True)
    return _tables[0]
