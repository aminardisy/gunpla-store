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
# Tugas 5
### Implementasikan fungsi untuk menghapus dan mengedit product.
1. Buat fungsi edit_mood di views.py
```python
def edit_gunpla(request, id):
    gunpla = Gunpla.objects.get(pk = id)

    form = GunplaForm(request.POST or None, instance=gunpla)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_gunpla.html", context)
```
2. Tambahkan import ke views.py
3. Buatlah berkas HTML baru dengan nama edit_gundam.html pada subdirektori main/templates.
```python
{% extends 'base.html' %}

{% load static %}

{% block content %}

<h1>Edit Mood</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Edit Gundam"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
4. Import dan tambahkan path fungsi yang sudah dibuat ke urls.py.
5. Tambahkan potongan kode untuk manampilkan tombol edit.
### Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:
Karena ini pertama kalinya saya mendesign web, design web yang ditampilkan mengacu pada template yang disediakan.
#### Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
##### Menampilkan Pesan dan Gambar Jika Belum Ada Produk.
1. Tambahkan logika untuk mengecek produk yang tersimpan
2. Jika tidak ada produk, tampilkan pesan "Belum ada data Gunpla dalam koleksi".
##### Menampilkan Produk dalam Bentuk Card
1. Gunakan Tailwind CSS untuk mendesain tampilan card.
2. Ubah bagian template yang menampilkan produk sehingga setiap produk ditampilkan dalam card yang menarik dan tidak sama dengan tutorial.
3. Card mencakupi:
   1. Gambar Produk (masih belum selesai)
   2. Nama Produk
   3. Deskripsi produk
   4. Harga Produk
   5. Dua tombol untuk edit dan hapus produk
##### Membuat Tombol Edit dan Delete Produk
- Tambahkan dua tombol pada setiap card produk:
  - Tombol Edit: Mengarahkan pengguna ke halaman pengeditan produk (edit_gundam).
  - Tombol Hapus: Mengarahkan pengguna ke halaman konfirmasi penghapusan (delete_gundam).
##### Membuat Navbar yang Responsif
1. Gunakan Tailwind CSS untuk membuat navbar yang responsif.
### Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas selector dari yang terendah ke yang tertinggi adalah sebagai berikut:
1. Selector Tag / Elemen (e.g., h1, p).
2. Selector Class (e.g., .class-name).
3. Selector Atribut (e.g., [type='text']).
4. Selector Pseudo-class (e.g., :hover, :focus).
5. Selector ID (e.g., #id-name).
6. Inline CSS (e.g., <div style="color: red;">).
7. !important rule: Aturan !important akan mengesampingkan semua prioritas lain dan akan diterapkan pada elemen, terlepas dari specificity.
### Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive Design adalah pendekatan desain web yang memastikan tampilan dan fungsionalitas situs dapat beradaptasi dengan baik pada berbagai perangkat dan ukuran layar, seperti desktop, tablet, dan ponsel. Ini sangat penting karena pengguna mengakses website dari perangkat yang beragam dengan resolusi layar yang berbeda-beda.

Alasan Mengapa Responsive Design Penting:
1. Meningkatkan Pengalaman Pengguna (User Experience): Layout yang responsif memberikan kemudahan navigasi dan keterbacaan konten.
2. SEO yang Lebih Baik: Mesin pencari seperti Google memberi peringkat lebih tinggi pada situs yang responsif.
3. Meningkatkan Aksesibilitas: Memastikan bahwa situs dapat diakses oleh berbagai pengguna dengan perangkat yang berbeda.
4. Penggunaan Sumber Daya Lebih Efisien: Menghindari pembuatan beberapa versi situs untuk perangkat berbeda.

Contoh:
- Situs dengan Responsive Design: https://www.apple.com
   Desain situs Apple akan beradaptasi sempurna ketika dibuka di ponsel, tablet, dan desktop. Ukuran gambar, tata letak        konten, dan menu berubah sesuai dengan perangkat.
- Situs Tanpa Responsive Design: http://example.com
   Pada situs tanpa responsivitas, elemen seperti gambar, teks, dan layout akan terlihat sama pada semua perangkat,            menyebabkan tampilan yang tidak rapi, konten yang terpotong, dan interaksi yang sulit pada layar kecil.
### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Ketiga properti ini digunakan untuk mengatur ruang di sekitar dan di dalam elemen HTML. Berikut adalah penjelasan perbedaannya:

1. Margin:
- Mengatur ruang di luar border dari elemen.
- Membuat jarak antara elemen yang berdekatan.
Contoh penggunaan:
```css
Salin kode
.box {
    margin: 20px;
}
```
2. Border:
- Merupakan bingkai di sekitar padding dan konten elemen.
- Border dapat diatur ketebalan, jenis garis, dan warnanya.
Contoh penggunaan:
```css
Salin kode
.box {
    border: 2px solid black;
}
```
3. Padding:
- Mengatur ruang di dalam border, tetapi di luar konten.
- Memberikan jarak antara border dengan teks atau konten di dalam elemen.
Contoh penggunaan:
```css
Salin kode
.box {
    padding: 10px;
}
```
### Jelaskan konsep flex box dan grid layout beserta kegunaannya!
1. Flexbox (Flexible Box Layout):
Flexbox digunakan untuk membuat layout yang fleksibel dan dapat menyesuaikan dengan ukuran konten dan ruang yang tersedia.
Kegunaan:
- Mengatur tata letak baris atau kolom dari elemen.
- Mengatur posisi elemen dengan cepat, termasuk perataan vertikal dan horizontal.
2. Grid Layout:
Grid layout adalah sistem tata letak berbasis grid dua dimensi yang memungkinkan Anda untuk membuat tata letak yang lebih kompleks dengan baris dan kolom.
Kegunaan:
- Membagi halaman menjadi grid dengan baris dan kolom.
- Memudahkan pengaturan layout yang rumit, seperti dashboard atau halaman dengan beberapa section.

# Tugas 6
### Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memiliki berbagai manfaat dalam pengembangan aplikasi web, antara lain:
- Interaktivitas: JavaScript memungkinkan pengembang menambahkan elemen interaktif pada halaman web, seperti animasi, dropdown menu, validasi form di sisi klien, dan lain-lain, yang membuat halaman lebih dinamis dan interaktif.
- Manipulasi DOM: Dengan JavaScript, pengembang dapat memodifikasi elemen-elemen pada halaman web secara langsung, misalnya mengubah gaya elemen, menambahkan konten baru, atau menghapus elemen.
- Komunikasi Asinkron: JavaScript memungkinkan pengembang menggunakan teknologi seperti AJAX untuk berkomunikasi dengan server secara asinkron tanpa perlu me-refresh halaman, sehingga pengalaman pengguna menjadi lebih mulus.
- Pengembangan Aplikasi Web Front-End dan Back-End: Dengan perkembangan framework seperti Node.js, JavaScript kini juga dapat digunakan untuk pengembangan sisi server, sehingga memungkinkan penggunaan satu bahasa pemrograman untuk keseluruhan aplikasi (full-stack).
- Mendukung Single Page Application (SPA): JavaScript digunakan dalam framework modern seperti React, Angular, dan Vue untuk membangun aplikasi web yang responsif dan berbasis SPA.

### Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Ketika kita menggunakan fetch() untuk mengambil data dari server, await digunakan untuk menunggu respons dari server sebelum melanjutkan ke baris kode berikutnya. Fungsinya adalah untuk:
- Membuat kode lebih mudah dibaca dan dikelola: Dengan await, kita dapat menulis kode asinkron dengan cara yang terlihat seperti kode sinkron, sehingga lebih mudah dipahami.
- Menangani Data Respons secara Tepat: await memastikan bahwa respons dari fetch() telah diterima sepenuhnya sebelum kita mencoba mengakses hasilnya, misalnya membaca JSON dari respons.
Jika kita tidak menggunakan await, maka fetch() akan mengembalikan promise tanpa menunggu respons dari server selesai. Akibatnya, jika kita mencoba menggunakan hasil fetch() tersebut (misalnya response.json()), kita akan mengalami kesalahan karena kita mencoba mengakses nilai yang belum ada.

### Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST
CSRF (Cross-Site Request Forgery) adalah serangan yang mengeksploitasi otentikasi pengguna untuk menjalankan tindakan tak diinginkan di sisi server. Dalam Django, decorator @csrf_exempt digunakan untuk menonaktifkan proteksi CSRF pada view tertentu. Kita perlu menggunakan @csrf_exempt pada view yang digunakan untuk AJAX POST ketika:
- Token CSRF Tidak Dikirimkan Secara Benar: Ketika permintaan AJAX POST tidak menyertakan token CSRF yang valid atau saat kita tidak ingin menambahkannya di sisi klien, Django akan memblokir permintaan tersebut karena dianggap berbahaya.
- Menghindari Error: Jika kita tidak menggunakan @csrf_exempt dan AJAX POST tidak menyertakan token CSRF yang benar, Django akan membalas dengan kesalahan "Forbidden (403)", yang menyebabkan request gagal.
Namun, penggunaan @csrf_exempt harus dilakukan dengan sangat hati-hati, karena menonaktifkan proteksi CSRF dapat membuat aplikasi lebih rentan terhadap serangan CSRF.

### Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data input pengguna di backend penting dilakukan meskipun validasi di frontend sudah ada karena:
- Keamanan: Validasi di frontend mudah diabaikan oleh pengguna yang mencoba menyerang aplikasi, misalnya dengan memodifikasi kode JavaScript atau mengirimkan permintaan langsung ke server menggunakan alat seperti Postman.
- Integritas Data: Dengan melakukan pembersihan data di backend, kita memastikan bahwa semua data yang masuk ke dalam sistem memenuhi standar yang telah ditetapkan, terlepas dari bagaimana data tersebut dikirimkan.
- Single Source of Truth: Backend adalah satu-satunya tempat di mana validasi dapat dipastikan selalu berjalan. Validasi di frontend hanya berfungsi sebagai lapisan tambahan untuk meningkatkan UX, tetapi backend adalah pengendali utama dari integritas data.
- Mengurangi Kerentanan Terhadap Manipulasi Data: Tanpa pembersihan data di backend, aplikasi akan rentan terhadap serangan injeksi, XSS (Cross-Site Scripting), dan serangan-serangan lainnya yang dapat dieksploitasi dari input pengguna yang tidak aman.
Oleh karena itu, validasi di frontend tidak cukup untuk menjamin keamanan dan keandalan data—pembersihan data di backend tetap diperlukan.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
#### AJAX GET
1. Ubahlah kode cards data mood agar dapat mendukung AJAX GET dengan menambahkan kode berikut
```python
   async function refreshGunplas() {
    document.getElementById("gunpla_cards").innerHTML = "";
    document.getElementById("gunpla_cards").className = "";
    const gunplas = await getGunplas();
    let htmlString = "";
    let classNameString = "";

    if (gunplas.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="No Product :[" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data Gunpla dalam koleksi.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        gunplas.forEach((item) => {
            htmlString += `
            <div class="relative break-inside-avoid">
                <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                </div>
                <div class="relative top-5 bg-gray-800 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-yellow-600 hover:rotate-0 transition-transform duration-300">
                  <div class="bg-gray-700 text-gray-200 p-4 rounded-t-lg border-b-2 border-yellow-600">
                    <img src="{{ gunpla.image.url }}" alt="{{ gunpla.name }}" class="w-full h-48 object-cover rounded-t-lg mb-2"> <!-- Menambahkan Gambar -->
                    <h3 class="font-bold text-xl mb-2 font-orbitron">{{ gunpla.name }}</h3>
                    <p class="text-gray-400">Price: ${item.fields.price}</p>
                  </div>
                  <div class="p-4">
                    <p class="font-semibold text-lg mb-2">Description</p>
                    <p class="text-gray-300 mb-2">${item.fields.description}</p>
                    <div class="mt-4">
                      <p class="text-gray-300 font-semibold mb-2">Size Ratio</p>
                      <p class="text-gray-400">${item.fields.size_ratio}</p>
                    </div>
                    <div class="mt-4">
                      <p class="text-gray-300 font-semibold mb-2">Extensions</p>
                      <p class="text-gray-400">${item.fields.extensions}</p>
                    </div>
                    <div class="mt-4">
                      <p class="text-gray-300 font-semibold mb-2">Notes</p>
                      <p class="text-gray-400">${item.fields.notes}</p>
                    </div>
                    <div class="mt-4">
                      <p class="text-gray-300 font-semibold mb-2">Image</p>
                      <p class="text-gray-400">${item.fields.image}</p>
                    </div>
                  </div>
                </div>
                <div class="absolute top-0 -right-4 flex space-x-1">
                  <a href="/edit-gunpla/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                      <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                  </a>
                  <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                      <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                  </a>
                </div>
              </div>
            `;
        });
    }
    document.getElementById("gunpla_cards").className = classNameString;
    document.getElementById("gunpla_cards").innerHTML = htmlString;
}
  }
