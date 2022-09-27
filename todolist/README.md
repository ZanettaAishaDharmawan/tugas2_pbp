# Tugas 4
Link heroku: https://tugas2-pbp-zanet.herokuapp.com/todolist/login/
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
``` {% csrf_token %} ``` merupakan bagian penting untuk sekuritas. CSRF merupakan suatu _built in_ 
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
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
