 # Tugas 3

link heroku: https://tugas2-pbp-zanet.herokuapp.com/mywatchlist/html/
 
 ## Jelaskan perbedaan antara JSON, XML, dan HTML!
**JSON (JavaScript Object Notation)** 

JSON merupakan format data dalam bentuk JavaScript. JSON digunakan untuk menyimpan informasi dengan cara terorganisir dan mudah di akses. JSON berjalan lebih cepat dibandingkan XML dan HTML karena JSON dirancang khusus untuk pertukaran data dan parser JSON kurang kompleks. Data menggunakan JSON lebih mudah ditukarkan
oleh komputer karena tidak memakan memori banyak.  

**XML (Extensible Markup Language)**

XML merupakan bahasa markup yang digunakan untuk pertukaran data. XML disajukan secara ringkas dan mudah diatur. Pertukaran data menggunakan XML lebih mudah dilakukan karena memberikan struktur yang jelas dan juga terdapat konfigurasi terhadap variabel. Data pada XML disimpan sebagai struktur pohon. 

**HTML (Hypertext Markup Language)**

HTML digunakan untuk membuat halaman web dan aplikasi web. HTML mudah dimengerti dan memiliki sintaks yang sangat sederhana. Penggunaan HTML dinilai kurang cocok untuk pertukaran data. 

## Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery dibutuhkan agar data dapat terjadi pertukaran data user dengan data server. Data delivery memudahkan pertukaran data. Request data biasanya menggunakan HTML page, style sheet, JPG image, JavaScript code, XML, ataupun JSON. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi mywatchlist dengan perintah ``` python manage.py startapp mywatchlist ```
2. Menambahkan path mywatchlist kedalam urls.py yang ada pada project_django dengan perintah ``` path('mywatchlist/', include('mywatchlist.urls')), ```
3. Menjalankan localhost dengan perintah ``` python manage.py runserver ```
4. Membuat model pada models.py yang menampilkan atribut watched, title, rating, release_date, review. Kemudian melakukan make migrations dan migrate dengan perintah ``` python manage.py makemigrations ``` dan  ``` python manage.py migrate ```
   ``` class MyWatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.CharField(max_length=255) ```
6. Menambahkan data dengan membuat file initial_mywatchlist_data.json pada folder fixtures dan mengisinya dengan 10 data yang perlu diisi berdasarkan model yang tersedia
7. Menambahkan fungsi untuk show_mywatchlist untuk html, show_xml untuk menampilkan xml, dan show_json untuk menampilkan json
8. Menambahkan path ke urls pattern agar dapat diakses menggunakan html, xml, dan json
   ``` 
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_xml, name="show_xml"),
    path('json/', show_json, name="show_json"), ```
9. Kemudian, lakukan git add, push, dan commit. Aplikasi akan terdeploy secara otomatis. 


## Tampilan Postman
 
### HTML
![html2](https://user-images.githubusercontent.com/112609911/191646295-7c18eb75-df25-454c-8f1d-aa8de1456515.jpg)

### XML
![xml2](https://user-images.githubusercontent.com/112609911/191646311-dd3abd14-69cb-4613-9b04-d52280f55e6c.jpg)

### JSON
![json2](https://user-images.githubusercontent.com/112609911/191646317-d489aadb-4d6d-4786-a302-11a6590550f8.jpg)
