> Pertemuan Minggu 12


# Jupyter Documentation

Selamat datang di dokumentasi Jupyter. ini bertindak sebagai dokumentasi "meta" untuk ekosistem Jupyter. 


## Jupyter

---
Perangkat lunak gratis, standar terbuka, dan layanan web untuk komputasi interaktif di semua bahasa pemrograman

`JupyterLab` adalah lingkungan pengembangan interaktif berbasis web terbaru untuk buku catatan, kode, dan data. Antarmukanya yang fleksibel memungkinkan pengguna untuk mengonfigurasi dan mengatur alur kerja dalam ilmu data, komputasi ilmiah, jurnalisme komputasi, dan pembelajaran mesin. Desain modular mengundang ekstensi untuk memperluas dan memperkaya fungsionalitas.

`Notebook Jupyter` adalah aplikasi web asli untuk membuat dan berbagi dokumen komputasi. Ini menawarkan pengalaman yang sederhana, efisien, dan berpusat pada dokumen.

---

**Language of choice**

Jupyter mendukung lebih dari 40 bahasa pemrograman, termasuk Python, R, Julia, dan Scala.

**Share notebooks**

Buku catatan dapat dibagikan dengan orang lain menggunakan email, Dropbox, GitHub, dan Jupyter Notebook Viewer .

**Interactive output**

Kode Kita dapat menghasilkan keluaran yang kaya dan interaktif: HTML, gambar, video, LaTeX, dan jenis MIME khusus.

**Big data integration**

Manfaatkan alat data besar, seperti Apache Spark, dari Python, R, dan Scala. Jelajahi data yang sama dengan pandas, scikit-learn, ggplot2, dan TensorFlow.


---


## Installing Jupyter

Alat Project Jupyter tersedia untuk instalasi melalui Python Package Index , repositori perangkat lunak terkemuka yang dibuat untuk bahasa pemrograman Python.

Halaman ini menggunakan instruksi dengan `pip`, alat instalasi yang direkomendasikan untuk Python . Jika Kita memerlukan manajemen lingkungan bukan hanya instalasi, lihat `conda` , `mamba` , dan `pipenv`.

---

### JupyterLab
---

Instal JupyterLab dengan pip:

```python
pip install jupyterlab
```

Setelah terinstal, luncurkan JupyterLab dengan:

```python
jupyter-lab
```
---
 ### Jupyter Notebook

---

Instal Notebook Jupyter klasik dengan:

```python
pip install notebook
```

Untuk menjalankan buku catatan:

```python
jupyter notebook
```
---
### Voila

---
Instal Voilà dengan:

```python
pip install voila
```
---
### JupyterHub
---


`JupyterHub` menghadirkan kekuatan notebook ke grup pengguna. Ini memberi pengguna akses ke lingkungan dan sumber daya komputasi tanpa membebani pengguna dengan tugas instalasi dan pemeliharaan.

`JupyterHub` berjalan di cloud atau di perangkat keras Anda sendiri, dan memungkinkan untuk menyajikan lingkungan ilmu data yang telah dikonfigurasi sebelumnya kepada pengguna mana pun di dunia. Ini dapat disesuaikan dan terukur, dan cocok untuk tim kecil dan besar, kursus akademik, dan infrastruktur skala besar.

---

#### Fitur utama JupyterHub

---

`Dapat disesuaikan` - JupyterHub dapat digunakan untuk melayani berbagai lingkungan. Ini mendukung lusinan kernel dengan server Jupyter, dan dapat digunakan untuk melayani berbagai antarmuka pengguna termasuk Notebook Jupyter, Jupyter Lab, RStudio, nteract, dan banyak lagi.

`Fleksibel` - JupyterHub dapat dikonfigurasi dengan otentikasi untuk memberikan akses ke sebagian pengguna. Otentikasi dapat dipasang, mendukung sejumlah protokol otentikasi (seperti OAuth dan GitHub).

`Scalable` - JupyterHub ramah terhadap container, dan dapat digunakan dengan teknologi container modern. Itu juga berjalan di Kubernetes, dan dapat berjalan dengan hingga puluhan ribu pengguna.

