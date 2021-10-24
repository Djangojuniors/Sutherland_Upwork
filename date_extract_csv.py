# from date_extractor import extract_date
import pandas as pd
import datetime
import sys
import re
csv_file = r"10 K Docs\Apple-34-table-0.csv"
extracted_dates = []

months_choices = []
for i in range(1,13):
    months_choices.append(datetime.date(2008, i, 1).strftime('%B'))
# print(months_choices)

# sys.exit()


var = pd.read_csv(csv_file)
for num, i in enumerate(var.columns):
    temp = []
    if num > 1:
        # print(var[i].values)
        val = list(var[i].values)
        val = [i  for i in val if str(i) != 'nan']
        for month in months_choices:
            filter = re.compile(month.lower())
            for v in val:
                # print(v)
                if filter.match(v.lower()):
                    print(v)

        # for i in val:
        #     val = i
        #     if any(val for items in months_choices):
        #         print(i)
            # if i.find(str(months_choices)):
            #     print(i)


                # print(j)
        # print(val)



        # for v in val:
            # date = extract_date(v)
            # print(date)

            # print(val)
            # val = ','.join(val)
            # print(val)
            # print(type(val))
            # break
