import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/IDCJAC0010_087031_2019_Data.csv'
filename2 = 'data/IDCJAC0011_087031_2019_Data.csv'

dates, highs, lows = [], [], []
#Open and read the content of the file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader) #read the header

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    for row in reader: #read each row of the data
        try:
            year = int(row[2])
            month = int(row[3])
            day = int(row[4])

            high = float(row[5])
        except ValueError:
            print("Missing data Error")
        else:
            date = datetime(year, month, day)
            # print(str(date))
            dates.append(date)
            highs.append(high)

with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            low = float(row[5])
        except ValueError:
            print("Missing Data Error")
        else:
            lows.append(low)
  
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.2)

title = "Daily High Tempterature - 2019"
plt.title(title, fontsize=16)
plt.xlabel("", fontsize=8)
fig.autofmt_xdate()
plt.ylabel("Temperature in Celsius(C)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()