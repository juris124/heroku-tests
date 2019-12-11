# Oktobra mājasdarbs

---

## Mērķis

Pārnest programmu uz Heroku

+++

## Rezultāti

- Izveidojām Heroku kontu
- Savienojām Heroku kontu ar GitHub
- Pārnesām iepriekšējo projektu
- Pievienojām jaunu funkcionalitāti

---?color=linear-gradient(90deg, white 50%, black 50%)

@snap[west span-30 text-center]

## Brīvais Suns

@img[](static/bildes/brivais_suns.png)

@snapend

@snap[east span-50 text-center]

@img[](static/bildes/brivais_suns.png)

@snapend

---

@snap[north-east]
#### Piemērs Heroku kodam
@snapend

```python
if __name__ == '__main__':
    app.run(threaded=True, port=5000)
    # Komentārs
    # Cits komentārs
```

@snap[south span-100 text-14]
@[1](Ja funkcija izsaukta kā __main__)
@[2](Palaiž aplikāciju)
@[3-4](Komentāri piemēram)
@snapend

Note:

- Šo nevajadzētu redzēt prezentācijā
- **Bold** un *italic*

+++?code=Procfile&lang=python

@snap[north-east]
#### Piemērs kodam no faila
@snapend

---
