# Tugas 4


  1. Menjalankan Program 
  
      ![enter image description here](Dokumentasi/run_program.png)

  2. Client 
     - Client bisa memilih 3 Command
     - Command Download : Untuk Mengambil File dari server
     - Command Upload : Untuk Mengupload File se server
     - Command List : Untuk Melihat daftar File server
  
      ![enter image description here](Dokumentasi/client.png)

  3. List file Server
     Ketika command List di jalankan 
      ![enter image description here](Dokumentasi/list.png)

  4. Download File From Server
     Ketika command download dijalankan
      ![enter image description here](Dokumentasi/download.png)

  5. Upload File To Server
     Ketika command upload dijalankan
      ![enter image description here](Dokumentasi/upload.png)

  6. Client Download Code
      - Client merequest suatu file yang ada di storage server dengan memberikan nama file yang akan dituju, lalu server meresponse mencari file di dalam storagenya, lalu setelah file ditemukan maka server akan mengirimkannya ke storage client
  
      ![enter image description here](Dokumentasi/code_download.png)

  7. Client Upload Code
      - client mengupload suatu file yang dipilih, untuk dicopykan ke dalam storage server
      ![enter image description here](Dokumentasi/code_upload.png)

  8. Client List Code
      - Disini Client merequest daftar file yang ada di dalam storage server, lalu server yang akan meresponnya dan mereturn semua list file di dalam storage server
      
      ![enter image description here](Dokumentasi/code_list.png)

  9. Protocol 
     - Terdapat 3 Protokol utama yaitu list, download, upload digunakan di setiap client yang merequest proses dengan menggunakan command 
     
      ![enter image description here](Dokumentasi/protocol.png)

  10. Storage Server
      
      ![enter image description here](Dokumentasi/storage_server.png)

  11. Storage Client
  
      ![enter image description here](Dokumentasi/storage_client.png)
