# Tugas 10 
## Hendra Ramadani (05111740000055)

Pertama-tama kita jalankan dulu server_thread / async_server , lalu kita jalankan runserver.sh dengan command `bash runserver.sh` , setelah itu yang terakhir kita jalankan load balancernya 

![enter image description here](Dokumentasi/run.PNG)

lalu coba kita akses http://localhost:44444/page.html

![enter image description here](Dokumentasi/browser.PNG)


Untuk benchmarking menggunakan port dari loadbalancer
## Server_thread_http.py di port 44444
### 1. `ab -n 1000 -c 1 http://127.0.0.1:44444/`
1000 Request with 1 concurency

![enter image description here](Dokumentasi/1.PNG)

### 2. `ab -n 1000 -c 10 http://127.0.0.1:44444/`
1000 Request with 10 concurency

![enter image description here](Dokumentasi/2.PNG)

### 3. `ab -n 1000 -c 50 http://127.0.0.1:44444/`
1000 Request with 50 concurency

![enter image description here](Dokumentasi/3.PNG)

### Comparison Table

![enter image description here](Dokumentasi/7.PNG)


## Server_async_http.py di port 44444
### 1. `ab -n 1000 -c 1 http://127.0.0.1:44444/`
1000 Request with 1 concurency

![enter image description here](Dokumentasi/4.PNG)

### 2. `ab -n 1000 -c 10 http://127.0.0.1:44444/`
1000 Request with 10 concurency

![enter image description here](Dokumentasi/5.PNG)

### 3. `ab -n 1000 -c 50 http://127.0.0.1:44444/`
1000 Request with 50 concurency

![enter image description here](Dokumentasi/6.PNG)

### Comparison Table

![enter image description here](Dokumentasi/8.PNG)
