# DWH Prototype COVID-19 Analytics

## 1. Выбранный источник данных

### Название
Our World in Data – COVID-19 Dataset

### Ссылка
https://ourworldindata.org/coronavirus

Прямая ссылка на CSV:
https://covid.ourworldindata.org/data/owid-covid-data.csv

### Формат
CSV, ежедневное обновление

---

## 2. Описание структуры данных

### Таблица 1 — Данные по заболеваемости

Поля:

- iso_code (TEXT)
- continent (TEXT)
- location (TEXT)
- date (DATE)
- total_cases (NUMERIC)
- new_cases (NUMERIC)
- total_deaths (NUMERIC)
- new_deaths (NUMERIC)
- total_cases_per_million (NUMERIC)
- total_deaths_per_million (NUMERIC)

---

### Таблица 2 — Данные по вакцинации

Поля:

- iso_code (TEXT)
- location (TEXT)
- date (DATE)
- total_vaccinations (NUMERIC)
- people_vaccinated (NUMERIC)
- people_fully_vaccinated (NUMERIC)
- new_vaccinations (NUMERIC)
- total_vaccinations_per_hundred (NUMERIC)

---

## 3. Обоснование выбора источника

- Открытый бесплатный доступ
- Регулярное обновление данных
- Исторические данные с 2020 года
- Подходит для построения DWH и витрин
- Удобен для демонстрации ETL-процесса
