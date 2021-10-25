import torch
from transformers import pipeline
import pandas as pd

tqa = pipeline(task="table-question-answering",
               model="google/tapas-base-finetuned-wtq")
table = pd.read_csv("output_csv\Jp Morgan-50-table-0.csv")
table = table.astype(str)


query = ["What is the Net Revenues on 2018?",
         "What is the total Net revenues in 2017?"]
answer = tqa(table=table, query=query)
for ans in answer:
    print(ans["answer"])