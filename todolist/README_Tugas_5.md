# Tugas 5
Link heroku: https://tugas2-pbp-zanet.herokuapp.com/todolist/login/
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
**Inline CSS**
Inline CSS digunakan untuk tag HTML tertentu. Style dapat ditambahkan pada setiap tag. Cara ini kurang direkomendasikan dan mempersulit web developer. Inline CSS berguna jika ingin mengubah 1 style component saja. 
Kelebihan inline CSS:
- Berfungsi jika ingin menguji dan melihat perubahan
- Berguna jika ingin perbaikan cepat
- HTTP Request lebih kecil

Kekurangan inline CSS:
- Inline CSS harus diterapkan pada setiap elemen
- Penerapan membutuhkan waktu yang lebih lama 

**Internal CSS**
Kode CSS internal diletakkan di dalam bagian <head> pada halaman. Class dan ID bisa digunakan untuk merujuk pada kode CSS, namun hanya akan aktif pada halaman tersebut
Kelebihan internal CSS:
- Perubahan hanya terjadi pada 1 halaman
- Class dan ID bisa digunakan oleh internal stylesheet
- Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

Kekurangan internal css:
- Meningkatkan waktu akses website
- Perubahan hanya terjadi pada 1 halaman
- kurang efisien jika ingin menerapkan style pada satu file
  
**External CSS**
External CSS adalah kode CSS yang ditulis terpisah dari kode HTML. External CSS ditulis di sebuah file khusus menggunakan ekstensi .css.
Kelebihan external CSS:
- Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
- Kecepatan loading menjadi lebih cepat
- File CSS yang sama bisa digunakan di banyak halaman.

Kekurangan external css:
- Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

## Jelaskan tag HTML5 yang kamu ketahui.
- ``` <section> ``` : Merupakan dokumen yang dapat digunkan untuk h1 - h6
- ``` <article> ``` : Merupakan sepotong independen isi dokumen, seperti sebuah blog atau artikel koran.
- ``` <header> ```  : Merupakan bagian kepala dari dokumen
- ``` <footer> ```  : Merupakan bagian catatan kaki
- ``` <nav> ```     : Merupakan bagian dari dokumen yang dimaksudkan untuk memudahkan dalam proses navigasi

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selector tag html
2. Selector ID: dipanggil dengan atribut 'id'
3. Selector Class: Saat memilih elemen dengan id tertentu maka ditulis dengan karakter (#)
4. Selector Group: memilih semua elemen HTML dengan style css yang sama. Untuk Group Selector, pisahkan setiap selector dengan tanda koma.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Mendownload CSS dan JS pada bootsrap dan memasukkannya ke dalam file static
2. Menghias file .html dengan pembuatan diawali dengan 
  ```
  {% load static %}
<!doctype html>
<html lang="en">
  <head>
    <title>ToDo List</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    <link href="{% static 'css/style.css' %}" rel="stylesheet">
  </head>
  <body>
  ```
 3. Mengaplikasikan komponen ke dalam html menggunakan kode yang ada pada Bootstap
