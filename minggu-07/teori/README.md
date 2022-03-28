> Pertemuan Minggu 07


# BAB.9 Classes (Kelas)

Python merupakan sebuah bahasa object oriented programming. Jadi hampir semua yang ada di python adalah sebuah object, dengan properties dan methods.
Class pada python bisa dikatakan sebagai blueprint(cetakan) dari objek yang ingin kita buat. Didalam kelas kita bisa menaruh satu atau beberapa function(methods) sekaligus untuk menajalankan perintah tertentu.

`Classes` atau kelas-kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Membuat sebuah class baru untuk menghasilkan objek dengan type baru, yang memungkinkan dibuatnya `instance` baru dari tipe itu. Setiap `instance` dari `class` dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisi. `Instance` dari sebuah `class` juga dapat memiliki metode (ditentukan oleh class) untuk memodifikasi kondisinya.

---
## 9.1. A Word About Names and Objects (Sebuah Kata Tentang Nama dan Objek)
---
Ini biasanya tidak dihargai pada pertemuan pertama di Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel).  Misalnya, melewatkan sebuah objek adalah murah karena hanya sebuah pointer yang dilewatkan oleh implementasi; dan jika suatu fungsi memodifikasi objek yang diteruskan sebagai argumen, pemanggil akan melihat perubahannya, ini menghilangkan kebutuhan akan dua mekanisme penerusan argumen yang berbeda seperti dalam Pascal. 

---
## 9.2. Python Scopes and Namespaces (Lingkup Python dan Ruang Nama)
---
Namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan itu mungkin berubah di masa depan. 
Contoh ruang nama namespace adalah himpunan nama bawaan (berisi fungsi seperti `abs()`, dan nama pengecualian bawaan), nama-nama global dalam sebuah modul, dan nama-nama lokal dalam pemanggilan fungsi.

Lingkup Python adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. “Dapat diakses secara langsung” di sini berarti bahwa referensi yang tidak memenuhi syarat untuk sebuah nama mencoba menemukan nama tersebut di namespace.



### 9.2.1. Scopes and Namespaces Example (Contoh Ruang Lingkup dan Ruang Nama)

---
Ini adalah contoh yang menunjukkan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda, dan bagaimana `global` dan `nonlocal` memengaruhi pengikatan variabel:

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
```

Outputnya :

```python
After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```
---
## 9.3. A First Look at Classes (Pandangan Pertama tentang Kelas)
---
Memperkenalkan sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

### 9.3.1. Class Definition Syntax (Sintaks Definisi Kelas)
---
bentuk paling sederhana dari class:

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```
 
Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek. Pernyataan di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi pernyataan lain diizinkan. Definisi fungsi di dalam kelas biasanya memiliki bentuk khusus daftar argumen, didikte oleh konvensi pemanggilan untuk metode. Ketika definisi kelas dimasukkan, `namespace` baru dibuat, dan digunakan sebagai lingkup `scope` lokal --- dengan demikian, semua tugas untuk variabel lokal masuk ke `namespace` baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.

### 9.3.2. Class Objects (Objek Kelas)
---

Objek kelas mendukung dua jenis operasi: `attribute references (referensi atribut)` dan `instantiation (instansiasi)`.

`Attribute references` menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: `obj.name`. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat. Jadi, jika definisi kelas tampak seperti ini:

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
```

kemudian `MyClass.i` dan `MyClass.f` adalah referensi atribut yang valid, masing-masing mengembalikan integer dan objek fungsi. Atribut kelas juga dapat ditetapkan, sehingga kita dapat mengubah nilai `MyClass.i` oleh penugasan. `__doc__` juga merupakan atribut yang valid, mengembalikan docstring milik kelas: `"A simple example class"`.

instantiation kelas menggunakan notasi fungsi. HAnggap saja objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. 
Misalnya (dengan asumsi kelas di atas) :

```python
x = MyClass()
```

membuat `instance` baru dari kelas dan menetapkan objek ini ke variabel lokal x.

Operasi instantiasi ("panggilan" dari objek kelas) membuat objek kosong. Banyak kelas lebih memilih untuk membuat objek dengan contoh yang memenuhi kriteria awal tertentu. Oleh karena itu, kelas dapat mendefinisikan metode khusus yang disebut __init__() seperti ini:

```python
def __init__(self):
    self.data = []
