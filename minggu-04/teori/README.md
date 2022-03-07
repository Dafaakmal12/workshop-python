> Pertemuan Minggu 04

# Bab.6 Modules

---
Dalam bab ini membahas tentang dengan modul pada python, modul pada Python adalah sebuah file yang berisikan sekumpulan kode fungsi, class dan variabel yang disimpan dalam satu file berekstensi `.py` dan dapat dieksekusi oleh interpreter Python.
Modul memungkinkan untuk mengatur kode Python secara logis. Mengelompokkan kode terkait ke dalam modul membuat kode lebih mudah dipahami dan digunakan. secara sederhana modul adalah file yang terdiri dari kode Python yang dapat mendefinisikan fungsi, kelas dan variabel.

contoh file fibo.py :
```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

selanjutnya masukkan interpreter Python dan impor modul ini dengan perintah berikut:

```python
>>> import fibo
```
Menggunakan nama modul kita untuk dapat mengakses fungsi, nama fungsi yang didefinisikan `fibo` kemudian memasukkan nama modul di fibo seperti berikut :

```python
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
```

Jika sering menggunakan suatu fungsi, kita dapat menetapkannya ke nama lokal seperti ini :

```python
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

## 6.1. More on Modules

---

Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. 

Dan juga modul dapat mengimport modul lain. Tetapi tidak diharus untuk menempatkan semua pernyataan import di awal modul. 

contoh pernyataan `import` yang mengimport nama dari modul langsung ke tabel simbol modul pengimpor :

```python
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Dalam pernyataan di atas tidak memperkenalkan nama modul dari mana import diambil dalam tabel simbol lokal.

ada juga contoh untuk mengimpor semua nama yang didefinisikan oleh modul:

```python
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

Jika nama modul diikuti oleh `as`, maka nama setelah `as` terikat langsung ke modul yang diimport.

```python
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

contoh di atas secara efektif mengimpor modul dengan cara yang sama dengan `import fibo` yang akan dilakukan, dengan satu-satunya perbedaan adalah sebagai `fib`.

ini juga dapat digunakan saat menggunakan `from`:

```python
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
```

### 6.1.1. Executing modules as scripts / Menjalankan modul sebagai skrip**

---

Saat Anda menjalankan modul Python  `python fibo.py <arguments>`, kode dalam modul akan dieksekusi.

jika Anda mengimpornya, tetapi dengan kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__set ke "__main__". Itu berarti bahwa dengan menambahkan kode tersebut di akhir modul.

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

Anda dapat membuat file dapat digunakan sebagai skrip serta modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

```python
$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```

Jika modul diimport, kode tidak bisa dieksekusi/dijalankan:

```python
>>> import fibo
>>>
```

### 6.1.2. The Module Search Path / Modul Jalur Pencarian

---

Ketika sebuah modul bernama `spam` diimport, interpreter pertama-tama akan mencari modul bawaan dengan nama itu. Jika tidak ditemukan, maka kemudian akan mencari berkas bernama spam.py dalam daftar directory yang diberikan oleh variabel `sys.path. sys.path` yang diinisialisasi dari lokasi ini:
- Directory yang berisi script masukan (atau direktori saat ini ketika tidak ada file ditentukan).
- PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan variabel shell PATH).
- Default yang bergantung pada instalasi (berdasarkan konvensi termasuk site-packagesdirektori, ditangani oleh sitemodul).

Setelah inisialisasi, program Python dapat memodifikasi ` data :sys.path`. Directory yang berisi script yang dijalankan dan ditempatkan di awal jalur pencarian, di depan jalur pustaka standar.

### 6.1.3. “Compiled” Python files / File Python "Dikompilasi"

---

Untuk mempercepat memuat modul, Python menyimpan cache versi terkompilasi dari setiap modul di directory `__pycache__` dengan nama `module. version.pyc`, di mana versi menyandikan format berkas terkompilasi; umumnya berisi nomor versi Python. Misalnya, dalam rilis CPython 3.3 versi yang dikompilasi dari `spam.py` akan di-cache sebagai `__pycache__/spam.cpython-33.pyc`. Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang beragam dan versi Python yang berbeda.


## 6.2. Standard Modules / Modul Standar

---

Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, winregmodul hanya disediakan pada sistem Windows.

Satu modul tertentu patut mendapat perhatian: `sys`, yang dibangun ke dalam setiap interpreter Python. Variabel `sys.ps1` dan `sys.ps2` menentukan string yang digunakan sebagai prompt primer dan sekunder.

```python
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

Kedua variabel tersebut hanya ditentukan jika interpreter dalam mode interaktif.

Variabel `sys.path` adalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Hal tersebut diinisialisasi ke jalur default yang diambil dari variabel lingkungan `PYTHONPATH`, yang dapat dimodifikasi menggunakan operasi standar untuk list:

```python
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
```

