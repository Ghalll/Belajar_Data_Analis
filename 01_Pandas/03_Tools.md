# Tools DA

Chapter ini akan menjelaskan tools-tools penting dalam Data Analyst

## 📊 Statistik Dasar

1. **Nilai rata-rata**
    = ini digunakan untuk mencari nilai rata-rata.
    ```bash
    df["penjualan_mingguan"].mean()
    ```

2. **Nilai tengah**
   = ini digunakan untuk mencari nilai tengah.
   ```bash
   df["penjualan_mingguan"].median()
   ```

3. **Nilai MAX**
   = ini digunakan untuk mencari nilai paling besar.
   ```bash
   df["penjualan_mingguan"].max()
   ```

4. **Nilai MIN**
   = ini digunakan untuk mencati nilai paling kecil.
   ```bash
   df["penjualan_mingguan"].min()
   ```

5. **Nilai Standar**
   = ini digunakan untuk mencari nilai yang tersebar dari rata-rata
   ```bash
   df["penjualan_mingguan"].std()
   ```

6. **Posisi Data (Persentil)**
   = ini digunakan untuk mencati nilai
   ```bash
   df["penjualan_mingguan"].quantile(0.75)
   ``` 
   
   
