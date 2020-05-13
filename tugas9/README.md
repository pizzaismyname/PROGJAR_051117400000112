# Tugas 9

- Jalankan kedua model
  - [Server_async_http.py](../tugas9/server_async_http.py) di port 45000
  - [Server_thread_http.py](../tugas9/server_thread_http.py) di port 46000
- Ujicobalah dengan apache benchmark untuk 1000 request dan konkurensi yang bervariasi  
  - [Screenshot server_async_http.py](https://htmlpreview.github.io/?https://github.com/pizzaismyname/PROGJAR_051117400000112/blob/master/tugas9/screenshot/server_async_http.html)
  - 
- Tabel hasil ujicoba
  - Server Asynchronous HTTP  
    <table>
    <thead>
    <tr>
        <th>No test<br></th>
        <th>Concurrency level<br></th>
        <th>Time taken for test<br>(seconds)</th>
        <th>Complete request<br></th>
        <th>Failed request<br></th>
        <th>Total transferred<br>(bytes)</th>
        <th>Request per second<br></th>
        <th>Time per request<br>(ms)</th>
        <th>Transfer rate<br>(Kbytes/sec)</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <td>1</td>
        <td>1</td>
        <td>0.426</td>
        <td>1000</td>
        <td>0</td>
        <td>122000</td>
        <td>2344.68</td>
        <td>0.426</td>
        <td>279.35</td>
    </tr>
    <tr>
        <td>2</td>
        <td>5</td>
        <td>0.416</td>
        <td>1000</td>
        <td>0</td>
        <td>122000</td>
        <td>2401.73</td>
        <td>2.082</td>
        <td>286.14</td>
    </tr>
    <tr>
        <td>3</td>
        <td>10</td>
        <td><span style="font-weight:400;font-style:normal">0.573</span></td>
        <td>1000</td>
        <td>0</td>
        <td>122000</td>
        <td><span style="font-weight:400;font-style:normal">1745.28</span></td>
        <td><span style="font-weight:400;font-style:normal">5.730</span></td>
        <td><span style="font-weight:400;font-style:normal">207.93</span></td>
    </tr>
    <tr>
        <td>4</td>
        <td>30</td>
        <td><span style="font-weight:400;font-style:normal">0.449</span></td>
        <td>1000</td>
        <td>0</td>
        <td>122000</td>
        <td><span style="font-weight:400;font-style:normal">2229.55</span></td>
        <td><span style="font-weight:400;font-style:normal">13.456</span></td>
        <td><span style="font-weight:400;font-style:normal">265.63</span></td>
    </tr>
    <tr>
        <td>5</td>
        <td>50</td>
        <td><span style="font-weight:400;font-style:normal">0.458</span></td>
        <td>1000</td>
        <td>0</td>
        <td>122000</td>
        <td><span style="font-weight:400;font-style:normal">2181.15</span></td>
        <td><span style="font-weight:400;font-style:normal">22.924</span></td>
        <td><span style="font-weight:400;font-style:normal">259.86</span></td>
    </tr>
    <tr>
        <td>6</td>
        <td>100</td>
        <td><span style="font-weight:400;font-style:normal">0.405</span></td>
        <td>1000</td>
        <td>0</td>
        <td>122000</td>
        <td><span style="font-weight:400;font-style:normal">2468.48</span><br></td>
        <td><span style="font-weight:400;font-style:normal">40.511</span></td>
        <td><span style="font-weight:400;font-style:normal">294.10</span></td>
    </tr>
    </tbody>
    </table>
  - Server Thread HTTP  
  tabel disini
