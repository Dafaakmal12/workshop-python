> Responsi

1. Import csv dan urlib.request
2. Definisikan untuk  path url atau file dataset
3. kemudian mendownload dan menampilkan data
    ```python
        import csv
    import urllib.request

    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/zillow.csv"
    response = urllib.request.urlopen(url)
    read = csv.reader(response)

    for row in read:
        print(row)
    ```

4. Dataset telah didownload dan ditampilkan.