`Portable` - JupyterHub sepenuhnya open-source dan dirancang untuk dijalankan di berbagai infrastruktur. Ini termasuk penyedia cloud komersial, mesin virtual, atau bahkan perangkat keras laptop Anda sendiri.

Kode dan teknologi dasar JupyterHub dapat ditemukan di repositori JupyterHub . Repositori ini dan dokumentasi JupyterHub berisi lebih banyak informasi tentang internal JupyterHub, penyesuaiannya, dan konfigurasinya.

---

# STRUKTUR DATA

---

Pada BAB ini menjelaskan beberapa hal mengenai struktur data pada python dan lain - lain. Struktur data adalah cara menyimpan dan mengatur data secara terstruktur pada sistem komputer atau database sehingga lebih mudah diakses.

---
## 5.1. Daftar List :clipboard
---
Berikut ini merupakan daftar list yang ada pada python:

`list.append(x)` berguna untuk menambahkan anggota/item ke dalam list. tepatnya pada akhir list.

`list.extend(iterable)` berfungsi untuk menambahkan list dalam 1(satu) kata  dan deretan angka menjadi nilai sebuah list atau memperpanjang daftar list dengan menambahkan semua item dari iterable. 

`list.insert(i, x)` berfungsi untuk memasukkan sebuah item ke dalam list pada posisi tertentu. Argumen pertama dalam parameter `i` merupakan sebuah indeks dari elemen sebelum dimasukkan.

`list.remove(x)` berfungsi menghapus item `x` dari daftar list. perintah tersebut akan menampilkan output `ValueError` ketika tidak ada item pada list.

`list.pop([i])` berfungsi menghapus item pada posisi yang diberikan dalam daftar, dan dikembalikan. Jika tidak ada indeks yang ditentukan, `a.pop()` akan menghapus dan mengembalikan item terakhir dalam daftar list.

`list.clear()` berfungsi menghapus semua item dari daftar list.

`list.index(x[, start[,end]])` berfungsi mengembalikan indeks dari `0` dalam daftar item pertama yang nilainya sama dengan `x`.

`list.count(x)` berfungsi mengembalikan atau menghitung nilai berapa kali item `x` yang muncul dalam daftar.

`list.sort(*, key=None, reverse=False)` berfungsi mengurutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan sesuai customization).

`list.reverse()` berfungsi mengembelikan elemen daftar list pada tempatnya.

`list.copy()` berfungsi mengembalikan salinan daftar list yang dangkal.

Kemudian berikut ini merupakan contoh dari sebagian penggunaan dari metode daftar list:

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
```

Untuk metode seperti `insert`, `remove`, atau `sort` hanya mengubah daftar list tidak memiliki nilai pengembalian yang dicetak dimana nilai yang dikembalikan adalah standar `None`. 

---

### 5.1.1. Menggunakan Daftar Lists sebagai Tumpukan (Stacks)

---

Stack adalah kumpulan data yang terurut sesuai bagaimana data tersebut ditambahkan atau dihapus. Proses pada stack terjadi pada satu ujung. di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out").  Sebagai contoh:

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```
---

### 5.1.2. Menggunakan Daftar Lists sebagai Antrian (Queues)

---

Queue (Antrian) adalah kumpulan data yang berurut dimana penambahan data baru berada di satu ujung bernama ekor atau rear. Seperti halnya Stack, Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil namun, daftar tidak efisien untuk tujuan ini. Sebagai contoh:

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```
---
### 5.1.3. Daftar List (Comprehensions)

---

List comprehension adalah  untuk mendefinisikan dan membuat list di Python. List comprehension terdiri dari sebuah ekspresi diikuti oleh pernyataan `for` yang diletakkan di dalam tanda kurung `[ ]`.Dengan menggunakan list comprehension kita bisa membuat list secara otomatis dalam satu baris perintah saja. 

Contoh membuat daftar squares, seperti:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Perhatikan bahwa ini akan membuat (atau menimpa) variabel bernama `x` yang masih ada setelah loop selesai. Untuk itu dapat menghitung daftar squares secara ringkas tanpa efek samping menggunakan:

```python
squares = list(map(lambda x: x**2, range(10)))
```

atau

```python
squares = [x**2 for x in range(10)]
```

Contoh, listcomp ini menggabungkan elemen dari dua daftar jika tidak sama:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

sama juga dengan:

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

Jika ekspresi adalah tuple (mis. (x, y) dalam contoh sebelumnya), ekspresi tersebut harus diberi kurung.

```python
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Pemahaman daftar list comprehensions dapat berisi ekspresi kompleks dan fungsi bersarang seperti:

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```
---
### 5.1.4. Pemahaman Daftar List Comprehensions Bersarang (Nested)

---

Daftar list comprehension dapat berupa ekspresi acak arbitrary, berikut contoh matriks 3x4 atau 3 list 4 length :

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

berikut akan mengubah baris dan kolom:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

atau menggunakan listcomp bersarang dievaluasi dalam konteks for yang mengikutinya, jadi contoh ini setara dengan:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

atau sama dengan:

```python
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

