# Kaggle Downloads

Команды для скачивания данных в проекты. Перед использованием нужно настроить Kaggle API: создать `kaggle.json` в профиле Kaggle и положить его в `~/.kaggle/`.

## Olist Marketplace Product Analytics

```bash
cd olist-marketplace-product-analytics
kaggle datasets download -d olistbr/brazilian-ecommerce
unzip brazilian-ecommerce.zip -d data/raw
```

## Fraud Detection & Risk Scoring

```bash
cd fraud-detection-risk-scoring
kaggle datasets download -d mlg-ulb/creditcardfraud
unzip creditcardfraud.zip -d data/raw
```

## Store Sales Forecasting ETL Pipeline

```bash
cd store-sales-forecasting-etl
kaggle competitions download -c store-sales-time-series-forecasting
unzip store-sales-time-series-forecasting.zip -d data/raw
```

## Telco Retention Experiment Design

```bash
cd telco-retention-experiment-design
kaggle datasets download -d blastchar/telco-customer-churn
unzip telco-customer-churn.zip -d data/raw
```

## MovieLens Recommendation API

```bash
cd movielens-recommendation-api
kaggle datasets download -d grouplens/movielens-20m-dataset
unzip movielens-20m-dataset.zip -d data/raw
```

## Customer Lifetime Value & RFM Segmentation

```bash
cd customer-lifetime-value-segmentation
kaggle datasets download -d hellbuoy/online-retail-customer-clustering
unzip online-retail-customer-clustering.zip -d data/raw
```
