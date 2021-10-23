from date_extractor import extract_date
import pandas as pd


csv_file = r"10 K Docs\Apple-34-table-0.csv"
var = pd.read_csv(csv_file)
for num, i in enumerate(var.columns):
    temp = []
    if num > 1:
        # print(var[i].values)
        val = list(var[i].values)
        val = [i  for i in val if str(i) != 'nan']
        for v in val:
            date = extract_date(v)
            print(date)

            # print(val)
            # val = ','.join(val)
            # print(val)
            # print(type(val))
            # break
