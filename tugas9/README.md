# Tugas 9

- Jalankan kedua model
  - [Server_async_http.py](../tugas9/server_async_http.py) di port 45000
  - [Server_thread_http.py](../tugas9/server_thread_http.py) di port 46000
- Ujicobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi  
  - [Screenshot server_async_http.py](https://htmlpreview.github.io/?https://github.com/pizzaismyname/PROGJAR_051117400000112/blob/master/tugas9/screenshot/server_async_http.html)
  - 
- Tabel hasil ujicoba
  - Server Asynchronous HTTP  
    | No test | Concurrency level | Time taken for test (seconds) | Complete request | Failed request | Total transferred (bytes) | Request per second | Time per request (ms) | Transfer rate (Kbytes/sec) |
    |---------|-------------------|-------------------------------|------------------|----------------|---------------------------|--------------------|-----------------------|----------------------------|
    | 1       | 1                 | 0.426                         | 1000             | 0              | 122000                    | 2344.68            | 0.426                 | 279.35                     |
    | 2       | 5                 | 0.416                         | 1000             | 0              | 122000                    | 2401.73            | 2.082                 | 286.14                     |
    | 3       | 10                | 0.573                         | 1000             | 0              | 122000                    | 1745.28            | 5.730                 | 207.93                     |
    | 4       | 30                | 0.449                         | 1000             | 0              | 122000                    | 2229.55            | 13.456                | 265.63                     |
    | 5       | 50                | 0.458                         | 1000             | 0              | 122000                    | 2181.15            | 22.924                | 259.86                     |
    | 6       | 100               | 0.405                         | 1000             | 0              | 122000                    | 2468.48            | 40.511                | 294.10                     |
  - Server Thread HTTP  
  tabel disini
