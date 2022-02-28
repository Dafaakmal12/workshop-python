> Pertemuan Minggu 03

## Bab.5 Struktur Data

Pada Bab 5 ini menjelaskan beberapa hal mengenai struktur data pada Python. struktur data berbicara mengenai suatu cara untuk menyimpan, menyusun, mengelompokkan dan merepresentasikan suatu data.Dalam Python terdapat empat struktur data built-in yaitu List, Tuple, Dictionary, Set, dan lain-lain.

### 5.1 Daftar

Daftar merupakan struktur data terurut (urutan), Setiap item dalam List memiliki indeks yang dimulai dari 0. List direpresentasikan dengan karakter kurung siku [ ].
Tipe data daftar memiliki beberapa metode lagi. Berikut adalah semua metode objek daftar :

- list.append(*x*) : Tambahkan item ke akhir daftar

- list.extend(*iterable* : untuk perluas pada daftar dapat menambahkan ke semua item yang ada pada iterable.

- list.insert(*i*, *x*) : untuk memasukkan item pada posisi tertentu.*

- list.remove(*x*) : untuk menghapus item pertama pada daftar yang nilainya sama dengan *x* dan ini akan menimbulkan *ValueError* jika tidak ditemukan item yang serupa. 

- list.pop([i]) : untuk menghapus item yang pada posisi tertentu didalam daftar dan dikembalikan. Jika tidak ada indeks yang ditentukan akan dihapus dan dikembalikan  item terakhir didalam daftar tersebut.

- list.clear() :  Menghapus semua item dari daftar.

- list.index(*x*[, *start*[, *end*]])
    Mengembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Menaikkan a ValueErrorjika tidak ada item seperti itu. Argumen opsional start dan end ditafsirkan seperti dalam notasi irisan dan digunakan untuk membatasi pencarian ke urutan daftar tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen awal.

- list.count(*x*) : Mengembalikan berapa kali x muncul dalam daftar.

- list.sort(*, key=None, Reverse=False) : Mengurutkan item didalam daftar.

- list.reverse() :  membalikkan elemen didaftar pada tempatnya.

- list.copy() : untuk mengembalikan salinan daftar yang dangkal.

Contoh yang menggunakan sebagian besar metode daftar: 

```python
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')

>>> fruits.count('tangerine')

>>> fruits.index('banana')

>>> fruits.index('banana', 4)  # Find next banana starting a position 4

>>> fruits.reverse()
>>> fruits

>>> fruits.append('grape')
>>> fruits

>>> fruits.sort()
>>> fruits

>>> fruits.pop()

```

#### 5.1.1 Menggunakan Daftar Sebagai Tumpukan

Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil. untuk menambahkan item ke bagian atas tumpukan, gunakan append() dan untuk mengambil item dari atas tumpukan, gunakan pop()tanpa indeks eksplisit.

contoh : 

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack

>>> stack.pop()

>>> stack

>>> stack.pop()

>>> stack.pop()

>>> stack

```

#### 5.1.2 Menggunakan Daftar Sebagai Antrian


Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama")

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")    
>>> queue.append("Graham")   
>>> queue.popleft()                 

>>> queue.popleft()             

>>> queue                     

```

#### 5.1.3 Daftar Pemahaman

Daftar pemahaman, dimana untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu.

contoh membuat daftar kotak, seperti berikut:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
```
untuk menghitung daftar kotak tanpa efek samping menggunakan:


```python
>>>squares = list(map(lambda x: x**2, range(10)))
```
untuk ekuivalen : 
```python
>>> squares = [x**2 for x in range(10)]
```
Pemahaman daftar terdiri dari tanda kurung yang berisi ekspresi diikuti oleh forklausa, lalu nol atau lebih foratau if klausa. Hasilnya adalah daftar baru yang dihasilkan dari evaluasi ekspresi dalam konteks fordan ifklausa yang mengikutinya. 
contoh listcomp menggabungkan elemen dari dua daftar jika tidak sama:
```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
```
Pemahaman daftar dapat berisi ekspresi kompleks dan fungsi bersarang :

```python
>>> from math import pi
[str(round(pi, i)) for i in range(1, 6)]
```

#### 5.1.4 Nested List Comprehensions / Pemahaman Daftar

Dalam pemahaman daftar dapat berupa arbitrary expression, termasuk pemahaman daftar yang lainnya. 

contoh matriks 3x4 yang diimplementasikan sebagai daftar 3 daftar/lists dan length/panjang 4 : 

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```
untuk mengubah baris dan kolom :

```python
>>> [[row[i] for row in matrix] for i in range(4)]
```

listcomp bersarang dievaluasi dalam konteks for
```python
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transpose
```


Menggunakan fungsi zip():

```python
>>> list(zip(*matrix))
```

### 5.2 Pernyataan Del

Pernyataan del dapat digunakan untuk item dari daftar atau pun juga dapat menghapus irisan dari daftar atau menghapus seluruh daftar.

contoh :
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

Pernyatan Del juga dapat digunakan untuk menghapus seluruh variabel :

```python
>>> del a
```

### 5.3 5.3. Tuple dan Urutan/sequences

Tipe data urutan tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:

```python
>>> t = 12345, 54321, 'hello!'
>>> t[0]

>>> t

>>> u = t, (1, 2, 3, 4, 5)
>>> u

>>>t[0] = 88888

>>> v = ([1, 2, 3], [3, 2, 1])
>>> v

```

Tupel kosong dibangun oleh sepasang tanda kurung kosong, tuple dengan satu item dibangun dengan mengikuti nilai dengan koma. contoh :

```python
>>> empty = ()
>>> singleton = 'Annyeonghaseo',    # <-- note trailing comma
>>> len(empty)

>>> len(singleton)

>>> singleton
```

### 5.4 Sets

Python juga menyertakan tipe data untuk set . Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat.  set()fungsi dapat digunakan untuk membuat himpunan. 

berikut contoh singkat :
```python

>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print (basket)         

>>> 'orange' in basket   

>>>'crabgrass' in basket

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a       
>>> a - b  

>>> a | b    
>>> a & b   
>>> a ^ b     
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
a
```

### 5.5 Dictionaries/Kamus

Tipe data lain dalam Python adalah Dictionaries/kamus Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut.

- untuk menghapus pasangan key:value dengan menggunakan _del_. 
-  untuk mengembalikan daftar semua kunci yang digunakan dalam kamus Melakukan _list()_.
- untuk urutan penyisipan menggunakan _sorted()_.
- Untuk memeriksa apakah satu kunci ada dalam kamus, gunakan _in_ kata kunci.

Contoh penggunaan kamus/dictionary:

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel

>>> tel['jack']

>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel

>>> list(tel)

>>> sorted(tel)

'guido' in tel

'jack' not in tel
```

### 5.6 Teknik Looping/Perulangan

pada teknik looping/perulangan pada kamus, kunci dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan _items()_.

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
```
indeks posisi dan nilai yang sesuai dapat diambil pada saat yang sama menggunakan fungsi _enumerate()_.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
```
Untuk mengulang dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan fungsi _zip()_.

```python
questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
```
Untuk mengulang urutan secara terbalik, menggunakan fungsi _reversed()_.
```python
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
```
Untuk mengulang urutan dalam urutan terurut, gunakan fungsi _sorted()_.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for i in sorted(basket):
...     print(i)
```

Penggunaan _sorted()_ kombinasi dengan _set()_, _set()_ pada urutan digunakan untuk menghilangkan elemen duplikat.
```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
```
### 5.7 More on Conditions

Kondisi yang digunakan dalam while dan if pernyataan dapat berisi operator apa pun, bukan hanya perbandingan. 

Operator perbandingan in dan not in merupakan tes untuk menentukan apakah suatu nilai adaa tau tidak.

Perbandingan dapat digabungkan menggunakan operator Boolean anddan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not.

contoh Untuk menetapkan hasil perbandingan atau ekspresi Boolean lainnya ke variabel :

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
```

### 5.8 Membandingkan Sequences dan Tipe lainnya 

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama.
```
Perbandingannya menggunakan lexicographical ordering : 
Dimana dua item dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan, jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis.
