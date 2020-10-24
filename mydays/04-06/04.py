from collections import defaultdict, namedtuple, Counter, deque
import csv
import random
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

Snapshot = namedtuple("snapshot", "datetime flow compression T_in T_out pressure")

filelocation = "/home/joseph/projects/100daysofcode-with-python-course/csvfiles/"
thisfile = filelocation + "Archiv_13.csv"
day = []

with open(thisfile, newline="", encoding="utf-16") as csvfile:
    myreader = csv.reader(csvfile, delimiter="\t", quotechar="|")
    for row in myreader:
        print(row[1])
        day.append(Snapshot(row[1], row[3], row[5], row[6], row[7], row[8]))

datetime = []
flow = []
compression = []
T_in = []
T_out = []
pressure = []
for count, enum_row in enumerate(day):
    datetime.append(day[count].datetime)
    flow.append(day[count].flow)
    compression.append(day[count].compression)
    T_in.append(day[count].T_in)
    T_out.append(day[count].T_out)
    pressure.append(day[count].pressure)

fig, ax = plt.subplots(constrained_layout=True)

with PdfPages(filelocation + "graph.pdf") as export_pdf:
    ax.plot(datetime, flow, datetime, compression, datetime, T_in, datetime, T_out, datetime, pressure)
    secax = ax.secondary_xaxis('top')
    export_pdf.savefig()
