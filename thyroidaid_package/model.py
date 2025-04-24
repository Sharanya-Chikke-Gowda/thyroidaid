import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

def preprocess_features(df):
    features = [
        'Age', 'Gender', 'Country', 'Ethnicity', 'Family_History',
        'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking',
        'Obesity', 'Diabetes', 'TSH_Level', 'T3_Level', 'T4_Level',
        'Nodule_Size'
    ]
    X = pd.get_dummies(df[features], drop_first=True)
    y = df['Diagnosis']
    return train_test_split(X, y, test_size=0.2, random_state=42), X

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print('Classification Report:\n', classification_report(y_test, y_pred))
    print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))
    print('Accuracy Score:', accuracy_score(y_test, y_pred))

def plot_feature_importance(model, X):
    feat_imp = pd.Series(model.feature_importances_, index=X.columns)
    top10 = feat_imp.sort_values(ascending=False).head(10)
    plt.figure(figsize=(6, 4))
    top10.plot(kind='barh')
    plt.title('Top 10 Feature Importances')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()