## 6.3. The dir() Function / Fungsi dir()

---

Fungsi bawaan `dir()` digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul. Dimana Fungsi dir() akan mengembalikan nilai berupa list yang berisi atribut-atribut dari suatu objek yang diurutkan:

```python
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__',
 '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__',
 '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_framework',
 '_getframe', '_git', '_home', '_xoptions', 'abiflags', 'addaudithook',
 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix',
 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing',
 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info',
 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info',
 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth',
 'getallocatedblocks', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile',
 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value',
 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',
 'path_importer_cache', 'platform', 'prefix', 'ps1', 'ps2', 'pycache_prefix',
 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'setdlopenflags',
 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr',
 'stdin', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info',
 'warnoptions']
```

jika Tanpa argumen, `dir()` mencantumkan nama yang telah kita tentukan saat ini:

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

jika fungsi dir() tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda ingin daftarnya, mereka didefinisikan dalam modul standar builtins:

```python
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
```

## 6.4. Packages / Paket

---
Paket pada python adalah sebuah cara untuk mengelola dan mengorganisir modul-modul python dalam bentuk direktori, memungkinkan sebuah modul untuk diakses menggunakan “namespace” dan titik lokasi.Misalnya, nama modul A.B menunjuk sebuah submodul yang dinamai B dalam sebuah paket bernama A.
Berikut adalah kemungkinan struktur untuk paket Anda (dinyatakan dalam bentuk sistem file hierarki):

```python
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Pengguna paket dapat mengimport modul individual dari paket, misalnya:

```python
import sound.effects.echo
```
ini memuat submodule `sound.effects.echo`. Hal tersebut harus dirujuk dengan nama lengkap yakni:

```python
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

menggunakan cara alternatif mengimport submodul seperti:

```python
from sound.effects import echo
```
itu juga akan memuat submodul `:mod: echo` dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:

```python
echo.echofilter(input, output, delay=0.7, atten=4)
```

atau menggunakan variasi lain ketika mengimport fungsi atau variabel yang diinginkan secara langsung dengan:

```python
from sound.effects.echo import echofilter
```

Dan hasilnya akan sama memuat submodul echo, tetapi ini membuat fungsinya menjadi `echofilter()` langsung tersedia dan tidak lagi diikuti dengan `echo.`:

```python
echofilter(input, output, delay=0.7, atten=4)
```


### 6.4.1. Importing * From a Package / Mengimpor * Dari Paket

---
 Pernyataan import menggunakan konvensi berikut: jika suatu paket punya kode `__init __.py` yang mendefinisikan daftar bernama `__all__`, itu diambil sebagai daftar nama modul yang harus diimport ketika `from package import *` ditemukan. Terserah pembuat paket untuk tetap memperbarui daftar ini ketika versi baru dari paket dirilis. Misalnya, file dapat berisi kode berikut: from package import `sound/effects/__init__.py` 

    ```python
    __all__ = ["echo", "surround", "reverse"]
    ```

Ini berarti bahwa `from sound.effects import *` akan mengimport tiga submodul bernama dari paket `sound`.

Jika `__all__` tidak didefinisikan, pernyataan `from sound.effects import *` tidak mengimport semua submodul dari paket `sound.effects` ke namespace saat ini; itu hanya memastikan bahwa paket `sound.effects` telah diimport (mungkin menjalankan kode inisialisasi apa pun di `__init__.py`) dan kemudian mengimport nama apa pun yang didefinisikan dalam paket. 

Pertimbangkan kode ini: `from sound.effects import`

```python
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
```

Dalam contoh ini, modul `echo` dan `surround` diimport dalam namespace saat ini karena mereka didefinisikan dalam paket `sound.effects` ketika paket `from...import` Pernyataan dieksekusi. (Ini juga berfungsi ketika `__all__` didefinisikan.)


### 6.4.2. Intra-package References / Referensi Intra-paket**

---

Ketika paket disusun menjadi subpaket, dapat menggunakan import absolut untuk merujuk pada submodul dari siblings packages. Misalnya, jika modul `sound.filters.vocoder` perlu menggunakan modul `echo` dalam paket `sound.effects`, hal tersebut dapat menggunakan `from sound.effects import echo `.

Dari modul `surround` misalnya dapat menggunakan:

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

### 6.4.3. Packages in Multiple Directories / Paket di Beberapa Direktori

---

Paket mendukung satu atribut khusus lagi, `__path__`. Hal ini diinisialisasi menjadi daftar yang berisi nama direktory yang menyimpan file paket: `__init__.py` sebelum kode dalam file tersebut dieksekusi.  Variabel ini dapat dimodifikasi, hal itu memengaruhi pencarian `modul` dan `subpackage` di masa depan yang terkandung dalam paket. dan fitur ini dapat digunakan untuk memperluas kumpulan modul yang ditemukan dalam sebuah paket.
