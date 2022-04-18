> Pertemuan Minggu 08


# BAB.10 Brief Tour of the Standard Library (Tur Singkat Perpustakaan Standar)

---

## 10.1. Operating System Interface (Antarmuka Sistem Operasi)

---

Modul `os` menyediakan puluhan fungsi untuk berintraksi dengan sistem operasi:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python310'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Pastikan untuk menggunakan gaya `import os` atau `from os import *`. Ini akan menjaga `os.open()` agar tidak membayangi fungsi bawaan `open()` yang beroperasi jauh berbeda.

Fungsi bawaan `dir()` dan `help()` berguna sebagi alat bantu interaktif untuk bekerja dengan modul besar seperti `os`:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>
```

Untuk tugas manajemen berkas dan direktori sehari-hari, modul `shutil` ini menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

---

## 10.2. File Wildcards

---

Modul `glob` ini menyediakan fungsi untuk membuat daftar/file dari pencarian di direktori `wildcard` :

```python
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

---

## 10.3. Command Line Arguments (Argumen Baris Perintah)

---

Skrip utilitas umum sering di perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut `argv` dari modul `sys` sebagai daftar. Sebagai contoh, hasil keluaran berikut dari menjalankan `python demo.py one two three` di baris perintah :

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```

Modul `argparse` menyediakan mekanisme yang lebih baaik lagi untuk memproses argumen baris perintah. Script berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional yang ditampilkan:

```python
import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```

---

## 10.4. Error Output Redirection and Program Termination (Pengalihan Output Kesalahan dan Penghentian Program)

---

Modul `sys` memiliki atribut untuk `stdin, stdout, dan stderr`. Yang terakhir ini berguna untuk mengirimkan peringantan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika `stdout` telah dialihkan:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

Cara paling langsung untuk mengakhiri skrip adalah dengan `sys.exit()`.

---

## 10.5. String Pattern Matching (Pencocokan Pola String)

---

Modul `re` menyediakan alat ekspresi reguler untuk pemrosesan string lanjutan. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

Ketika kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan debug:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

---

## 10.6. Mathematics (Matematika)

---

Modul `math` memberikan akses ke fungsi pustaka C yang mendasari untuk matematika floating point:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

Modul `random` menyediakan alat untuk membuat pilihan acak:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4
```

Modul `statistics` menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```

---

## 10.7. Internet Access (Akses internet)

---

Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah `urllib.request` untuk mengambil data dari URL dan `smtplib` untuk mengirim email:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
...     for line in response:
...         line = line.decode()             # Convert bytes to a str
...         if line.startswith('datetime'):
...             print(line.rstrip())         # Remove trailing newline
...
datetime: 2022-01-01T01:36:47.689215+00:00

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```

---

## 10.8. Dates and Times (Tanggal dan Waktu)

---

Modul `datetime` menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Modul ini juga mendukung objek yang mengerti zona waktu.

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

---

## 10.9. Data Compression (Kompresi Data)

---

penagarsipan data umum dan kompresi secara langsung didukung dengan modul-modul yang ada, antara lain: `:mod: zlib`, `gzip`, `bz2`, `lzma`, `zipfile`, dan `tarfile`.

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

---

## 10.10. Performance Measurement (Pengukuran Kinerja)

---

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Python menyediakan alat pengukuran yang segera menjawab pertanyaan-pertanyaan itu.

Misalnya, untuk menggunakan fitur tuple packing dan unpacking daripada menggunakan pendekatan tradisional untuk bertukar argumen. Modul `:mod: timeit` dengan cepat menunjukkan keunggulan kinerja secara sederhana:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

Berbeda dengan granularity tingkat halus `timeit`, modul `profile`, dan modul `pstats` menyediakan alat untuk mengidentifikasi bagian waktu dalam block kode yang lebih besar.

---

## 10.11. Quality Control (Kontrol kualitas)

---

Modul `doctest` menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam docstrings program. Konstruksi pengujian sesederhana memotong dan menempelkan panggilan biasa beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
```

Modul `unittest` tidak semudah modul `doctest`, tetapi memungkinkan serangkaian pengujian yang lebih komprehensif untuk dipertahankan dalam file terpisah:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests
```

---

## 10.12. Batteries Included

---

Python memiliki filosofi "Batteries Included", ini paling baik dilihat melaluii kemampuan yang canggih dan kuat robust dengan dukungan paket-paket yang lebih besar.

Sebagai contoh:

- Modul `xmlrpc.client` dan `xmlrpc.server` membuat penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama modul, tidak diperlukan pengetahuan atau penanganan XML yang dilakukan.

- Paket `email` adalah pustaka untuk mengelola pesan email, termasuk MIME dan lainnya `RFC 2822` dokumen pesan berbasis.

- Paket json menyediakan dukungan kuat untuk mengurai format pertukaran data populer ini. Modul `csv` mendukung pembacaan dan penulisan berkas secara langsung dalam format Nilai Terpisah-Koma atau CSV, umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh paket `xml.etree.ElementTree`, `xml.dom` dan `xml.sax`.

- Modul `sqlite3` adalah pembungkus untuk pustaka basis data SQLite, menyediakan basis data persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.

- Internasionalisasi didukung oleh sejumlah modul termasuk paket `gettext`, `locale`, dan paket `codecs`.

---

# BAB.11 Brief Tour of the Standard Library - Part II (Tur Singkat Perpustakaan Standar - Bagian II)

Pada Bagian II ini mencakup modul yang lebih canggih dan mendukung kebutuhan pemrograman profesional.

---

## 11.1 Output Formatting (Pemformatan Keluaran)

---

