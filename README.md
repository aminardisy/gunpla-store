# Tugas 2
### Checklist 1: Membuat Proyek Django Baru
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
### Checklist 2: Membuat aplikasi dengan nama main pada proyek tersebut.
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
### Checklist 3: Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib
1. Di models.py di dalam aplikasi main, tambahkan class berupa produk yang akan ditampilkan dengan atribut name, price, description, dan atribut lainnya
2. Lalu migrasikan model tersebut
### Checklist 4: Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.
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
### Checklist 5: Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
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
### Checklist 6: Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
1. Ubah branch direktori ke master
2. Lalu push ke pws dengan menjalankan
```bash
git push pws master
```
### Bagan
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

### Fungsi Git Untuk Pengembang
Git adalah sistem kontrol versi terdistribusi yang digunakan dalam pengembangan perangkat lunak untuk mengelola perubahan kode sumber secara efisien. Berikut adalah fungsi utama Git dalam pengembangan perangkat lunak:

1. Pencatatan Versi Kode: Git memungkinkan pengembang untuk menyimpan riwayat perubahan pada kode, sehingga setiap perubahan dapat dilacak, di-revert, atau dibandingkan dengan versi sebelumnya.
   
2. Kolaborasi Tim: Git memungkinkan banyak pengembang untuk bekerja secara bersamaan di repositori yang sama tanpa mengganggu pekerjaan satu sama lain. Dengan fitur branch dan merge, mereka dapat menggabungkan kode dengan mudah.

3. Branching: Git menyediakan kemampuan untuk membuat cabang (branch) dari kode utama (main/master), yang memungkinkan pengembangan fitur baru atau perbaikan bug dilakukan secara terpisah tanpa mengganggu kode stabil di cabang utama.

4. Backup Terdistribusi: Karena repositori Git bersifat terdistribusi, setiap pengembang memiliki salinan penuh dari proyek, memberikan cadangan otomatis terhadap proyek tersebut.

5. Manajemen Konflik: Ketika beberapa pengembang mengedit file yang sama, Git membantu mendeteksi dan memandu penyelesaian konflik penggabungan (merge conflicts) dalam kode.

Dengan Git, pengembangan perangkat lunak menjadi lebih terorganisir, aman, dan memungkinkan kolaborasi yang lebih baik antara tim pengembang.
### Menjawab pertanyaan: Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Dari saya pribadi, mungkin karena framework django relatif lebih mudah dipahami oleh pemula daripada framework yang lain

### Menjawab pertanyaan: Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai **ORM (Object-Relational Mapping)** karena model berfungsi sebagai penghubung antara objek dalam kode Python dan tabel dalam database relasional. ORM memungkinkan pengembang untuk bekerja dengan data di database menggunakan objek Python tanpa perlu menulis query SQL secara langsung. Berikut penjelasan lebih rinci:

1. **Object-Oriented**: Django ORM mengizinkan pengembang untuk memanipulasi data dalam database melalui objek Python. Setiap model di Django adalah sebuah class Python, dan setiap record di dalam tabel database adalah sebuah instance dari class tersebut.

2. **Relational Mapping**: Tabel dalam database relasional (seperti PostgreSQL, MySQL, SQLite) dipetakan ke model Django. Setiap field dalam model berhubungan dengan kolom dalam tabel database. Misalnya, sebuah model `Product` dengan atribut `name`, `price`, dan `description` akan dipetakan ke tabel database dengan kolom yang sesuai.

3. **Query Abstraction**: ORM menyediakan cara untuk menulis query database menggunakan bahasa Python. Dengan Django ORM, kita bisa melakukan operasi CRUD (Create, Read, Update, Delete) tanpa menulis query SQL mentah. Django ORM akan secara otomatis mengonversi operasi Python ke query SQL yang sesuai.

   Contoh:
   ```python
   # Mengambil semua objek Product
   products = Product.objects.all()
   ```

4. **Portabilitas**: Karena ORM mengabstraksikan query database, pengembang bisa berpindah-pindah antar database yang berbeda (PostgreSQL, MySQL, SQLite, dll.) tanpa perlu mengubah logika pengelolaan data di model atau query yang digunakan.

Secara keseluruhan, Django ORM menyederhanakan interaksi dengan database relasional dan memungkinkan pengembang fokus pada logika bisnis tanpa terlalu banyak berurusan dengan detail teknis SQL.

# Tugas 3

### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dalam pengimplementasian sebuah platform sangat penting karena beberapa alasan berikut:

