# Tugas 7

## Performance Test

[Server yang ditest](../tugas6/server_thread_http.py)

### Keluaran Hasil

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;border-color:#93a1a1;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#002b36;background-color:#fdf6e3;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#93a1a1;color:#fdf6e3;background-color:#657b83;}
.tg .tg-b406{background-color:#eee8d5;border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-9wq8{border-color:inherit;text-align:center;vertical-align:middle}
.tg .tg-7ca6{background-color:#eee8d5;border-color:#000000;text-align:center;vertical-align:middle}
.tg .tg-xwyw{border-color:#000000;text-align:center;vertical-align:middle}
</style>
<table class="tg">
  <tr>
    <th class="tg-9wq8">No test<br></th>
    <th class="tg-9wq8">Concurrency level<br></th>
    <th class="tg-9wq8">Time taken for test<br>(seconds)</th>
    <th class="tg-9wq8">Complete request<br></th>
    <th class="tg-9wq8">Failed request<br></th>
    <th class="tg-9wq8">Total transferred<br>(bytes)</th>
    <th class="tg-9wq8">Request per second<br></th>
    <th class="tg-9wq8">Time per request<br>(ms)</th>
    <th class="tg-9wq8">Transfer rate<br>(Kbytes/sec)</th>
  </tr>
  <tr>
    <td class="tg-b406" rowspan="3">1</td>
    <td class="tg-b406">1</td>
    <td class="tg-b406">0.099</td>
    <td class="tg-b406">10</td>
    <td class="tg-b406">0</td>
    <td class="tg-b406">1360</td>
    <td class="tg-b406">100.61</td>
    <td class="tg-b406">9.939</td>
    <td class="tg-b406">13.36</td>
  </tr>
  <tr>
    <td class="tg-9wq8">5</td>
    <td class="tg-9wq8">0.073</td>
    <td class="tg-9wq8">10</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">1360</td>
    <td class="tg-9wq8">137.17</td>
    <td class="tg-9wq8">36.450</td>
    <td class="tg-9wq8">18.22</td>
  </tr>
  <tr>
    <td class="tg-b406">10</td>
    <td class="tg-b406">0.080</td>
    <td class="tg-b406">10</td>
    <td class="tg-b406">0</td>
    <td class="tg-b406">1360</td>
    <td class="tg-b406">124.37</td>
    <td class="tg-b406">80.405</td>
    <td class="tg-b406">16.52</td>
  </tr>
  <tr>
    <td class="tg-xwyw" rowspan="4">2</td>
    <td class="tg-xwyw">1</td>
    <td class="tg-xwyw">1.064</td>
    <td class="tg-xwyw">50</td>
    <td class="tg-xwyw">0</td>
    <td class="tg-xwyw">6800</td>
    <td class="tg-xwyw">46.99</td>
    <td class="tg-xwyw">21.279</td>
    <td class="tg-xwyw">6.24</td>
  </tr>
  <tr>
    <td class="tg-7ca6">10</td>
    <td class="tg-7ca6">1.479</td>
    <td class="tg-7ca6">50</td>
    <td class="tg-7ca6">0</td>
    <td class="tg-7ca6">6800</td>
    <td class="tg-7ca6">33.81</td>
    <td class="tg-7ca6">295.774</td>
    <td class="tg-7ca6">4.49</td>
  </tr>
  <tr>
    <td class="tg-9wq8">30</td>
    <td class="tg-9wq8">7.732</td>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">6800</td>
    <td class="tg-9wq8">6.47</td>
    <td class="tg-9wq8">4639.134</td>
    <td class="tg-9wq8">0.86</td>
  </tr>
  <tr>
    <td class="tg-b406">50</td>
    <td class="tg-b406">29.552</td>
    <td class="tg-b406">50</td>
    <td class="tg-b406">0</td>
    <td class="tg-b406">6800</td>
    <td class="tg-b406">1.69</td>
    <td class="tg-b406">29552.276</td>
    <td class="tg-b406">0.22</td>
  </tr>
  <tr>
    <td class="tg-9wq8" rowspan="4">3</td>
    <td class="tg-9wq8">1</td>
    <td class="tg-9wq8">10.979</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">13600</td>
    <td class="tg-9wq8">9.11</td>
    <td class="tg-9wq8">109.787</td>
    <td class="tg-9wq8">1.21</td>
  </tr>
  <tr>
    <td class="tg-b406">10</td>
    <td class="tg-b406">7.792</td>
    <td class="tg-b406">100</td>
    <td class="tg-b406">0</td>
    <td class="tg-b406">13600</td>
    <td class="tg-b406">12.83</td>
    <td class="tg-b406">779.210</td>
    <td class="tg-b406">1.70</td>
  </tr>
  <tr>
    <td class="tg-9wq8">50</td>
    <td class="tg-9wq8">0.624</td>
    <td class="tg-9wq8">100</td>
    <td class="tg-9wq8">0</td>
    <td class="tg-9wq8">13600</td>
    <td class="tg-9wq8">160.38</td>
    <td class="tg-9wq8">311.761</td>
    <td class="tg-9wq8">21.30</td>
  </tr>
  <tr>
    <td class="tg-7ca6">100</td>
    <td class="tg-7ca6">0.724</td>
    <td class="tg-7ca6">100</td>
    <td class="tg-7ca6">0</td>
    <td class="tg-7ca6">13600</td>
    <td class="tg-7ca6">138.10</td>
    <td class="tg-7ca6">724.138</td>
    <td class="tg-7ca6">18.34</td>
  </tr>
</table>

### Screenshot

- `ab -n 10 -c 1 http://127.0.0.1:10001/`  
![1](screenshot/1_1.png)
- `ab -n 10 -c 5 http://127.0.0.1:10001/`  
![1](screenshot/1_2.png)
- `ab -n 10 -c 10 http://127.0.0.1:10001/`  
![1](screenshot/1_3.png)
- `ab -n 50 -c 1 http://127.0.0.1:10001/`  
![2](screenshot/2_1.png)
- `ab -n 50 -c 10 http://127.0.0.1:10001/`  
![2](screenshot/2_2.png)
- `ab -n 50 -c 30 http://127.0.0.1:10001/`  
![2](screenshot/2_3.png)
- `ab -n 50 -c 50 http://127.0.0.1:10001/`  
![2](screenshot/2_4.png)
- `ab -n 100 -c 1 http://127.0.0.1:10001/`  
![3](screenshot/3_1.png)
- `ab -n 100 -c 10 http://127.0.0.1:10001/`  
![3](screenshot/3_2.png)
- `ab -n 100 -c 50 http://127.0.0.1:10001/`  
![3](screenshot/3_3.png)
- `ab -n 100 -c 100 http://127.0.0.1:10001/`  
![3](screenshot/3_4.png)
