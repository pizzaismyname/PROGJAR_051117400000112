# Tugas 10

- Jalankan `async_server.py` pada port 9002, 9003, 9004, 9005  
![2](screenshot/2.png)  
- Jalankan file `lb.py`, jalankan di port 44444  
![3](screenshot/3.png)  
- Jalankan browser, akseslah `http://localhost:44444/page.html`  
![4](screenshot/4.png)  
- Lihatlah di log program, bahwa setiap request akan dilayani oleh backend yang bergantian  
![5_1](screenshot/5_1.png)  
![5_2](screenshot/5_2.png)  
- Lakukan performance test, bandingkan penggunaan __load balancer__  
  - [Screenshot `async_server.py`](https://htmlpreview.github.io/?https://github.com/pizzaismyname/PROGJAR_051117400000112/blob/master/tugas10/screenshot/async_server.html)  
  - [Screenshot `server_thread_http.py`](https://htmlpreview.github.io/?https://github.com/pizzaismyname/PROGJAR_051117400000112/blob/master/tugas9/screenshot/server_thread_http.html)
- Tabel hasil performance test
  - [async_server.py](../tugas10/async_server.py)  
    | No test | Concurrency level | Time taken for test (seconds) | Complete request | Failed request | Total transferred (bytes) | Request per second | Time per request (ms) | Transfer rate (Kbytes/sec) |
    |---------|-------------------|-------------------------------|------------------|----------------|---------------------------|--------------------|-----------------------|----------------------------|
    | 1       | 1                 | 0.646                         | 1000             | 0              | 122000                    | 1549.09            | 0.646                 | 184.56                     |
    | 2       | 5                 | 0.542                         | 1000             | 0              | 122000                    | 1844.11            | 2.711                 | 219.71                     |
    | 3       | 10                | 0.640                         | 1000             | 0              | 122000                    | 1562.98            | 6.398                 | 186.21                     |
    | 4       | 30                | 0.620                         | 1000             | 0              | 122000                    | 1613.40            | 18.594                | 192.22                     |
    | 5       | 50                | 0.608                         | 1000             | 0              | 122000                    | 1644.70            | 30.401                | 195.95                     |
    | 6       | 100               | 0.505                         | 1000             | 0              | 122000                    | 1980.94            | 50.481                | 236.01                     |
  - [Server_thread_http.py](../tugas9/server_thread_http.py)  
    | No test | Concurrency level | Time taken for test (seconds) | Complete request | Failed request | Total transferred (bytes) | Request per second | Time per request (ms) | Transfer rate (Kbytes/sec) |
    |---------|-------------------|-------------------------------|------------------|----------------|---------------------------|--------------------|-----------------------|----------------------------|
    | 1       | 1                 | 409.798                       | 1000             | 0              | 122000                    | 2.44               | 409.798               | 0.29                       |
    | 2       | 5                 | 180.725                       | 1000             | 0              | 122000                    | 5.53               | 903.624               | 0.66                       |
    | 3       | 10                | 184.945                       | 1000             | 0              | 122000                    | 5.41               | 1849.452              | 0.64                       |
    | 4       | 30                | 170.246                       | 1000             | 0              | 122000                    | 5.87               | 5107.387              | 0.67                       |
    | 5       | 50                | 354.162                       | 1000             | 0              | 122000                    | 2.82               | 17708.086             | 0.29                       |
    | 6       | 100               | 317.385                       | 1000             | 0              | 122000                    | 3.15               | 31738.456             | 0.32                       |
