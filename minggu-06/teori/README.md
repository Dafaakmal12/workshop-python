> Pertemuan Minggu 06


# BAB.8 Errors and Exceptions (Kesalahan dan Pengecualian)

Kesalahan adalah masalah dalam suatu program yang menyebabkan program akan menghentikan eksekusi. Di sisi lain, pengecualian dimunculkan ketika beberapa peristiwa internal terjadi yang mengubah aliran normal program. terdapat dua jenis Kesalahan terjadi di python yaitu kesalahan sintaks (syntax errors) dan pengecualian (exceptions).

## 8.1. Kesalahan Sintaks (Syntax Errors)

syntax errors terjadi ketika Python tidak dapat mengerti apa yang Anda perintahkan. Hal ini juga dikenal sebagai kesalahan penguraian `parsing`, mungkin merupakan jenis keluhan paling umum yang kita dapatkan ketika masih belajar Python, seperti contoh berikut :

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```
 Dalam contoh, kesalahan terdeteksi pada fungsi `print()`, karena titik dua (`:`) yang hilang sebelum itu. Nama file dan nomor baris dicetak sehingga kita tahu ke mana harus mencari masukan yang berasal dari script.


## 8.2. Pengecualian (Exceptions)

Pengecualian atau exceptions (kesalahan saat beroperasi) terjadi ketika Python mengerti apa yang Anda perintahkan tetapi mendapatkan masalah saat mengikuti yang Anda perintahkan (terjadi saat aplikasi sudah mulai beroperasi). Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti contoh berikut :

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

Dalam contoh diatas, Pengecualian datang dalam tipe yang berbeda, dan tipe tersebut dicetak sebagai bagian dari pesan: tipe dalam contoh adalah ZeroDivisionError, NameErrordan TypeError.  String yang dicetak sebagai tipe pengecualian adalah nama pengecualian bawaan yang terjadi. Sisa baris memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya. Bagian pesan kesalahan sebelumnya menunjukkan konteks di mana pengecualian terjadi, dalam bentuk pelacakan balik tumpukan. Pengecualian Bawaan mencantumkan pengecualian bawaan dan artinya.



## 8.3. Menangani Pengecualian (Handling Exceptions)

Memungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Lihat contoh berikut, yang meminta pengguna untuk memasukkan hingga bilangan bulat yang valid telah dimasukkan, tetapi mengizinkan pengguna untuk menginterupsi program.
Perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan munculnya pengecualian KeyboardInterrup.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

Pertanyaan `try` berfungsi sebagai berikut:

- Pertama, klausa `try clause` (pernyataan antara kata kunci try dan except) dieksekusi.

- Jika tidak ada pengecualian yang terjadi, clause  dilewati dan eksekusi dengan pernyataan `try`  dan selesai.

- Jika pengecualian terjadi selama eksekusi `try clause`, sisa clause akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci `except`kata kunci, clause dieksekusi, dan kemudian eksekusi dilanjutkan setelah blok ctry/except.

- Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam  kecuali , itu diteruskan ke trypernyataan luar; jika tidak ada penangan yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan `try` mungkin memiliki lebih dari satu `except clause`, untuk menentukan penanganan untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Handler hanya menangani pengecualian yang terjadi di klausa `try` yang sesuai, bukan di handler lain dari pernyataan `try` yang sama. 

Contoh :

```python
... except (RuntimeError, TypeError, NameError):
...     pass
```

Kelas dalam `except clause` kompatibel dengan pengecualian jika itu adalah kelas yang sama atau kelas dasar daripada hal itu. Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Perhatikan bahwa jika klausa kecuali dibalik (kecuali dengan B pertama), itu akan dicetak B, B, B. pencocokan pertama klausa kecuali dipicu.

Semua pengecualian mewarisi dari `BaseException`, sehingga dapat digunakan untuk berfungsi sebagai `wildcard`.


```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

Sebagai alternatif, klausa pengecualian terakhir dapat menghilangkan nama pengecualian, namun nilai pengecualian kemudian harus diambil dari `sys.exc_info()[1]`.

Pernyataan `try ... except` memiliki klausa `else` opsional, yang atau jika ada, harus mengikuti semua `except clause`. Berguna untuk kode yang harus dijalankan jika klausa `try` tidak memunculkan eksepsi.

contoh :

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

Penggunaan klausa `else` lebih baik daripada menambahkan kode tambahan ke klausa `try` karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dimunculkan oleh kode yang dilindungi oleh pernyataan `try ... :keyword: !except`. ketika pengecualian terjadi, itu mungkin memiliki nilai terkait, juga dikenal sebagai `argument pengecualian`. Kehadiran dan jenis argumen tergantung pada jenis pengecualian.

