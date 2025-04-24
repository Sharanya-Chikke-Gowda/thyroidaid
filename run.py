from thyroidaid_package.data import load_data
from thyroidaid_package.eda import run_eda
from thyroidaid_package.model import preprocess_features, train_model, evaluate_model, plot_feature_importance

df = load_data('/content/thyroid_cancer_risk_data.csv')
run_eda(df)

(X_train, X_test, y_train, y_test), X_full = preprocess_features(df)
model = train_model(X_train, y_train)
evaluate_model(model, X_test, y_test)
plot_feature_importance(model, X_full)
