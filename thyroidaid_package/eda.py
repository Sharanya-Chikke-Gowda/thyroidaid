import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def run_eda(df):
    factor = [
        'Age', 'Gender', 'Country', 'Ethnicity', 'Family_History',
        'Radiation_Exposure', 'Iodine_Deficiency', 'Smoking',
        'Obesity', 'Diabetes', 'TSH_Level', 'T3_Level', 'T4_Level',
        'Nodule_Size'
    ]

    for col in factor:
        plt.figure(figsize=(10, 6))
        try:
            if col == 'Nodule_Size':
                df['Nodule_Size'] = pd.to_numeric(df['Nodule_Size'], errors='coerce')
                sns.histplot(df['Nodule_Size'][df['Nodule_Size'] < 3.0], kde=True)
            elif df[col].dtype == 'object':
                sns.countplot(data=df, x=col)
            else:
                sns.histplot(df[col], kde=True)
            plt.title(f'Distribution of {col}')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Could not plot column {col}: {e}")

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Diagnosis')
    plt.title('Diagnosis Distribution')
    plt.tight_layout()
    plt.show()
