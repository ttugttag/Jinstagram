import csv
import pandas as pd
# from chart.models import TableApp

with open('G:\\Jinstagram\\Jinstagram\data\\table.csv','r') as f:
    dr = csv.DictReader(f)
    s = pd.DataFrame(dr)
    # print(s)

# print(s)

ss = []
for i in range(len(s)):
    print(s["name"])
    # st = (s['name'][i], s['position'][i], s['office'][i], s['age'][i], s['startdate'][i], s['salary'][i])
    # ss.append(st)

# print(ss)

# for i in range(len(s)):
#     TableApp.objects.create(name=ss[i][0], position=ss[i][1], office=ss[i][2], age=ss[i][3], startdate=ss[i][4], salary=ss[i][5])