# Tugas 6
Link heroku: https://tugas2-pbp-zanet.herokuapp.com/todolist/login/
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Synchronus programming mengeksekusi kode program satu-satu per baris. Task di eksekusi satu-satu sesuai dengan urutan task. Pada synchronus programming membutuhkan waktu yang lebih lama untuk dieksekusi. 

Asynchronus programming tidak terikat dengan input dan output. Asynchronus programming tidak mengeksekusi kode program per baris. Asynchronus bekerja secara independen.Synchronus programming mengeksekusi program lebih cepat dibandingkan synchronus

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming.

Event driven programming adalah suatu paradigma pemrograman yang alurnya ditentukan oleh user. Contohnya sesperti merespons ketika user melakukan click terhadap suatu button. 
 
## Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Penerapan asynchronus programming pada ajax ketika user melakukan event driven programming. Ketika menekan tombol create di modal ajax akan menampung data dan akan dikirimkan ke server secara asynchronus. 

## Jelaskan penerapan asynchronous programming pada AJAX.

Penerapan asynchronus pada ajax terjadi saat user menambahkan data, maka website melakukan update data tanpa harus merefresh halaman tersebut. Contohnya saat user melakukan event driven programming, maka ajax akan menampung data dan mengirimkan data ke server secara asynchronus. Pada tugas ini, dapat dilihat ketika user menambahkan task baru, maka akan terbentuk card yang langsung muncul tanpa harus mereload halaman. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat fungsi show_ajax pada views.py dengan return JSONResponse data yang telah di POST
2. Menambahkan 'todolist/json' ke dalam path di urls.py
3. Membuat fungsi get data pada todolist.html, menggunakan data yang ada pada json
4. Membuat modal pada todolist.html
5. Membuat tombol Create Task dipetakan untuk membuka modal
6. Ketika menekan tombol create pada modal, maka akan memanggil fungsi add_ajax
7. Kemudian data akan diambil dan card akan ditambahkan
