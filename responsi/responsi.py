import csv
import urllib.request

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/zillow.csv"
response = urllib.request.urlopen(url)
read = csv.reader(response)

for row in read:
    print(row)
