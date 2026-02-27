# DWH Prototype – COVID-19 Analytics

## 1. Источник данных

Источник: Our World in Data  
Ссылка: https://ourworldindata.org/covid-data  
CSV: https://covid.ourworldindata.org/data/owid-covid-data.csv  

Почему выбран:

- Бесплатный открытый источник
- Полная историческая статистика
- Подходит для построения витрин и BI

Основные поля:

- location (text)
- date (date)
- total_cases (numeric)
- new_cases (numeric)
- total_deaths (numeric)
- new_deaths (numeric)
- total_vaccinations (numeric)
- population (numeric)

---

## 2. Архитектура

API → Airflow → PostgreSQL (raw schema) → DWH → BI

---

## 3. Запуск проекта

1. docker-compose up -d
2. Airflow: http://localhost:8080
3. PostgreSQL: localhost:5432

## 4. Витрина данных (Data Mart)

### Выбранные метрики

1. Средняя цена закрытия (avg_close_price)
   Позволяет анализировать среднюю стоимость акции за период.

2. Дневная волатильность (volatility)
   Показывает уровень колебаний цены.

3. Объем торгов (total_volume)
   Позволяет оценить активность рынка.

### Структура витрины

Таблица: mart_stock_metrics

- trade_date
- ticker
- avg_close_price
- volatility
- total_volume

## Дашборд

BI-система: Yandex DataLens

Ссылка на опубликованный дашборд:
https://datalens.yandex/your_dashboard_link

Скриншоты находятся в папке /screenshots