```

Ketika sebuah kelas mendefinisikan metode __init__(), instantiasi kelas secara otomatis memanggil __init__() untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, contoh baru yang diinisialisasi dapat diperoleh oleh:

```python
x = MyClass()
```

Tentu saja, metode __init__() metode ini mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal itu, argumen yang diberikan kepada operator instantiasi kelas diteruskan ke __init__(). 

Contoh :

```python
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

### 9.3.3. Instance Objects (Objek Instance)
---

Operasi yang dipahami oleh objek instance adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data dan metode. Data `atribut` sesuai dengan Smalltalk "variabel contoh" dan C ++ "anggota data". Tidak perlu mendeklarasikan atribut data. Seperti variabel lokal, variabel tersebut ditampilkan saat pertama kali ditetapkan. Misalnya, jika x adalah turunan dari `Myclass` yang dibuat di atas, bagian kode berikutnya akan menampilkan nilai `16` tanpa meninggalkan jejak :

```python
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
```

Jenis lainnya dari referensi atribut instance adalah `method`. Metode adalah fungsi yang "milik" suatu objek. (Dalam Python, istilah metode tidak unik untuk instance kelas: tipe objek lain dapat memiliki metode juga. Misalnya, objek daftar memiliki metode yang disebut `append, insert, remove, sort, dan sebagainya`.

### 9.3.4. Method Objects (Metode Objek)
---

suatu metode biasanya dipanggil tepat setelah terikat:

```python
x.f()
```

Dalam contoh MyClass, ini akan mengembalikan string `'hello world'`. Namun, tidak perlu memanggil metode segera: `x.f` adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu. 

Contoh:

```python
xf = x.f
while True:
    print(xf())
```

ini akan terus mencetak hello world hingga akhir waktu.

Kita memperhatikan bahwa `x.f()` dipanggil tanpa argumen di atas, meskipun definisi fungsi untuk `f()` menentukan argumen. Metode adalah objek `instance` dilewatkan sebagai argumen pertama dari fungsi. Secara umum, memanggil metode dengan daftar argumen `n` setara dengan memanggil fungsi yang sesuai dengan daftar argumen yang dibuat dengan menyisipkan objek contoh metode sebelum argumen pertama. 

Jika nama menunjukkan atribut kelas yang valid yang merupakan objek fungsi, objek metode dibuat dengan mengemas `(Pointers to)` objek instance dan objek fungsi yang baru saja ditemukan bersama dalam objek abstrak: ini adalah objek metode. Ketika objek metode dipanggil dengan daftar argumen, daftar argumen baru dibangun dari objek `instance `dan daftar argumen, dan objek fungsi dipanggil dengan daftar argumen baru ini.

### 9.3.5. Class and Instance Variables (Kelas dan Variabel Instance)
---
Secara umum, variabel `instance` adalah untuk data unik untuk setiap `instance` dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua `instance` kelas:

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```
shared data dapat memiliki efek yang mungkin mengejutkan dengan melibatkan objek yang bisa berubah seperti `lists` dan `dictionaries`.
Contoh, daftar `tricks` dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua `Dog instance`:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Desain kelas yang benar harus menggunakan variabel `instance` sebagai gantinya:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

---
## 9.4. Random Remarks (Keterangan Acak)
---

Jika nama atribut yang sama terjadi di kedua `instance` dan di `class`, maka pencarian atribut memprioritaskan `instance`:

```python
>>> class Warehouse:
        purpose = 'storage'
        region = 'west'

>>> w1 = Warehouse()
>>> print(w1.purpose, w1.region)
storage west
>>> w2 = Warehouse()
>>> w2.region = 'east'
>>> print(w2.purpose, w2.region)
storage east
```
Atribut data dapat direferensikan oleh metode serta oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Faktanya, tidak ada dalam Python yang memungkinkan untuk memaksakan penyembunyian data, semuanya didasarkan pada konvensi.

Objek fungsi apapun yang merupakan atribut kelas mendefenisikan metode untuk instance dari kelas itu. bahwa definisi fungsi Tidak perlu  secara teks dalam definisi kelas, menetapkan objek fungsi ke variabel lokal di kelas juga bisa.

Contoh:

```python
# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
```

Sekarang `f`, `g` dan `h` adalah semua atribut class C yang merujuk ke objek-objek fungsi, dan akibatnya semua atribut class c tersebut merupakan metode instance dari C --- `h` yang sama persis dengan `g`.

Metode dapat memanggil metode lain dengan menggunakan atribut metode dari argumen `self`:

```python
class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
```

Metode dapat mereferensikan nama global dengan cara yang sama seperti fungsi biasa. Lingkup global yang terkait dengan suatu metode adalah modul yang berisi definisinya. (Sebuah kelas tidak pernah digunakan sebagai lingkup global.) Meskipun jarang ditemukan alasan yang baik untuk menggunakan data global dalam suatu metode, ada banyak penggunaan yang sah dari lingkup global.

Setiap nilai adalah objek, dan karenanya memiliki kelas (juga disebut sebagai type). Ini disimpan sebagai object.__class__.

---
## 9.5. Inheritance (Pewarisan)
---

fitur bahasa tidak akan layak untuk nama `"class"` tanpa mendukung `pewarisan`. Sintaks untuk definisi kelas turunan terlihat seperti ini:

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```
Nama `BaseClassName` harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Ini bisa berguna, misalnya, ketika kelas dasar didefinisikan dalam modul lain:

```python
class DerivedClassName(modname.BaseClassName):
```
Eksekusi definisi kelas turunan menghasilkan sama seperti untuk kelas dasar. Ketika objek kelas dibangun, kelas dasar diingat. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan untuk mencari di kelas dasar.


Tidak ada yang istimewa tentang instance kelas turunan: `DerivedClassName()` membuat instance baru dari kelas. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, turun rantai kelas dasar jika perlu, dan referensi metode ini valid jika ini menghasilkan objek fungsi.

Metode utama dalam kelas turunan mungkin sebenarnya ingin memperluas daripada hanya mengganti metode kelas dasar dengan nama yang sama. untuk memanggil metode kelas dasar secara langsung, cukup panggil `BaseClassName.methodname(self, arguments)`.(Perhatikan bahwa ini hanya berfungsi jika kelas dasar dapat diakses sebagai `BaseClassName` dalam lingkup global.)

Python memiliki dua fungsi bawaan yang bekerja dengan warisan:

- Gunakan `isinstance()` untuk memeriksa jenis instance: `isinstance(obj, int) ` akan menjadi `True` hanya jika `obj.__class__` adalah `int` atau beberapa kelas yang diturunkan dari `int`.
- Gunakan `issubclass()` untuk memeriksa warisan kelas: `issubclass(bool, int)adalah True` karena `bool` adalah subkelas dari `int`. Namun, `issubclass(float, int)` adalah `False` karena `float` bukan subkelas dari `int`. 

### 9.5.1. Multiple Inheritance (Pewarisan Berganda)
---

Python juga mendukung bentuk pewarisan berganda. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

Untuk sebagian besar tujuan, dalam kasus yang paling sederhana, Anda dapat menganggap pencarian atribut yang diwarisi dari kelas induk sebagai depth-first, left-to-right, bukan pencarian dua kali di kelas yang sama di mana terdapat tumpang tindih dalam hierarki. Jika atribut tidak ditemukan di `D`erivedClassName, itu dicari di Base1, kemudian (secara rekursif) di kelas dasar dari `Base1`, dan jika tidak ditemukan di sana, itu dicari di `Base2`, dan seterusnya. 

Urutan resolusi metode berubah secara dinamis untuk mendukung pemanggilan kooperatif ke `super()`. Pendekatan ini dikenal dalam beberapa bahasa warisan ganda sebagai metode panggilan-berikutnya `call-next-method` dan lebih berdaya daripada panggilan super yang ditemukan dalam bahasa warisan tunggal.

---
## 9.6. Private Variables (Variabel Privat)
---

Variabel instance `"Private"` yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (mis. `_spam`) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

ada dukungan terbatas untuk mekanisme seperti itu, yang disebut `Name mangling`. `Name mangling` sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode `intraclass`.

Contoh :

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

Contoh di atas akan berfungsi bahkan jika `MappingSubclass` akan memperkenalkan sebuah pengidentifikasi `__update` karena diganti dengan `_Mapping__update` di kelas `Mapping` dan `_MappingSubclass__update` di kelas M`appingSubclass` masing-masing.

Dapat dilihat bahwa kode yang dilewatkan ke `exec()` atau `eval()` tidak menganggap nama kelas classname dari kelas yang dipanggil sebagai kelas saat ini; ini mirip dengan efek pernyataan `global`, yang efeknya juga terbatas pada kode yang dikompilasi`-byte byte-compiled` bersama. Pembatasan yang sama berlaku untuk `getattr()`, `setattr()` dan `delattr()`, serta saat mereferensikan __dict__ secara langsung.

---
## 9.7. Odds and Ends
---
Memiliki tipe data yang mirip dengan `"record"` Pascal atau `"struct"` C terkadang berguna, menggabungkan beberapa item data bernama. Definisi kelas kosong akan menghasilkan hal tersebut dengan baik:

```python
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
```
Sebuah kode Python yang mengharapkan tipe data abstrak tertentu sering kali dapat dilewatkan ke kelas yang mengemulasi metode tipe data itu sebagai gantinya. 
Objek metode instance memiliki atribut, juga: m.__self__ adalah objek instan dengan metode m(), dan m.__func__ adalah objek fungsi yang sesuai dengan metode.

---
## 9.8. Iterators
---

Sekarang dapat diperhatikan bahwa sebagian besar objek container dapat dibuat perulangan menggunakan pernyataan `for`:

```python
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```
Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__ yang mengakses elemen dalam penampung `container` satu per satu. Ketika tidak ada lagi elemen, __next__ memunculkan pengecualian `StopIteration` yang memberi tahu perulangan for untuk mengakhiri.

Penggunaan iterator meliputi dan menyatukan Python. Di bail layar, pernyataan `for` memanggil `iter()` pada objek penampung container. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__() yang mengakses elemen dalam container satu per satu. Ketika tidak ada lagi elemen, __next__() memunculkan pengecualian `StopIteration` yang memberi tahu perulangan for untuk mengakhiri. untuk memanggil metode __next__() menggunakan next() fungsi bawaan.

Contoh ini menunjukkan cara kerjanya :

```python
>>> s = 'abc'
>>> it = iter(s)
>>> it
<str_iterator object at 0x10c90e650>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
```

Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas. tentukan metode __iter__() yang mengembalikan objek dengan metode __next__(). Jika kelas mendefinisikan __next__(), maka __iter__() bisa langsung mengembalikan `self`:

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```
```python
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```
---
## 9.9. Generators
---
Generator adalah tools atau alat yang sederhana dan kuat untuk membuat iterator. Mereka ditulis seperti fungsi biasa tetapi menggunakan pernyataan `yield` setiap kali mereka ingin mengembalikan data. Setiap kali `next()` dipanggil, generator melanjutkan di tempat yang ditinggalkannya.

Contoh menunjukkan bahwa generator sangat mudah dibuat:

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
```
```python
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

Apa pun yang dapat dilakukan dengan pembangkit generator juga dapat dilakukan dengan `iterator` berbasis kelas seperti yang dijelaskan pada bagian sebelumnya. Apa yang membuat generator sangat kompak adalah bahwa metode __iter__() dan __next__() dibuat secara otomatis. fiitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara pemanggilan. Ini membuat fungsi lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan menggunakan variabel instan seperti `self.index` dan `self.data`. 
Selain pembuatan metode otomatis dan menyimpan status program, ketika generator dimatikan , akan secara otomatis menaikkan `StopIteration`.

---
## 9.10. Generator Expressions
---
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan pemahaman daftar tetapi dengan tanda kurung alih-alih tanda kurung siku. Ekspresi generator lebih ringkas tetapi kurang fleksibel daripada definisi generator lengkap dan cenderung lebih ramah memori daripada pemahaman daftar yang setara.

Contoh:

```python
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> unique_words = set(word for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
```