1. **Aksesibilitas Data**: Data delivery memastikan bahwa data yang dibutuhkan pengguna tersedia pada waktu yang tepat, dalam format yang mudah dipahami, dan dapat diakses dengan mudah. Ini penting untuk mendukung pengambilan keputusan yang cepat dan tepat.

2. **Kinerja Platform**: Data delivery membantu menjaga performa platform dengan mengoptimalkan bagaimana data dikirimkan ke pengguna. Misalnya, penggunaan caching atau kompresi data dapat mempercepat proses pengiriman data dan mengurangi beban pada server.

3. **Pengalaman Pengguna (UX)**: Pengiriman data yang cepat dan efisien meningkatkan pengalaman pengguna. Jika platform lambat dalam mengirimkan data, pengguna mungkin merasa frustrasi dan beralih ke solusi lain yang lebih responsif.

4. **Keamanan dan Keandalan**: Proses pengiriman data yang baik juga melibatkan mekanisme untuk menjaga keamanan data selama pengiriman, seperti enkripsi. Ini penting untuk mencegah akses yang tidak sah atau pencurian data selama proses transfer.

5. **Integrasi dengan Sistem Lain**: Dalam banyak kasus, platform perlu mengirimkan data ke sistem lain atau menerima data dari sistem eksternal. Data delivery yang efisien memungkinkan integrasi ini berjalan lancar, yang penting untuk memastikan bahwa berbagai sistem dapat berkomunikasi dan bertukar data secara real-time atau mendekati real-time.

6. **Efisiensi Bisnis**: Data delivery yang baik memungkinkan platform untuk menyajikan informasi yang relevan secara tepat waktu, yang membantu bisnis dalam menjalankan proses operasional dengan lebih efisien, misalnya melalui pelaporan otomatis atau pemberian rekomendasi yang didukung data.

Dalam konteks platform modern, seperti aplikasi cloud atau berbasis web, data delivery adalah bagian penting dari arsitektur data yang mendukung berbagai layanan yang ditawarkan platform tersebut.

### Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya JSON lebih baik dari XML, hal ini dikarenakan alasan yang simpel yaitu JSON lebih ringkas dan padat, sehingga lebih cepat untuk diurai dan dibuat.

### Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Fungsi dari `is_valid()` pada form Django adalah untuk memeriksa apakah data yang dikirimkan melalui form memenuhi semua persyaratan validasi yang telah ditentukan. Method ini menggabungkan dua aspek penting:

1. **Validasi Data**: Ketika `is_valid()` dipanggil, Django akan memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang sudah ditetapkan dalam definisi form. Ini bisa mencakup validasi tipe data, panjang data, format tertentu (seperti alamat email atau nomor telepon), dan berbagai aturan kustom lainnya yang didefinisikan oleh pengguna.

2. **Pembersihan Data (Data Cleaning)**: Jika data dianggap valid, Django juga membersihkan atau memproses data tersebut sebelum menyimpannya dalam form. Data yang telah divalidasi dan dibersihkan ini kemudian bisa diakses melalui atribut `form.cleaned_data`. Atribut ini memberikan data dalam format yang telah disesuaikan dengan tipe data yang benar untuk digunakan dalam logika bisnis atau disimpan ke dalam database.

### Mengapa Kita Membutuhkan `is_valid()`?

1. **Menghindari Error di Server**: Memastikan bahwa data yang dikirimkan valid sangat penting untuk menghindari terjadinya error ketika aplikasi mencoba memproses atau menyimpan data yang salah. Tanpa validasi, data yang tidak sesuai dapat menyebabkan crash atau masalah di server.

2. **Keamanan**: Dengan memvalidasi data, aplikasi Django dapat mencegah serangan berbahaya, seperti injeksi SQL atau cross-site scripting (XSS), karena form secara otomatis membersihkan data sebelum memprosesnya.

3. **Integritas Data**: Validasi memastikan bahwa hanya data yang valid dan sesuai aturan yang diterima oleh sistem. Hal ini menjaga integritas data dalam basis data dan mengurangi risiko kesalahan yang mungkin terjadi akibat data yang tidak sesuai.

4. **Feedback ke Pengguna**: Jika data yang dimasukkan ke dalam form tidak valid, method ini memungkinkan Django untuk memberikan umpan balik yang relevan kepada pengguna. Django akan menghasilkan pesan error untuk setiap field yang tidak valid, sehingga pengguna bisa memperbaiki kesalahan mereka.

Jadi, method `is_valid()` berperan penting dalam memastikan bahwa data yang diterima oleh form Django valid, aman, dan siap untuk diproses lebih lanjut.

