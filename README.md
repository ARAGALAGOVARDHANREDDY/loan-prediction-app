# 🏦 Loan Approval Prediction System

A machine learning-based web application that predicts whether a loan application is likely to be approved based on applicant and financial information.

The project compares multiple machine learning classification algorithms and selects **LightGBM** as the best-performing model based on the evaluation results.

🚀 **Live Demo:**  
https://loan-prediction-app-apg4dln7fdto45kare37gg.streamlit.app/

💻 **Source Code:**  
https://github.com/ARAGALAGOVARDHANREDDY/loan-prediction-app

---

## 📌 Project Overview

Loan approval prediction is a classification problem where machine learning can be used to analyze applicant information and predict the likelihood of loan approval.

In this project, multiple machine learning models were trained and evaluated using the Kaggle Loan Prediction Dataset.

The evaluated models include:

- LightGBM
- XGBoost
- Random Forest
- Decision Tree
- AdaBoost
- Gaussian Naive Bayes
- Support Vector Machine (SVM)
- Logistic Regression
- K-Nearest Neighbors (KNN)

After comparing the models using Accuracy, Precision, Recall, and F1 Score, **LightGBM achieved the highest accuracy of 97.84%** among the evaluated models.

The selected model was then integrated into a Streamlit web application and deployed online.

---

## 🚀 Live Demo

Try the deployed application:

👉 https://loan-prediction-app-apg4dln7fdto45kare37gg.streamlit.app/

Users can enter applicant information and receive a real-time loan approval prediction.

---

## ✨ Features

- 🤖 Machine learning-based loan approval prediction
- 📊 Comparison of multiple classification algorithms
- 🏆 LightGBM selected as the best-performing model
- 📝 Interactive applicant information form
- ⚡ Real-time prediction using Streamlit
- 🔄 Data preprocessing and feature encoding
- 📈 Model evaluation using multiple performance metrics
- 🌐 Deployed as a live web application
- 📱 Simple and user-friendly interface

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Science & Machine Learning

- Pandas
- NumPy
- Scikit-learn
- LightGBM
- XGBoost

### Model Persistence

- Joblib
- Pickle

### Web Application

- Streamlit

### Development Environment

- Jupyter Notebook

### Deployment

- Streamlit Community Cloud

---

## 📊 Dataset

The project uses the **Loan Prediction Dataset from Kaggle**.

The dataset contains information about loan applicants and their financial and personal details.

Key features used in the prediction process include:

- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Term
- Credit History
- Education
- Self Employment Status
- Property Area
- Other applicant-related attributes

The data was preprocessed before training the machine learning models.

---

## 🔄 Machine Learning Workflow

The project follows the following machine learning workflow:

```text
Kaggle Loan Prediction Dataset
            ↓
Data Loading
            ↓
Data Cleaning
            ↓
Exploratory Data Analysis
            ↓
Feature Preprocessing
            ↓
Categorical Feature Encoding
            ↓
Feature Scaling
            ↓
Train-Test Split
            ↓
Model Training
            ↓
Multiple Model Comparison
            ↓
Model Evaluation
            ↓
Best Model Selection
            ↓
LightGBM Model
            ↓
Model Saving
            ↓
Streamlit Application
            ↓
Online Deployment
