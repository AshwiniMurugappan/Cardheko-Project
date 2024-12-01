# Cardheko-Project

## Introduction:

**Problem Statement:**

The goal is to enhance the customer experience and streamline the pricing process by leveraging machine learning.
Objective:
To develop a machine learning model to create an accurate and user-friendly streamlit tool that can predict used car prices based on various features
Project Scope:
The model should be integrated into a Streamlit-based web application to allow users to input car details and receive an estimated price instantly.

## Data Cleaning and Preprocessing:

**Dataset:**

There were 6 City’s Dataset which was converted into structured format.
Concatenated all the dataset and made a single Dataset.
The Shape of the Dataset was (8369, 77)
We must Handle missing values (imputation or removal), Duplicate rows and columns.
Normalization or standardization of numerical features
Encoding categorical features (one-hot encoding, label encoding, ordinal encoding) 
Feature engineering (creating new features like price in lakhs)

## Exploratory Data Analysis (EDA):

EDA is the initial investigation of data to discover patterns, it helps to understand the data's characteristics, identify potential issues, and guide feature engineering and modeling choices.

**Data Understanding:** Gain insights into your data's distribution, patterns, and trends.

**Feature Engineering Guidance:** Inform decisions about which features to include or transform.

**Model Selection:** Choose appropriate algorithms based on data characteristics.

**Insights:**

1. Identify relationships between features and price
2. Discover patterns and trends
3. Understand the distribution of numerical features

## Data Preprocessing – Encoding :

To effectively prepare the data for model training, the following encoding techniques were used:

**One-Hot Encoding:**
Used for the "Car Brand" column, which consists of categorical data with no inherent order. Each unique brand was converted into a binary feature, creating a new column for each brand.
**Ordinal Encoding:**
Applied to the "Engine Displacement" column, which represents a categorical variable with a natural order. Each unique displacement value was assigned a numerical value based on its rank. 
**Label Encoding:**
Utilized for other categorical columns that did not require one-hot encoding or ordinal encoding. Each unique category was assigned a numerical label, simplifying the data for the model.

## Model Training and Testing:

**Model Selection:** 
Experimented with various regression algorithms (Linear Regression, Decision Tree Regression, Random Forest Regression, etc.) to identify the best-performing model.

**Model Training:** 
Trained the selected model on the prepared dataset, optimizing parameters to improve accuracy.

**Baseline Model:**
Linear Regression
Lasso and Ridge

**Advanced Models:**
Decision Tree Regression
Random Forest Regression


## Model Evaluation

Assessed the model's performance using metrics like 

1. Mean Squared Error (MSE)
2. Root Mean Square Error (RMSE)
3. Mean Absolute Error (MAE)
4. R-squared Score.

**Model Comparison:**
Compared the performance of different models to select the best-performing one.

## Model Deployment in Streamlit

**Web App Development:** 
Built a user-friendly web application using Streamlit to deploy the model.

**User Interface:** 
Designed an intuitive interface for users to input car details (e.g., make, model, year, mileage, fuel type).

**Model Integration:** 
Integrated the trained model into the Streamlit app to make real-time predictions.

## Conclusion:

**Data Quality and Preprocessing:** The importance of clean and well-prepared data for accurate model predictions.

**Feature Engineering:** The impact of feature engineering techniques

**Model Selection and Training:** Experience with various machine learning algorithms.

**Model Evaluation:** The importance of using appropriate evaluation metrics to assess model accuracy and reliability.

CONSIDERING ALL THE PERFORMANCE METRICS FOR TRAIN AND TEST DATA WE CHOOSE TO USE THE **RANDOM FOREST REGRESSION MODEL**. 

**Model Deployment:** Skills in using tools like Streamlit to create user-friendly web applications

