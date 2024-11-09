import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Jinstagram.settings")
django.setup()

from chart.models import TableApp
from chart.models import Samsung

# # TableApp
# with open('G:\\Jinstagram\\Jinstagram\data\\table.csv') as csv_file_sub_categories:
#     rows = csv.reader(csv_file_sub_categories)
#     next(rows, None)
#     for row in rows:
#         TableApp.objects.create(
#             name=row[0],
#             position=row[1],
#             office=row[2],
#             age=int(row[3]),
#             startdate=row[4],
#             salary=row[5],
#         )
#         print(row)

# Samsung
with open('G:\\Jinstagram\\Jinstagram\data\\samsung.csv') as f:
    rows = csv.reader(f)
    next(rows, None)
    for row in rows:
        Samsung.objects.create(
            Date=row[0],
            Close_price=row[1],
            Individual=row[2],
            Foreigner=row[3],
            Organ=row[4],
            Finance=row[5],
            Insurance=row[6],
            Investment=row[7],
            Bank=row[8],
            Other_finance=(row[9]),
            Pension_fund=row[10],
            Other_corporations=row[11],
            Other_foreiner=(row[12]),
            Private_fund=row[13],
        )
        print(row)