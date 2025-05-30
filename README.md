# ThyroidAid

**ThyroidAid** is a Python package designed for exploratory analysis and prediction of thyroid health risks based on clinical and lifestyle indicators.

## Abstract
ThyroidAid presents a machine learning-based system designed for the exploratory analysis and prediction of thyroid health risks. By analyzing clinical and lifestyle indicators, the project aims to support early diagnosis and risk stratification of thyroid disorders.

## Introduction
Thyroid disorders affect a significant portion of the global population, often remaining undiagnosed due to subtle or nonspecific symptoms. Predicting thyroid risk factors using machine learning models offers the potential to improve early diagnosis, optimize treatments, and better manage public health resources. This project applies a Random Forest classifier to predict thyroid disease risks based on multiple demographic and clinical features.

## Methodology
1. Data Preprocessing: Cleaning and handling missing values using pandas.
2. Exploratory Data Analysis (EDA): Visualization of feature distributions using seaborn and matplotlib.
3. Modeling: A Random Forest Classifier is trained to predict thyroid risk.
4. Evaluation: Model performance is assessed based on accuracy scores and feature importances.

## Features
- Clean and preprocess thyroid risk datasets
- Generate insightful EDA visualizations
- Train and evaluate classification models using Random Forest
- Plot top predictors contributing to thyroid diagnosis

## Installation
```bash
pip install .
```

## Usage
```python
from thyroidaid_package.data import load_data
from thyroidaid_package.eda import run_eda
from thyroidaid_package.model import preprocess_features, train_model, evaluate_model, plot_feature_importance

# Load data
df = load_data('your_dataset.csv')
run_eda(df)

# Train and evaluate model
(X_train, X_test, y_train, y_test), X = preprocess_features(df)
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)
plot_feature_importance(model, X)
```

## Results

**Feature Distributions**

Figure 1: Nodule Size Distribution
[Image/Distribution of Nodule_Size.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20Nodule_Size.png)

Figure 2: T4 Level Distribution
[Image/Distribution of T4_Level.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20T4_Level.png)

Figure 3: T3 Level Distribution
[Image/Distribution of T3_Level.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20T3_Level.png)

Figure 4: TSH Level Distribution
[Image/Distribution of TSH_Level.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20TSH_Level.png)

Figure 5: Diabetes Distribution
[Image/Distribution of Diabetes.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20Diabetes.png)

Figure 6: Obesity Distribution
[Image/Distribution of Obesity.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20Obesity.png)

Figure 7: Smoking Distribution
[Image/Distribution of Smoking.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Distribution%20of%20Smoking.png)

**Model Evaluation**

Figure 8: Diagnosis Distribution
[Image/Diagnosis Distribution.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Diagnosis%20Distribution.png)

Figure 9: Top 10 Feature Importances
[Image/Top 10 Feature Importances.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Top%2010%20Feature%20Importances.png)

Figure 10: Classification Model Report and Accuracy
[Image/Classification Model (Random Forest) Accuracy.png](https://raw.githubusercontent.com/Sharanya-Chikke-Gowda/thyroidaid/refs/heads/main/Image/Classification%20Model%20(Random%20Forest)%20Accuracy.png)

## Conclusion
This project demonstrates that thyroid disease risk can be effectively predicted using machine learning techniques, particularly Random Forest classifiers. The analysis highlights key features such as TSH levels, family history, and nodule size as major predictors. Future work may include refining the model through hyperparameter tuning and integrating other advanced machine learning models.

## Requirements
- pandas
- seaborn
- matplotlib
- scikit-learn

## License
MIT License
