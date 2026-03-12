# Electricity Cost Prediction

## Project Overview
This project predicts electricity cost for buildings using machine learning.

The project demonstrates a complete machine learning pipeline including:
- Exploratory Data Analysis
- Model Training
- FastAPI backend for predictions
- Streamlit frontend for user interaction
  
## DATASET FEATURES
The model uses the following features:
- site_area
- water_consumption
- resident_count
- utilisation_rate
- structure_type
  
## MODEL
Random Forest Regressor was used to train the prediction model.

Random Forest is an ensemble learning algorithm that combines multiple
decision trees to improve prediction accuracy and reduce overfitting.

## MODEL PERFORMANCE
R2 Score: 0.95
MAE: 180
RMSE: 227

## PROJECT ARCHITECTURE
Dataset
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Saved Model (.pkl)
   ↓
FastAPI Backend
   ↓
Streamlit Frontend


