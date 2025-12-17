# Dictionary

Adalah struktur data yang memiliki 2 unsur yaitu : **keys** dan **values**, yang mana setiap key digunakan untuk mengakses valuenya.

contoh dalam program :

```bash
europe = {
    'spain' : 'madrid',
    'france' : 'paris',
    'germany' : 'berlin',
    'norway' : 'oslo'
}
```

`spain` = adalah key.

`madrid` = adalah value.


# Fungsi Dasar Dictionary

- `print(europe.keys())` = untuk mengakses keys di data dictionary **europe**

    output = `dict_keys(['spain', 'france', 'germany', 'norway'])`

- `print(europe.values())` = untuk mengakses values di data dictionary **europe**

    output = `dict_values(['madrid', 'paris', 'berlin', 'oslo'])`

- `print(europe['norway'])` = untuk mengakses value dari key **norway** pada data **europe**

    output = `oslo`

- `europe.update({'italy':'rome'})` = untuk menambahkan **italy** ke dalam data **europe**

- `europe['spain'] = 'barca'` = untuk update value dari key **spain**

- `del(europe['france'])` = untuk hapus **france** dari data **europe**


# Lainya

1. **Sub-Dictionary**

   Adalah membuat dictionary di dalam dictionary yang sudah ada.

   Fungsi untuk buat ngatur data yang bertingkat dan saling berhubungan. Itu saja intinya.

   Contoh : User → nama, email, role

   ```bash
   # Dictionaty dalam dictionary
   country = { 'Indonesia' : {'Ibu kota':'Jakarta', 'Populasi':'200 juta'},
               'Malaysia' : {'Ibu kota': 'Putra Jaya', 'Populasi':'36 juta'}
               'Thailand' : {'Ibu kota': 'Bangkok', 'Populasi':'71 juta'}
             }

   # Membuat sub dictionary
   data = {'Ibu kota':'Hanoi', 'Populasi':'102 juta'}

   # Menambahkan vietnam ke dalam dictionary
   country.update({'Vietnam':data})
   ```

3. 
