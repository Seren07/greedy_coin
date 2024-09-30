## Nama Kelompok
1. Muhammad Hafiz Dicky Putra (L0123096)  
2. Nadzira Rifqi Amin Rinawan (L0123104)  

### Apa itu Greedy Coin?
Merupakan sebuah program yang mengimplementasikan _Greedy Algorithm_ atau algoritma rakus untuk menyelesaikan masalah **coin change**. Tujuannya adalah mencari cara paling sedikit untuk memberikan kembalian uang dengan sejumlah koin yang tersedia. Algoritma greedy pada prinsipnya mengambil keputusan terbaik di setiap langkah dengan harapan solusi akhirnya adalah yang terbaik secara keseluruhan.

### Gambaran Program
Himpunan kandidat = list coin [10,5,2,1]  
Himpunan solusi = jumlah koin pada setiap nilainya  
Fungsi seleksi = mengurangi jumlah uang mulai dari koin dengan nilai terbesar sampai koin yang terkecil dan menambahkan jumlah koin pada setiap pengurangannya  
Fungsi kelayakan = jumlah uang sama dengan nol  
Fungsi objektif = meminimumkan total jumlah koin  