CSRF Token (Cross-Site Request Forgery Token) adalah elemen keamanan penting dalam form Django untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah jenis serangan di mana penyerang menipu pengguna yang telah diautentikasi di sebuah situs agar tanpa disadari melakukan aksi di situs tersebut, seperti mengubah pengaturan akun atau melakukan transaksi, tanpa sepengetahuan pengguna.

### Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
CSRF Token (Cross-Site Request Forgery Token) adalah elemen keamanan penting dalam form Django untuk melindungi aplikasi dari serangan **Cross-Site Request Forgery (CSRF)**. CSRF adalah jenis serangan di mana penyerang menipu pengguna yang telah diautentikasi di sebuah situs agar tanpa disadari melakukan aksi di situs tersebut, seperti mengubah pengaturan akun atau melakukan transaksi, tanpa sepengetahuan pengguna.

### Mengapa Kita Membutuhkan `csrf_token`?

Django secara default menerapkan CSRF protection untuk semua form yang mengirimkan data melalui metode POST. `csrf_token` dibutuhkan untuk:

1. **Mencegah Serangan CSRF**: CSRF token memastikan bahwa setiap permintaan POST, PUT, atau DELETE yang dibuat oleh pengguna adalah permintaan yang sah dari situs itu sendiri, dan bukan dari sumber eksternal yang berbahaya. Token ini dihasilkan secara acak dan unik untuk setiap sesi pengguna, sehingga hanya permintaan yang memiliki token valid yang akan diproses oleh server.

2. **Mengidentifikasi Sumber Asli Permintaan**: CSRF token ditambahkan ke setiap form sebagai input tersembunyi dan dikirim ke server bersama dengan permintaan POST. Server kemudian memeriksa token ini untuk memastikan bahwa permintaan berasal dari pengguna yang sah dan bukan dari situs atau sumber eksternal.

### Apa yang Terjadi Jika Kita Tidak Menambahkan `csrf_token`?

Jika kita tidak menambahkan CSRF token pada form Django, aplikasi kita menjadi rentan terhadap serangan CSRF. Berikut adalah risiko yang bisa terjadi:

1. **Eksekusi Permintaan Berbahaya**: Tanpa `csrf_token`, penyerang dapat mengirimkan permintaan berbahaya atas nama pengguna tanpa sepengetahuan mereka. Misalnya, jika pengguna telah login ke situs bank dan mengunjungi halaman yang disusupi oleh penyerang, situs tersebut bisa diam-diam mengirimkan permintaan transfer uang dengan menggunakan cookie sesi pengguna.

2. **Pengambilalihan Akun**: Penyerang dapat mengeksploitasi CSRF untuk mengubah pengaturan akun pengguna, seperti mengganti alamat email atau kata sandi, yang dapat mengakibatkan pengambilalihan akun.

### Contoh Serangan CSRF

Misalkan ada situs yang memungkinkan pengguna untuk mengubah kata sandi mereka melalui form POST tanpa perlindungan CSRF. Penyerang dapat membuat sebuah situs palsu yang, ketika dikunjungi oleh korban yang telah login ke situs asli, akan mengirimkan permintaan POST ke situs asli untuk mengubah kata sandi korban. Karena tidak ada CSRF token yang memvalidasi permintaan tersebut, server situs asli mungkin memproses permintaan berbahaya tersebut, dan kata sandi korban akan berubah tanpa mereka sadari.

### Bagaimana CSRF Dimanfaatkan oleh Penyerang?

1. **Situs Berbahaya**: Penyerang dapat membuat situs web palsu yang menyertakan form tersembunyi atau skrip yang mengirimkan permintaan POST ke aplikasi target.
   
2. **Penggunaan Cookie Sesi**: Karena browser secara otomatis mengirimkan cookie sesi ke server yang sesuai, penyerang dapat memanfaatkan cookie sesi yang sah untuk mengirimkan permintaan berbahaya atas nama korban yang sudah login ke aplikasi target.

3. **Pengarahan Pengguna**: Penyerang bisa menggunakan email atau pesan sosial media yang berisi tautan ke situs jahat, yang ketika diklik oleh korban, menjalankan aksi yang merugikan di aplikasi target.

### Kesimpulan

Menambahkan `csrf_token` ke dalam form Django sangat penting untuk mencegah serangan CSRF. Tanpa mekanisme ini, aplikasi kita rentan terhadap permintaan berbahaya yang dapat merusak data, mencuri informasi, atau menjalankan aksi tidak sah lainnya. Django menyediakan mekanisme `csrf_token` secara otomatis sebagai bagian dari keamanan aplikasi web, sehingga setiap form POST yang dikirimkan oleh pengguna terlindungi dari ancaman ini.