Modul `reprlib` menyediakan versi `repr()` yang disesuaikan untuk tampilan singkat container besar atau bersarang dalam:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"
```

Modul `pprint` menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan objek yang ditentukan pengguna dengan cara yang dapat dibaca oleh penerjemah. Ketika hasilnya lebih panjang dari satu baris, "pretty printer" menambahkan jeda baris dan lekukan untuk mengungkapkan struktur data dengan lebih jelas:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
```

Modul `textwrap` memformat paragraf teks agar sesuai dengan lebar layar yang diberikan:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
```

Modul `locale` mengakses database format data spesifik budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung untuk memformat angka dengan pemisah grup:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'
```

---

## 11.2. Templating (Templating)

---

Modul `string` menyertakan kelas serbaguna `Template` dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna. Formatnya menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan kurung memungkinkan untuk diikuti oleh lebih banyak huruf alfanumerik tanpa spasi.

Menulis $$ membuat satu pelarian $:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'
```

Metode `substitute()` memunculkan `KeyError` ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi mail-merge, data yang diberikan pengguna mungkin tidak lengkap dan metode `safe_substitute()` mungkin lebih tepat. ini akan membuat placeholder tidak berubah jika data hilang:

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'
```

Subkelas template dapat menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
```

Aplikasi lain untuk templating adalah memisahkan logika program dari detail beberapa format output. Hal ini memungkinkan untuk mengganti template khusus untuk file XML files, plain text reports, dan HTML web reports.

---

## 11.3 Working with Binary Data Record Layouts (Bekerja dengan Tata Letak Rekam Data Biner)

---

Modul `struct` ini menyediakan `pack()` dan `unpack()` berfungsi untuk bekerja dengan format rekaman biner yang memiliki panjang variabel.

Contoh berikut menunjukan bagaimana cara loop tajuk header informasi dalam berkas ZIP tanpa menggunakan modul `zipfile`. Kode paket H dan I masing-masing mewakili dua dan empat byte angka yang tidak bertanda unsigned. `<` menunjukan bahwa mereka adalah ukuran standar dan dalam urutan byte little-endian :

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
```

---

## 11.4. Multi-threading

---

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Threads dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I/O secara paralel dengan perhitungan di thread lainnya.

Kode berikut menunjukkan bagaimana modul `threading` tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan :

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

Tantangan utama aplikasi multi-utas atau `multi-threaded` adalah mengordinasikan thread yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronasi termasuk kunci locks, peristiwa event, variabel kondisi, dan semafor.

---

## 11.5. Logging

---

Modul `logging` menawarkan sistem logging yang berfitur lengkap dan fleksibel. Paling sederhana, catatan log pesan dikirim ke berkas atau ke `sys.stderr`:

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

Menghasilkan output berikut :

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

Secara default, pesan informasi dan debugging ditekan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk perutean pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih perutean yang berbeda berdasarkan prioritas pesan: `DEBUG`, `INFO`, `WARNING`, `ERROR`, dan `CRITICAL`.

---

## 11.6. Weak References

---

Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir dihilangkan.

Pendekatan ini bekerja dengan baik untuk sebagian besar aplikasi tetapi kadang-kadang ada kebutuhan untuk melacak objek hanya selama mereka digunakan oleh sesuatu yang lain. Sayangnya, hanya melacak mereka membuat referensi yang membuatnya permanen. Modul `weakref` ini menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, itu secara otomatis dihapus dari tabel weakref dan callback dipicu untuk weakref. Aplikasi yang umum termasuk caching objek yang mahal untuk dibuat:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python310/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
```

---

## 11.7 Tools for Working with Lists (

---

Modul `array` menyediakan objek `array()` yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih ringkas. Contoh berikut menunjukkan array angka yang disimpan sebagai dua byte angka biner tidak bertanda (typecode `"H"`) daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

Modul `collections` menyediakan objek `deque()` yang seperti daftar dengan penambahan yang lebih cepat dan muncul dari sisi kiri tetapi pencarian yang lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas :

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

Selain implementasi daftar alternatif, perpustakaan juga menawarkan alat lain seperti modul `bisect`dengan fungsi untuk memanipulasi daftar yang diurutkan :

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

Modul `heapq` menyediakan fungsi untuk mengimplementasikan heap berdasarkan daftar reguler. Entri bernilai rendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan pengurutan daftar secara lengkap :

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```

## 11.8. Decimal Floating Point Arithmetic (Aritmatika Pecahan Floating Point Desimal)

Modul `decimal` menawarkan tipe data `decimal` untuk aritmatika decimal floating point. Dibandingkan dengan implementasi float built-in dari floating point biner, kelas ini sangat membantu untuk :

- aplikasi keuangan dan penggunaan lain yang memerlukan representasi desimal yang tepat,
- kontrol atas presisi,
- kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
- pelacakan tempat desimal yang signifikan, atau
- aplikasi di mana pengguna mengharapkan hasil yang sesuai dengan perhitungan yang dilakukan dengan tangan.

Contohnya, menghitung pajak 5% untuk biaya telepon 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Perbedaan menjadi signifikan jika hasilnya dibulatkan ke sen terdekat :

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```

Hasil Desimal mempertahankan angka nol, secara otomatis menyimpulkan signifikansi empat tempat dari perkalian dengan signifikansi dua tempat. Desimal mereproduksi matematika seperti yang dilakukan dengan tangan dan menghindari masalah yang dapat muncul ketika titik mengambang biner tidak dapat secara tepat mewakili jumlah desimal.

Representasi yang tepat memungkinkan kelas Desimal untuk melakukan perhitungan modulo dan tes kesetaraan yang tidak cocok untuk floating point biner :

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```

Modul `decimal` menyediakan aritmatika dengan presisi sebanyak yang diperlukan:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```

---
