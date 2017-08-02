Escuelas Argentinas
===================

Información sobre más de 62.000 Establecimientos educativos en Argentina
del sitio http://escuelasarg.com/


Para correr el scraper


```
$ pip3 install -r requirements
$ scrapy crawl escuelas -t csv -o escuelas_argentinas.csv
```

Para separar por provincia usé pandas

```python

In [1]: import pandas as pd

In [2]: escuelas = pd.read_csv('escuelas_argentina.csv')

In [3]: provs = set(escuelas.jurisdiccion.values)

In [4]: from django.utils.text import slugify

In [5]: for prov in provs:
    ...:     prov = escuelas[escuelas.jurisdiccion == prov]
    ...:     slug = slugify(prov)
    ...:     prov.to_csv(f'{slug}.csv')
```