### Langkah-langkah membuat input form untuk menambahkan objek model pada app sebelumnya.
1. Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data baru. Tambahkan kode ini ke forms.py
```python
from django.forms import ModelForm
from main.models import Gunpla

class GunplaForm(ModelForm):
    class Meta:
        model = Gunpla
        fields = ["name", "price", "description", "size_ratio", "extensions", "notes"]
```
2. Import GunplaForm dan Gunpla ke views.py dan tambahkan redirect di import render.
3. Tambahkan fungsi dibawah untuk menghasilkan form yang dapat menambahkan data gunpla secara otomatis.
```python
def create_gunpla(request):
    form = GunplaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_gunpla.html", context)
```
4. tambahkan ```'gunpla':gunplas ``` ke dalam context di fungsi show main.
5. Import fungsi yang ada di nomor 3 ke urls.py dan tambahkan path url-nya.
6. Buat berkas HTML baru dengan nama create_gunpla.html pada direktori main/templates. Isi create_gunpla.html dengan kode berikut.
```python
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Gunpla</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Gunpla" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
7. Di dalam main.html, tambahkan kode berikut di dalam block content untuk menampilkan data gunpla.
```python
{% if not gunpla %}
<p>Belum ada data gunpla pada gunplastore.</p>
{% else %}
<table>
  <tr>
    <th>Gunpla Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Size ratio</th>
    <th>Extensions</th>
    <th>Notes</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data gunpla di bawah baris ini 
  {% endcomment %} 
  {% for gunpla in gunpla %}
  <tr>
    <td>{{gunpla.name}}</td>
    <td>{{gunpla.price}}</td>
    <td>{{gunpla.description}}</td>
    <td>{{gunpla.size_ratio}}</td>
    <td>{{gunpla.extensions}}</td>
    <td>{{gunpla.notes}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_gunpla' %}">
  <button>Add New Gunpla</button>
</a>
```
### Langkah -langkah untuk menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
1. Tambahkan 4 fungsi ini ke views.py
```python
def show_xml(request):
    data = Gunpla.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Gunpla.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Gunpla.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Gunpla.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
2. Lalu import keempat fungsi tersebut ke urls.py.
```python
from main.views import show_main, create_gunpla, show_xml, show_json, show_xml_by_id, show_json_by_id
```
### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
Tambahkan kode ini ke urlpatterns di urls.py.
```python
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```
### Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. xml
   ![image](https://github.com/user-attachments/assets/c727909f-2556-487d-8384-38e02a15b4c6)
2. xml/[id]
   ![image](https://github.com/user-attachments/assets/16b5d059-d4bd-4371-95b7-87dc7f8ca02a)
3. json
   ![image](https://github.com/user-attachments/assets/078f6841-5af6-4d51-8d07-9330048b6471)
4. json/[id]
   ![image](https://github.com/user-attachments/assets/39ef32f3-a236-4fd6-9fa1-4d8b40d04b0b)

# Tugas 4
### Apa perbedaan antara HttpResponseRedirect() dan redirect()?
HttpResponseRedirect() dan redirect() adalah dua cara untuk melakukan pengalihan (redirect) pada URL di Django, tetapi keduanya memiliki beberapa perbedaan dalam cara penggunaannya:
HttpResponseRedirect():
- Merupakan class yang ada di django.http.
- Mengembalikan response dengan status HTTP 302 yang menunjukkan bahwa halaman telah pindah ke lokasi baru.
- Digunakan dengan cara memberikan URL sebagai argumen, misalnya HttpResponseRedirect('/new-url/').
- Memerlukan URL absolut atau relatif sebagai parameter.

redirect():
- Merupakan fungsi bawaan dari django.shortcuts.
- Merupakan cara yang lebih ringkas dan lebih mudah dibaca untuk mengarahkan ulang pengguna.
- Mendukung beberapa jenis parameter: URL string, nama view, atau bahkan objek model.
- Bisa digunakan dengan URL absolut atau relatif, nama dari view yang diinginkan (beserta argumen view), atau bahkan objek model yang memiliki metode get_absolute_url().
- Lebih fleksibel dan direkomendasikan untuk digunakan dalam sebagian besar kasus.

### Jelaskan cara kerja penghubungan model Gunpla dengan User!
Penghubungan model Gunpla dengan model User di Django bekerja dengan menggunakan ForeignKey, yang merupakan salah satu tipe relasi dalam database relasional. Relasi ini memungkinkan kita untuk mengaitkan setiap entri gunpla (Gunpla) dengan pengguna (User) yang membuatnya, sehingga setiap entri gunpla terhubung dengan pengguna yang spesifik.

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut?
Authentication (Autentikasi):
- Proses memverifikasi identitas pengguna, memastikan bahwa pengguna adalah siapa yang mereka klaim.
- Terlibat dalam proses login, di mana pengguna memasukkan kredensial seperti username dan password.
- Menentukan siapa pengguna tersebut, tetapi tidak memberikan akses langsung ke sumber daya atau data.
- Contoh: Memasukkan username dan password untuk masuk ke sebuah akun.

Authorization (Otorisasi):
- Proses menentukan hak akses pengguna terhadap sumber daya tertentu setelah berhasil terautentikasi.
- Menentukan apa yang diizinkan atau tidak diizinkan untuk dilakukan oleh pengguna dalam sistem.
- Berfokus pada apa yang bisa dilakukan pengguna, seperti mengakses data tertentu, membuat perubahan, atau menjalankan fungsi spesifik.
- Contoh: Setelah login, hanya pengguna dengan peran admin yang dapat mengakses halaman pengaturan.

### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
- Django mengingat pengguna yang telah login dengan menggunakan session dan cookies. Setelah pengguna berhasil login, Django membuat session yang disimpan di server dan mengirimkan cookie khusus kepada browser pengguna untuk melacak session tersebut. 
- Cookies memiliki beberapa kegunaan lain, seperti:
   1. Menyimpan Preferensi Pengguna:
      Cookies digunakan untuk menyimpan preferensi pengguna, seperti tema, bahasa, atau pengaturan tampilan, yang membuat pengalaman pengguna lebih personal.
   2. Pelacakan Pengguna (Tracking):
      Cookies sering digunakan untuk melacak aktivitas pengguna di sebuah situs web, seperti item yang ditambahkan ke keranjang belanja atau halaman yang dilihat.
   3. Penyimpanan Data Sementara:
      Cookies dapat menyimpan data sementara yang diperlukan antar halaman, seperti status form, progress kuis, atau data yang perlu disimpan sementara sebelum dikirimkan ke server.
   4. Autentikasi dan Keamanan:
      Selain session management, cookies juga digunakan untuk token autentikasi seperti JWT (JSON Web Token) untuk mengelola otentikasi yang lebih kompleks pada aplikasi modern.
  Namun, tidak semua cookies aman digunakan.

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
1. Menambahkan import UserCreationForm dan messages pada views.py.
2. Menambahkan fungsi register ke views.py.
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
3. Membuat file register.html untuk menampilkan halaman login.
```python
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```
4. Tambahkan path ke urls.py
5. Menambahkan import authenticate, login, AuthenticationForm, dan logout.
6. Lalu tambahkan 2 kode ini ke views.py.
```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')
```
7. Setelah itu buat file login.html.
```python
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```
8. Lalu tambahkan path-path url yang dibutuhkan ke urls.py
### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Saya lakukan dengan membuat akun di form register pada program dan mengisi field-field yang dibutuhkan

### Menghubungkan model Product dengan User.
1. Import model User ke models.py
2. Menambahkan potongan kode
```python
 user = models.ForeignKey(User, on_delete=models.CASCADE)
```
   ke model Gunpla yang sudah dibuat
3. Mengubah fungsi create_gunpla agar menyimpan objek yang sudah dibuat dan menghubungkannya ke User.
```python
def create_gunpla(request):
    form = GunplaForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        gunpla = form.save(commit=False)
        gunpla.user = request.user
        gunpla.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_gunpla.html", context)
```
4. Mengubah nilai 'name' pada context menjadi ```bash 'name': request.user.username, ```.
5. Tambahkan import os pada settings.py dan mengganti DEBUG menjadi ```bash PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION ```.
6. Migrate model.
###  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. Menambahkan import HttpResponseRedirect, reverse, dan datetime pada views.py
2. Menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Caranya adalah dengan mengganti kode yang ada pada blok if form.is_valid() menjadi potongan kode berikut.
```python
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```
3. Menambahkan potongan kode 'last_login': request.COOKIES['last_login'] ke dalam variabel context.
```python
def show_main(request):
    gunplas = Gunpla.objects.filter(user=request.user)

    context = {
        'nama': request.user.username,
        'kelas': 'PBP B',
        'gunpla': gunplas,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```
4. Tambahkan potongan kode ini ke main.html untuk menampilkan data login terakhir.
```python
<h5>Sesi terakhir login: {{ last_login }}</h5>
```
