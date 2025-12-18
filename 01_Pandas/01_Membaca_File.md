# Pandas

Library Pandas digunakan untuk membaca file, bisa file dengan beberapa macam ekstensi.

Contoh code untuk mengimport lilbrary pandas

```bash
import pandas as pd
```

# Fungsi Read Data

1. `read_csv`
  
   Digunakan untuk membaca file dengan ekstensi **csv**
  
    Contoh code :
  
   ```bash
   data = pd.read_csv('namafile.csv')
   ```

2. `read_excel`
  
   Digunakan untuk membaca file dengan ekstensi **xlsl**
  
   Contoh code :
  
   ```bash
   data = pd.read_excel('namafile.xlsl')
   ```
   
3. `read_pickle`
  
    Digunakan untuk membaca file dengan ekstensi **pkl**
  
    Contoh code :
  
    ```bash
    data = pd.read_pickle('namafile.pkl')
    ```

# Inspeksi Data

1. **Menampilkan 5 baris data teratas**

   ```bash
   import pandas as pd
    
   load_data = pd.read_csv('data/titanic.csv')
       
   print(load_data.head())
   ```

3. **Menampilkan 5 baris data terbawah**

   ```bash
   import pandas as pd
    
   load_data = pd.read_csv('data/titanic.csv')
       
   print(load_data.tail())
   ```

4. **Menampilkan ringkasan struktur data**

   ```bash
   import pandas as pd
    
   load_data = pd.read_csv('data/titanic.csv')
       
   print(load_data.info())
   ```

5. **Menampilkan Statistik ringkas data numerik**

   ```bash
   import pandas as pd
    
   load_data = pd.read_csv('data/titanic.csv')
       
   print(load_data.describe())
   ```


6. **Menampilkan ukuran baris dan kolom data**

   ```bash
   import pandas as pd
   
   load_data = pd.read_csv('data/titanic.csv')
       
   print(load_data.shape)
   ```

# Atribut Dasar

1. **Mengambil semua data dalam bentuk array 2D**
  
    ```bash
    import pandas as pd
     
    load_data = pd.read_csv('data/titanic.csv')
         
    print(load_data.values)
    ```

2. **Menampilkan daftar nama kolom**

    ```bash
    import pandas as pd
     
    load_data = pd.read_csv('data/titanic.csv')
         
    print(load_data.columns) 
    ```

3. **Menampilkan daftar index (label baris)**

    ```bash
    import pandas as pd
     
    load_data = pd.read_csv('data/titanic.csv')
         
    print(load_data.index)   
    ```

# Manipulasi Data

1. **Mengurutkan data**

   ```bash
   homelessness_ind = homelessness.sort_values("individuals")
   ```
   
3. **Ambil data pakai label + kondisi**

   ```bash
   df.loc[df['Age'] > 18, ['Name', 'Age']]
   ```
   
5. **Cek keanggotaan**

   ```bash
   south_mid_atlantic = homelessness[homelessness["region"].isin(["South Atlantic", "Mid-Atlantic"])]
   ```
