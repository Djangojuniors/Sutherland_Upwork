# from date_extractor import extract_date
import pandas as pd
import datetime
import sys
import re
import spacy

nlp = spacy.load("en_core_web_sm")

csv_file = r"10 K Docs\Starbucks-35-table-0.csv"

extracted_dates = []
test = []

var = pd.read_csv(csv_file)
new_df = pd.read_csv(csv_file)
for num, i in enumerate(var.columns):
    temp = []
    if num > 1:
        val = list(var[i].values)
        val = [i  for i in val if str(i) != 'nan']
        for v in val:
            year = nlp(str(v))
            for entity in year.ents:
                if entity.label_ == 'DATE':
                    temp.append(v)
    if len(temp) > 0:
        date = "".join(temp)
        new_df = new_df.rename({i: date}, axis=1)
        for k in temp:
            new_df = new_df.replace(k, '', regex=True)
        new_df.to_csv('output_csv/Starbucks-35-table-0.csv')
# print(test)
# date_format = " ".join(str(x) for x in test)
# print(date_format)