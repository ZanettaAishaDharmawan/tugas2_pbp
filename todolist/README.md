# Tugas 4
Link heroku: https://tugas2-pbp-zanet.herokuapp.com/todolist/login/
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
``` {% csrf_token %} ``` merupakan bagian penting untuk sekuritas. CSRF merupakan suatu _built in_ yang dimiliki oleh django. Token csrf bersifat unik. Token CSRF dibuat pada server dan dikirimkan ke klien dalam bentuk HTTP request. Jika tidak ada elemen token tersebut maka CSRF dapat diserang.
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Bisa, ada beberapa cara untuk membuat table, berikut merupakah contohnya
```
<form method="POST" action="">
        {% csrf_token %}
        <table>
        ...........................
        </table>
</form>
```
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Setelah mengisi submisi dan menekan tombol submit, lakukan pengecekan data yang di input sesuai dengan format pada models.py. Kemudian, data akan tersimpan pada database. Berikut merupakan contoh tampilan dan pemanggilan date, title, dan description pada html.
```
{% for todo in list_todo %}
        <tr>
            <th>{{todo.date}}</th>
            <th>{{todo.title}}</th>
            <th>{{todo.description}}</th>
```
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat aplikasi baru bernama todolist dengan menggunakan perintah ``` python manage.py startapp wishlist ```
2. Menambahkan path todolist ke dalam urls.py pada folder project django dan masukkan ``` path('todolist/', include('todolist.urls')), ``` pada urlpatterns
3. Membuat atribut pada models.py dengan nama Class Task yang berisikan atribut user, date, title, dan description
4. Membuat beberapa fungsi pada views.py berupa show_todolist, register_user, login_user, logout_user, dan create_task
5. Menambahkan routing pada urls.py berupa
  ```
  urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('delete-task/<int:pk>', delete_task, name='delete-task'),
    path('change-task/<int:pk>', change_task, name='change-task'),
]
  ```
6. Menambahkan beberapa halaman .html untuk redirect page ke login.html, register.html, todolist.html, dan tambah.html. Kemudian mengedit beberapa field sesuai dengan atribut yang tersedia pada models.py
7. Add, commit, dan push file ke git. Kemudian melakukan deploy.
8. Membuat 2 akun pengguna dengan 3 dummy di aplikasi heroku.