Variabel terikat ke instance pengecualian dengan argumen yang disimpan di `instance.args.` Untuk kenyamanan, instance pengecualian mendefinisikan `__str__` sehingga argumen dapat dicetak secara langsung tanpa harus merujuk ke `.args.` Seseorang juga dapat membuat instance pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```
Jika pengecualian memiliki argumen, mereka akan dicetak sebagai bagian (detail) terakhir  dari pesan  pengecualian mentah. Handler eksepsi menangani eksepsi tidak hanya ketika terjadi secara langsung dalam klausa `try`, tetapi juga ketika terjadi (juga secara tidak langsung) dalam fungsi yang disebut dalam klausa` try`. 

Contoh :

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## 8.4. Memunculkan Pengecualian (Raising Exceptions)

Pernyataan `raise` memungkinkan pemrogram untuk memaksakan pengecualian tertentu. sebagai contoh :

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

Satu-satunya argumen untuk `raise` menunjukkan bahwa pengecualian telah dilemparkan. Itu harus berupa  pengecualian instance atau kelas pengecualian (kelas yang diturunkan dari `Exception/pengecualian`). Jika kelas pengecualian dilewatkan, kelas tersebut secara implisit diinisialisasi dengan memanggil konstruktornya tanpa argumen :

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

Jika Anda perlu menentukan apakah pengecualian telah dimunculkan, tetapi Anda tidak bermaksud untuk menanganinya, Anda dapat memunculkan kembali pengecualian tersebut menggunakan bentuk pernyataan `raise` yang lebih sederhana.


```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5. Exception Chaining (Rantai Pengecualian)

Pernyataan `raise`  memungkinkan opsional yang memungkinkan pengecualian berantai. sebagai contoh:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

Ini bisa berguna saat kita mengubah pengecualian. contoh :

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian  secara otomatis dinaikkan ketika pengecualian dilemparkan ke bagian `except` atau `finally`. Ini dapat dinonaktifkan  menggunakan `from None idiom`:

```python
>>> try:
...    open('database.sqlite')
... except OSError:
...    raise RuntimeError from None

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

## 8.6. Pengecualian yang Ditentukan Pengguna (User-defined Exceptions)

Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat Kelas untuk informasi lebih lanjut tentang kelas Python). Pengecualian biasanya perlu diturunkan secara langsung atau tidak langsung dari kelas Pengecualian. Kelas pengecualian / `Exception classes` dapat didefinisikan untuk melakukan segala sesuatu yang dapat dilakukan oleh kelas lain, tetapi biasanya dibuat sederhana dan sering kali hanya menyediakan satu set atribut yang dapat diekstraksi oleh pengendali pengecualian untuk informasi tentang kesalahan. 

Sebagian besar pengecualian didefinisikan dengan nama yang diakhiri dengan "kesalahan", mirip dengan penamaan pengecualian standar. 
 Banyak modul standar mendefinisikan pengecualian mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi dalam fungsi yang mereka tetapkan. Lihat bab Kelas untuk informasi lebih lanjut tentang kelas.


---

## 8.7. Mendefinisikan Tindakan Pembersihan (Defining Clean-up Actions)

Pernyataan `try` memiliki klausa opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan.

Contoh :

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Jika klausa `finally` ada, klausa `finally` adalah yang terakhir dieksekusi  sebelum pernyataan try selesai. Klausa `finally` dieksekusi terlepas dari apakah pernyataan try melempar pengecualian. Poin-poin berikut mencakup kasus yang lebih kompleks di mana Exception / pengecualian terjadi :

- Jika  `Exception` terjadi selama eksekusi klausa try, pengecualian dapat ditangani oleh klausa exception. Jika pengecualian tidak ditangani oleh klausa kecuali, pengecualian dinaikkan kembali setelah klausa `finally` dieksekusi.

- Pengecualian / Exception dapat terjadi selama eksekusi klausa kecuali atau klausa lain. Sekali lagi, pengecualian dinaikkan kembali setelah klausa `finally` dieksekusi.

- Jika klausa `finally` mengeksekusi pernyataan break, continue, atau return, eksepsi tidak dimunculkan kembali.

- Jika pernyataan `try` mencapai pernyataan break, continue, atau return, klausa `finally` akan dieksekusi tepat sebelum eksekusi pernyataan break, continue, atau return.

- Jika klausa `finally` menyertakan pernyataan pengembalian, nilai yang dikembalikan akan menjadi nilai dari pernyataan pengembalian klausa `finally`, bukan nilai dari pernyataan pengembalian klausa `try`.

Contoh:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False
```

Contoh yang lebih kompleks :

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang Anda lihat, klausa `finally` selalu dieksekusi. TypeError yang disebabkan oleh garis-bagi string tidak ditangani oleh klausa `except`, sehingga dikembalikan setelah klausa `finally` dieksekusi. Dalam aplikasi  nyata, klausa "akhirnya" membantu membebaskan sumber daya eksternal (seperti file dan koneksi jaringan) terlepas dari keberhasilannya.

---

## 8.8. Tindakan Pembersihan yang Sudah Ditentukan (Predefined Clean-up Actions)

Beberapa objek menentukan tindakan pembersihan default yang harus Anda ambil saat Anda tidak lagi membutuhkan objek, terlepas dari apakah operasi dengan objek berhasil atau gagal. Perhatikan contoh berikut untuk membuka file dan mencoba mencetak isinya ke layar :

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Masalah dengan kode ini adalah bahwa file tetap terbuka tanpa batas waktu  setelah bagian kode ini dijalankan. Ini bukan masalah untuk skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi  besar. Anda dapat menggunakan pernyataan with untuk membersihkan objek seperti file setiap saat dengan cepat dan akurat.

Contoh :

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah mengeksekusi pernyataan, file `f` selalu ditutup, bahkan jika ada masalah saat memproses baris. Objek yang menyediakan tindakan pembersihan yang telah ditentukan sebelumnya, seperti file, menunjukkan hal ini dalam dokumentasi.