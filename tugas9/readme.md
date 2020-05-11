# Tugas 9 - Asynchronous Processing

## Server_thread_http.py di port 46000
### 1. `ab -n 1000 -c 1 http://127.0.0.1:46000/`
1000 Request with 1 concurency

![enter image description here](Dokumentasi/Thread/1.1.PNG)

### 2. `ab -n 1000 -c 10 http://127.0.0.1:46000/`
1000 Request with 10 concurency

![enter image description here](Dokumentasi/Thread/2.1.PNG)

### 3. `ab -n 1000 -c 50 http://127.0.0.1:46000/`
1000 Request with 50 concurency

![enter image description here](Dokumentasi/Thread/3.PNG)

### Comparison Table

![enter image description here](Dokumentasi/Thread/4.PNG)


## Server_async_http.py di port 45000
### 1. `ab -n 1000 -c 1 http://127.0.0.1:45000/`
1000 Request with 1 concurency

![enter image description here](Dokumentasi/Async/1.1.PNG)

### 2. `ab -n 1000 -c 10 http://127.0.0.1:45000/`
1000 Request with 10 concurency

![enter image description here](Dokumentasi/Async/2.1.PNG)

### 3. `ab -n 1000 -c 50 http://127.0.0.1:45000/`
1000 Request with 50 concurency

![enter image description here](Dokumentasi/Async/3.1.PNG)

### Comparison Table

![enter image description here](Dokumentasi/Async/4.PNG)
