# Airbnb Price Prediction

Ovaj projekt izrađen je u sklopu kolegija **Računarstvo usluga i analiza podataka**.  
Cilj projekta je izraditi **model za predikciju cijene Airbnb smještaja** i omogućiti korisniku jednostavno web sučelje za unos podataka i dobivanje procjene cijene.

---
Značajke korištene za predikciju:
- grad
- tip smještaja
- broj osoba i soba
- je li domaćin superhost
- ocjene čistoće i zadovoljstva gostiju
- radi li se o vikendu ili radnom danu

Cilj je bio izgraditi **regresijski model** koji na temelju navedenih značajki može predvidjeti cijenu smještaja.

---

## Podaci

Podaci su preuzeti s platforme **Kaggle**:

🔗 https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities

Podaci obuhvaćaju više europskih gradova i razdvojeni su na weekday / weekend. Zbog lakšeg stvaranja modela svi dataseti su spojeni u jednu tablicu (`airbnb_merged.csv`) te su dodana dodatna polja za grad i tip dana

---

## Model strojnog učenja

- Model je treniran nad obrađenim podacima
- Korišten je one-hot encoding za kategorijske varijable (grad, tip sobe)
- Model predviđa **realnu cijenu smještaja**
---

## Web aplikacija

Projekt uključuje web aplikaciju izrađenu pomoću **Flaska**.

### Backend
- Flask REST API
- Endpoint `/predict` prima JSON podatke
- Podaci se pretvaraju u Pandas DataFrame
- Model vraća predikciju cijene

### Frontend
- HTML / CSS / JavaScript


## Pokretanje projekta lokalno

```bash
git clone https://github.com/anajerkovic/AirBnB-PricePrediction.git
cd AirBnB-PricePrediction
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python backend.py

