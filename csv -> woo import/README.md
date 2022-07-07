# csv -> woo import

## 1. Command format:

```
python3 main.py [module] [module, parameters, ...]
```

### 1.1 Modules:

**1. Iam:** `python3 main.py iam [input.csv] [data_folder]`\
data_folder\
    ├── orig\
    │       ├── 15 ml\
    │       ├── 7 ml\
    │       └──...\
    └── out\
**2. Other:** `python3 main.py other [input.csv] [out_folder]`
out_folder, is jut folder where renamed photos are stored

**input.csv**
Header must contains:

```
naziv,kratkiO,opis,proizvajalec,orgLink,kategorije,kategorije2,cena,skrij,slike,navodila,opozorila,sestavine,odgOseba,certifikati,video,barva,volumen
```
