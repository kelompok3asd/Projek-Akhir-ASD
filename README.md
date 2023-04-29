# Projek Akhir ASD Kelompok 3: FRIEND LIST
1. Tsurayya Salsabila (2209116076)
2. Afrila Zahra Prasetyo (2209116079)
3. Adli Imam Suryadin (2209116096)

Program ini merupakan program yang menampilkan sebuah friend list didalam suatu game. Yang dimana pengguna dapat melakukan registrasi, menambahkan teman, menghapus teman, dan mengurutkan teman.

## Prasyarat
Python 3.x, linked list, merge sort, jump search.

## Mulai
Unduh file program, kemudian jalankan program menggunakan bahasa pemrograman Python.

## Cara Penggunaan
1. Ketika program mulai dijalankan, terminal akan menampilkan output berupa 3 pilihan, diantaranya yaitu registrasi, login, dan quit.
2. Untuk pengguna pertama, disarankan untuk melakukan registrasi agar data nya masuk ke dalam list pengguna. Dan saat selesai melakukan registrasi, pengguna diminta untuk melakukan login dengan username dan password yang baru saja dibuatnya.
3. Setelah berhasil login, pengguna akan melihat beberapa menu yang tertera yang dapat di akses. Yang pertama adalah menu "Show friend list" yang akan menampilkan list teman yang pengguna punyai. Namun karena pengguna baru maka list akan kosong dan teman tidak ditemukan.
4. Menu kedua merupakan "Show detailed info about a friend" yang dimana menu ini akan menampilkan menu lebih detail mengenai teman si pengguna. Detail info ini berupa nama teman, id, level, dan total achievement.
5. Selanjutnya adalah menu "Add friend" yang digunakan untuk menambahkan teman. Ini bisa jadi langkah awal yang diambil untuk menambahkan teman lalu akan masuk nama dan detail infonya ke dalam dictionary user dan detail.
6. Menu "Unfriend" digunakan untuk menghapus list teman yang ada.
7. Di kedua menu setelahnya terdapat menu "Sort by level (Ascending & Descending)", menu ini akan mengurutkan friend list berdasarkan besar angka levelnya, bisa ascending (pengurutan angka dari terkecil ke terbesar) maupun descending (pengurutan angka dari terbesar ke terkecil).
8. Menu yang terakhir adalah menu "Back" yang akan kembali ke menu sebelumnya (menu untuk login).

## Class and Function
### Class FriendList
  Class FriendList memiliki class lain didalamnya, yaitu class FriendNode. Class FriendNode ini terdiri dari beberapa function sebagai berikut.
#### Function
1. Function yang mendeklarasikan dirinya sebagai 'name', 'id_char', 'level', dan 'total_achievement'.
2. Function yang mendeklarasikan head dan size (panjang list).
3. Function add_friend dengan atribut 'name', 'id_char', 'level', dan 'total achievement'. Function ini digunakan untuk menambahkan teman baru.
4. Function remove_friend dengan atribut 'name' sebagai kata kuncinya dan digunakan untuk menghapus teman.
5. Function get_mid merge sort digunakan untuk mengambil nilai tengah dalam linked list menggunakan head.
6. Function merge_sort_ascending digunakan untuk mengembalikan linked list yang telah diurutkan dengan merge sort berdasarkan level dari yang terendah hingga yang tertinggi.
7. Function merge_sort_descending digunakan untuk mengembalikan linked list yang telah diurutkan dengan merge sort berdasarkan level dari yang tertinggi hingga yang terendah.
8. Function merge_ascending dan merge_descending digunakan untuk menggabungkan dua linked list pada merge sort secara ascending dan descending.
9. Function jump_search digunakan untuk melakukan pencarian secara acak dengan hanya menyebutkan kata kuncinya, yaitu dengan variabel 'name'.
10. Function print_friends berguna untuk menampilkan list teman yang ada pada friend list pengguna.
11. Function print_detail menggunakan variabel 'name' sebagai kata kuncinya untuk menampilkan detail info mengenai teman si pengguna.
12. Function friend_menu berguna untuk menyimpan data user dan object linked list.
13. Function register yang berguna untuk menerima dan menyimpan masukan pengguna ketika membuat username dan password.
14. Function login mengambil input pengguna untuk nama pengguna dan kata sandi yang ada, serta memeriksa kecocokan dari data.
15. Function main_menu mendefinisikan opsi menu utama untuk program dan memungkinkan pengguna untuk memilih salah satunya. 
