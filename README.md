# Tugas 2
**Checklist 1: Membuat Proyek Django Baru**
1. Buat direktori baru gunpla-store
2. Di dalam direktori tersebut aktifkan cirtual environment dengan menjalankan
   ```bash
   env\Scripts\activate
   ```
4. Menyiapkan requirements untuk django
5. Tambahkan berkas .gitignore
6. Menginstall requirements tersebut
7. Menambahkan host ke host yang diizinkan
8. Lalu jalankan server dengan perintah
   ```bash
   python manage.py runserver
   ```
**Checklist 2: Membuat aplikasi dengan nama main pada proyek tersebut.**
1. Pertama kita bisa menjalankan
   ```bash
   django-admin startproject mental_health_tracker .
   ```
2. Aktifkan virtual environment
3. Untuk membuat aplikasi main baru kita bisa menjalankan perintah
   ```bash
   python manage.py startapp main
   ```
4. Tambahkan main ke aplikasi dasar di settings.py
5. Buat direktori baru **templates** di dalam direktori main
6. Di dalam templates buat main.html dan diisi dengan kode data diri
**Checklist 3: Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib**
1. Di models.py di dalam aplikasi main, tambahkan class berupa produk yang akan ditampilkan dengan atribut name, price, description, dan atribut lainnya
2. Lalu migrasikan model tersebut
**Checklist 4: Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**
1. Tambahkan fungsi show_main di bawah impor:
```python
def show_main(request):
    context = {
        'nama:': 'Ardi Syahputra Amin',
        'kelas': 'PBP B',
        'name' : 'MG GUNDAM F90',
        'price': '420.000',
        'description' : 'Technology & Combat Characteristics The Gundam F90 is a prototype unit developed by the Strategic Naval Research Institute under the “Formula Project”, a plan to create small mobile suits. Standing at only 14.8 meters compared to the 18 meters tall RX-78-2 Gundam, the Gundam F90’s downsizing was achieved through the use of micro-honeycomb structure obtained from Yashima Heavy Industries, enabling its armor and movable frame to be made lighter. It also has a downsized reactor, but its output is 1.5 times that of existing mobile suits. With a total of 51 attitude control thrusters placed throughout its body, the Gundam F90 is also highly mobile and maneuverable. A total of three Gundam F90 units were built and are known as Unit 1 to Unit 3. The Gundam F90’s most prominent feature is its adaptation of the Mission Packs. These dedicated optional equipment can be attached across the 11 hardpoints placed throughout the Gundam F90’s body, allowing the mobile suit to take on a variety of missions. They can also be exchanged when needed, granting the Gundam F90 extremely high versatility. To control the Mission Packs, pseudo-personality computers were installed. Unit 1 has the Type-A.R., while Unit 2 has the Type-C.A. The Gundam F90’s standard armament consist of two head vulcans, a beam rifle, two beam sabers, and a shield.',
        'size_ratio': '1/100',
        'extensions': 'stand base',
        'notes':'*The product in the image is a prototype still in its developmental stage. The product is also painted. The actual product may appear differently from the image. *Please note that in some cases bubbles may enter the clear parts during manufacturing process.'
    }

    return render(request, "main.html", context)
```
**Checklist 5: Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.**
1. Buatlah berkas urls.py di dalam direktori main.
   Isi urls.py dengan kode berikut.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
2. Buka berkas urls.py di dalam direktori proyek gunpla-store, bukan yang ada di dalam direktori aplikasi main.
3. Impor fungsi include dari django.urls.
```python
...
from django.urls import path, include
...
```
4. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan main di dalam variabel urlpatterns.
```python
urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
```
5. Jalankan proyek Django dengan perintah python manage.py runserver
6. Bukalah http://localhost:8000/ di browser untuk melihat halaman yang sudah  dibuat.
**Checklist 6: Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**
1. Ubah branch direktori ke master
2. Lalu push ke pws dengan menjalankan
```bash
git push pws master
```
**Bagan**
![image](https://github.com/user-attachments/assets/c1ac7dc2-3fb5-460c-9d96-207dca47cff2)
1. urls.py (Routing)
Fungsi: urls.py bertugas sebagai pengatur rute (routing) dari URL yang dimasukkan oleh pengguna ke aplikasi Django. Ia memetakan URL tertentu ke fungsi atau view yang sesuai di dalam views.py.
Kaitan: Ketika pengguna mengakses URL, Django menggunakan urls.py untuk menentukan fungsi atau view mana yang akan dipanggil. Contohnya, jika pengguna mengakses /home, urls.py akan memanggil fungsi home() dari views.py.
Alur Kerja: URL → urls.py → View (di views.py)

2. views.py (Logika dan Kontrol)
Fungsi: views.py bertugas untuk menangani permintaan (request) dari pengguna. View ini berfungsi sebagai penghubung antara urls.py dan model (jika ada), serta berkas HTML. View dapat mengambil data dari model, mengolahnya, dan kemudian mengirim data tersebut ke template HTML.
Kaitan: Setelah urls.py memetakan URL ke view, view di views.py akan bertindak untuk memproses logika, mengambil data dari model (jika perlu), dan menyiapkan data yang akan dikirim ke template HTML.
Alur Kerja: View menerima permintaan dari URL → Mengambil data dari models.py (jika diperlukan) → Mengirim data ke template HTML.

3. models.py (Pengelolaan Data)
Fungsi: models.py digunakan untuk mendefinisikan struktur data yang disimpan di database. Model merepresentasikan data yang dikelola oleh aplikasi, seperti entitas Product dengan atribut name, price, dan description. Model ini juga bertanggung jawab atas interaksi dengan database (CRUD: Create, Read, Update, Delete).
Kaitan: View di views.py sering kali berinteraksi dengan model untuk mengambil data dari database atau menyimpannya. Model ini menyediakan data yang nantinya akan ditampilkan di template HTML.
Alur Kerja: View memanggil Model → Model mengambil/mengolah data dari/ke database → Data dikirim ke View → Data ditampilkan di template HTML.

4. Template HTML (Presentasi/Frontend)
Fungsi: Template HTML adalah berkas yang digunakan untuk menampilkan data kepada pengguna dalam format web. Template ini menerima data yang dikirim dari views.py dan kemudian menampilkannya dalam bentuk halaman web yang dapat dilihat oleh pengguna.
Kaitan: Setelah view di views.py mengumpulkan data, view akan memanggil template HTML dan memberikan data tersebut untuk ditampilkan. Di dalam template HTML, data ini bisa diakses menggunakan sintaks Django Template Language (DTL), seperti {{ data }}.
Alur Kerja: View mengirim data ke Template HTML → Template menampilkan data di halaman web.


