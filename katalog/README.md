Tugas 2

Berikut merupakan link dari pengerjaan tugas 2: https://tugas2-pbp-zanet.herokuapp.com/katalog/ 

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
  ![djanggggggggggggo](https://user-images.githubusercontent.com/112609911/190220740-6e486da6-56a9-4cb9-b49a-971d4df68bda.jpg)
  
  Bagan tersebut menjelaskan tentang bagaimana request oleh user atau client dijalankan. Pertama, user atau client akan mengirim request berupa akses ke urls.py. Lalu, request akan diterima oleh Django dan akan di ekstraksi argumennya, kemudian request akan dikirimkan ke URLs. URLs akan menerima request dan meneruskannya ke views.py. Setelah itu, views.py akan mencari template (html) yang tepat. Selain itu, views.py juga akan melakukan identifikasi model yang cocok dengan melakukan interaksi dengan database. Setelah menemukan template yang tepat, halaman website akan ditampilkan ke user. 

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
  
  Virtual environments adalah tools untuk membuat lingkungan python virtual yang terisolasi. Terisolasi merupakan tertutup dan tidak dapat diakses oleh dunia luar. Virtual environment digunakan agar tidak terjadi konflik antara satu aplikasi dengan aplikasi lainnya. Contohnya, aplikasi 1 membutuhkan Django versi 1.1 dan aplikasi 2 membutuhkan Django versi 4.0, dengan virtual environment aplikasi 1 dan aplikasi 2 dapat dijalankan secara terpisah dengan versi Django yang berbeda. Pembuatan aplikasi web berbasis Django bisa dibuat tanpa menggunakan virtual environment, tetapi kemungkinan terjadi konfliknya terlalu besar. 

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
    
    a. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.
      
      Pada views.py, untuk mengambil model maka perlu import CatalogItem dari katalog.models. Data yang diambil berupa list barang, nama, dan npm. Dalam views. py akan dibuat sebuah fungsi bernama show_katalog dengan parameter request. Di dalam fungsi tersebut terdapat beberapa context yang ingin ditampilkan seperti list_barang, nama, dan npm. Fungsi akan merender dan mengembalikan context tersebut ke dalam katalog.html. User dapat melihat tampilan context pada html tersebut. 
    
    b. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.
       
       Pembuatan routing untuk memetakan fungsi pada views.py adalah dengan menambahkan urlspatterns berikut ke dalam urls.py di project_django.
       path('katalog/', include('katalog.urls')), 
   
   c. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.
       
       Untuk memetakan nama dapat menggunakan sintaks {{nama}} dan untuk memetakan npm dapat menggunakan sintaks {{npm}}. Untuk memetakan list barang dapat menggunakan for barang in list_barang, dan memanggil yang perlu ditampilkan dengan sintaks seperti berikut,
        {% for barang in list_barang %}
            <tr>
                <th>{{barang.item_name}}</th>
                <th>{{barang.item_price}}</th>
                <th>{{barang.item_stock}}</th>
                <th>{{barang.rating}}</th>
                <th>{{barang.description}}</th>
                <th>{{barang.item_url}}</th>
            </tr>
    
    d. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
       
       Melakukan deployment dapat dilakukan dengan membuat akun di Heroku terlebih dahulu. Setelah itu, buat aplikasi baru. Kemudian, masukan HEROKU_API_KEY (tersedia pada accounts settings Heroku) dan HEROKU_APP_NAME (nama aplikasi Heroku) ke dalam github repository > secrets -> action. Kemudian jalankan pilih opsi actions dan jalankan workflows.