```
2. Lakukan pengambilan data mood menggunakan AJAX GET. Pastikan bahwa data yang diambil hanyalah data milik pengguna yang logged-in dengan mengimplementasikan kdoe berikut di views.py.
```python
 async function getGunplas(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }
```
#### AJAX POST
1.  Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan gunpla dengan mengimplementasikan kode berikut.
```python
   <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-yellow-500 hover:bg-yellow-600 text-black font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
      Add New Gunpla by AJAX
    </button>
```
2. Buatlah fungsi view baru untuk menambahkan gunpla baru ke dalam basis data dengan mengimplementasikan kode berikut.
```python
@csrf_exempt
@require_POST
def add_gunpla_ajax(request):
    user = request.user
    name = request.POST.get("name")
    image = request.POST.get("image")
    price = request.POST.get("price")
    description = request.POST.get("description")
    size_ratio = request.POST.get("size_ratio")
    extensions = request.POST.get("extensions")
    notes = request.POST.get("notes")

    new_Gunpla = Gunpla(name=name, price=price, description=description, size_ratio=size_ratio, extensions=extensions, notes=notes, user=user, image=image)
    new_Gunpla.save()
    
    return HttpResponse(b"CREATED", status=201)
```
3.  Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru dibuat dengan menambah path berikut.
```python
path('create-gunpla-ajax', add_gunpla_ajax, name='add_gunpla_ajax'),
```
4. Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/ dengan mengimport fungsi add_gunpla_ajax ke views.py
5. Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar gunpla terbaru tanpa reload halaman utama secara keseluruhan dengan menambahkan kode berikut
```python
function addGunpla() {
    fetch("{% url 'main:add_gunpla_ajax' %}", {
      method: "POST",
      body: new FormData(document.querySelector('#gunplaEntryForm')),
    })
    .then(response => refreshGunplas())

    document.getElementById("gunplaEntryForm").reset(); 
    document.querySelector("[data-modal-toggle='crudModal']").click();

    return false;
  }
```
