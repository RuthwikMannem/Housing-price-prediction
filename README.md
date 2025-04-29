# Housing-price-prediction
# Overview
This repository contains a House Price Prediction project using Machine Learning and Exploratory Data Analysis (EDA).
The goal of the project is to predict the price of houses using regression models.

We all have experienced a time when we had to look for a new house to buy. But the journey begins with a lot of frauds, negotiating deals, researching local areas, and so on.

To solve these issues, this project builds a Machine Learning-based model trained on a House Price Prediction Dataset.

# Data
The dataset used in this project is from Kaggle.

## Dataset contains:
Id - Count of records

MSSubClass - Identifies the type of dwelling involved in the sale

MSZoning - General zoning classification of the sale

LotArea - Lot size in square feet

LotConfig - Configuration of the lot

BldgType - Type of dwelling

OverallCond - Rates the overall condition of the house

YearBuilt - Original construction year

YearRemodAdd - Remodel year (same as construction year if no remodeling)

Exterior1st - Exterior covering on the house

BsmtFinSF2 - Type 2 finished square feet

TotalBsmtSF - Total square feet of basement area

SalePrice - Target variable (house price to be predicted)

# Exploratory Data Analysis
EDA is performed in the notebook named EDA.ipynb.

This includes:

Loading and understanding the dataset

Handling missing values

Summary statistics of all features

Data visualizations using Matplotlib and Seaborn

Correlation matrix and heatmap

Feature distributions

Relationships with the target variable SalePrice

# House Price Prediction
Model training is performed in the notebook House Price Prediction & EDA.ipynb

## It includes:
Loading the data and understanding the structure

Feature selection using correlation and feature importance

Data preprocessing:

Handling missing data

Encoding categorical variables

Treating outliers

Model building:

Linear Regression

Support Vector Regression (SVR)

Random Forest Regression

Model evaluation using:

Mean Absolute Error (MAE)

Model tuning using:

Hyperparameter tuning

