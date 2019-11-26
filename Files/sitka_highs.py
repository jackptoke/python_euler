import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    #Get high temperature from this file
    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        low = int(row[6])
        high = int(row[5])
        dates.append(current_date)
        lows.append(low)
        highs.append(high)
    
    #Plot the high temperature
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.8)
    ax.plot(dates, lows, c='blue', alpha=0.6)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.4)

    #Format the plot
    plt.title("Daily high and low temperature, July 2018", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature in (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
    