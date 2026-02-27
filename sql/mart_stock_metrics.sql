CREATE TABLE IF NOT EXISTS mart_stock_metrics AS
SELECT
    trade_date,
    ticker,
    AVG(close_price) AS avg_close_price,
    STDDEV(close_price) AS volatility,
    SUM(volume) AS total_volume
FROM raw_stock_data
GROUP BY trade_date, ticker;
