# Global Flight Fare Prediction: Data Preprocessing & Integration

A collaborative machine learning project investigating global flight fare prediction using crude oil prices, airline financial indicators, fuel surcharges, route disruptions and geopolitical events.

## Project Overview

Flight fares are influenced by multiple interacting factors, including route characteristics, passenger demand, fuel prices and geopolitical disruptions. This project integrates multiple aviation and energy-market datasets to prepare a unified dataset for machine learning-based flight fare prediction.

**My primary contribution: Data preprocessing and integration.**

I worked on preparing heterogeneous datasets for downstream modelling, with an emphasis on data quality, multi-source integration, temporal alignment, feature transformation and data integrity.

## Technical Stack

- **Language:** Python
- **Data manipulation:** pandas, NumPy
- **Exploratory data analysis:** Matplotlib, Seaborn
- **Machine learning:** scikit-learn, XGBoost
- **Environment:** Jupyter Notebook

## Data Sources

The project uses six datasets from the [Kaggle Airline Ticket Prices vs Oil and Fuel Costs dataset](https://www.kaggle.com/datasets/zkskhurram/airline-ticket-prices-vs-oil-and-fuel-costs):

1. Airline ticket prices
2. Airline financial impact
3. Oil and jet fuel prices
4. Fuel surcharges
5. Route cost impact
6. Conflict and oil events

The ticket-price dataset served as the base table, with `fare_total_usd` as the prediction target.

## My Contribution: Data Preprocessing

### 1. Data Quality Assessment and Cleaning

- Inspected dataset dimensions, column structures, descriptive statistics and missing-value patterns.
- Investigated missing data and distinguished structural missingness from values requiring imputation.
- Checked for duplicate records and corrected inconsistent airline naming across datasets.
- Used box plots and the interquartile range (IQR) rule to investigate outliers, retaining observations judged to represent legitimate extreme values rather than automatically removing them.

### 2. Multi-Source Data Integration

- Integrated six datasets through five sequential left-join operations.
- Selected appropriate join keys based on temporal and entity-level relationships.
- Aggregated surcharge records to airline-month level and route-cost records to airline-month level before merging, reducing the risk of unintended row multiplication.
- Aligned quarterly airline financial indicators with monthly observations using linear interpolation for selected continuous variables and forward-filling for selected stock or policy variables.
- Reviewed missing values introduced or exposed during integration.

### 3. Data Transformation and Feature Preparation

- Converted temporal variables into pandas datetime representations.
- Converted binary disruption indicators into numerical values.
- Applied ordinal encoding to ordered categories and one-hot encoding to nominal categorical variables.
- Extracted temporal components and applied cyclical encoding to represent month-of-year patterns.

### 4. Data Reduction and Integrity

- Removed redundant columns and duplicate tracking information.
- Identified target-derived variables that could cause data leakage and removed them from the predictor set.
- Reduced redundancy among correlated energy-market variables and identifiers.
- Reviewed records with missing airline financial context before determining which observations could be retained.

## Project Workflow

1. Inspect and clean the six source datasets.
2. Aggregate and integrate datasets with different levels of granularity.
3. Transform categorical and temporal variables.
4. Remove redundant or potentially leakage-prone features.
5. Prepare the consolidated dataset for machine learning.
6. Evaluate regression models and investigate feature selection and hyperparameter optimisation as part of the wider group project.

## Group Project Results

The group evaluated Linear Regression, Random Forest and XGBoost before comparing feature-selection strategies and tuning the XGBoost model.

The group report recorded the following results for the final tuned XGBoost model using Recursive Feature Elimination (RFE):

| Metric | Reported result |
|---|---:|
| RMSE | 186.38 |
| MAE | 86.93 |
| R² | 0.9843 |
| Selected features | 22 |

These are **group-level modelling results**, not results attributable solely to my preprocessing contribution.

## Repository Structure

```text
global-flight-fare-prediction/
├── README.md
├── notebooks/
│   └── data_preprocessing.ipynb
├── src/
│   └── preprocessing/
├── docs/
│   └── preprocessing_pipeline.png
├── reports/
├── requirements.txt
└── .gitignore
```

## Reproducibility

The notebook uses Python data analysis libraries to inspect, clean, integrate and transform the source datasets.

To reproduce the workflow:
1. Install the dependencies listed in `requirements.txt`.
2. Obtain the source data from the linked Kaggle dataset.
3. Run the preprocessing notebook sequentially.
4. Verify the resulting dataset dimensions and data-quality checks.

## Limitations and Future Improvements

- Validate the integrated dataset against the original source tables and document the treatment of missing observations.
- Explore a time-based train-test split to better reflect future airfare prediction.
- Package the preprocessing workflow into reusable Python functions.
- Add automated data-quality checks and a data dictionary.
- Investigate whether alternative temporal alignment methods improve the reliability of interpolated financial features.

## Acknowledgements

This was a collaborative group project completed for the Machine Learning for Data Science module at the University of Malaya. The modelling results and project outcomes reflect the work of the group.