menggunakan Fungsi zip() :

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```
---
## 5.2. Pernyataan del

---

Pernyataan `del` dapat digunakan untuk menghapus item dari daftar list atau menghapus seluruh daftar list. 

Sebagai contoh:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

`del` juga dapat digunakan untuk menghapus seluruh variabel:

```python
>>> del a
```
---
## 5.3. Tuples dan Urutan Sequences

---

Tuple adalah tipe data urutan objek Python yang tidak berubah. Perbedaan utama antara tupel dan daftarnya adalah bahwa tupel tidak dapat diubah tidak seperti List Python. sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma.

contoh :

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
```

Seperti yang kita lihat, pada output tuple selalu ditampilkan dengan tanda kurung, Meskipun tuple mungkin mirip dengan daftar, tuple sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. 

Masalah khusus adalah pembangunan tuple yang mengandung 0 atau 1 item Tuple kosong dibangun oleh sepasang kurung kosong; tupel dengan satu item dikonstruksi dengan mengikuti nilai dengan koma.

Sebagai contoh:

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

```python
>>> x, y, z = t
```


---
## 5.4. Sets

---

Python juga menyertakan tipe data untuk sets. Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. fungsi set() dapat digunakan untuk membuat himpunan. Catatan: untuk membuat himpunan kosong Anda harus menggunakan `set()`, bukan `{}`.

Berikut ini adalah demonstrasi singkat:

```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

Seperti halnya untuk list comprehensions, set comprehensions juga didukung:

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```
---
## 5.5. Dictionaries

---

Operasi utama pada kamus dictionary adalah menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan kunci key. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan _del_. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan.

Contoh menggunakan dictionary:

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```
Constructor `dict()` membangun kamus langsung dari urutan pasangan kunci-nilai:

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

kamus `dict comprehensions` dapat digunakan untuk membuat kamus dictionary dari ekspresi kunci dan nilai acak arbitrary:

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```
---
## 5.6. Teknik Perulangan / Looping

---

Saat mengulang pada dictionaries, kunci key dan nilai value terkait dapat diambil pada saat yang sama menggunakan metode `items()`, `enumerate()`, `zip()`, `reversed()`, `sorted()`.

---
fungsi `items()`
```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

menggunakan fungsi `enumerate()`.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
```

fungsi `zip()`.

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

fungsi `reversed()`.

```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
```

fungsi `sort()`

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
...
apple
apple
banana
orange
orange
pear
```

Menggunakan `sorted()` 
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
```

Terkadang tergoda untuk mengubah daftar `list` saat Anda mengulanginya; namun, seringkali lebih mudah dan aman untuk membuat daftar `list` baru.

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```
---
## 5.7. Lebih lanjut tentang Kondisi

---

Kondisi yang digunakan dalam pernyataan `while` dan `if` dapat berisi operator apa pun, bukan hanya perbandingan.

Perbandingan dapat digabungkan menggunakan operator Boolean `and` dan `or`, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan `not`.  untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel. 

Sebagai contoh :

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

Perhatikan bahwa dalam Python, tidak seperti C, penugasan di dalam ekspresi harus dilakukan secara eksplisit dengan operator walrus `:=`. 

---
## 5.8. Membandingkan Urutan Sequences dan Tipe Lainnya

---

Objek urutan sequence biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan pengurutan `lexicographical`.

Contoh perbandingan antara urutan dengan tipe yang sama:

```python
(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
```

