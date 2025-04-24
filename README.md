# ThyroidAid

**ThyroidAid** is a Python package designed for exploratory analysis and prediction of thyroid health risks based on clinical and lifestyle indicators.

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

## Requirements
- pandas
- seaborn
- matplotlib
- scikit-learn

## License
MIT License
