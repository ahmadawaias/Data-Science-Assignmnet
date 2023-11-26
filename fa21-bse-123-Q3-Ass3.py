# Import necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import make_scorer, f1_score
import numpy as np
import pandas as pd

# Specify the path to your CSV file
file_path = "gender-prediction.csv"
# Replace with the actual path to your CSV file

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Assume your dataset is in a Pandas DataFrame called df

# Map categorical variables to numerical values
df["beard"] = df["beard"].map({"yes": 1, "no": 0})
df["hair_length"] = df["hair_length"].map(
    {"short": 0, "bald": 1, "medium": 2, "long": 3}
)
df["scarf"] = df["scarf"].map({"no": 0, "yes": 1})
df["eye_color"] = (
    df["eye_color"].astype("category").cat.codes
)  # Convert categorical eye color to numerical
df["gender"] = df["gender"].map({"male": 0, "female": 1})  # Convert gender to numerical

# Split the data into features (X) and target variable (y)
X = df.drop("gender", axis=1)
y = df["gender"]

# Define the Random Forest classifier
rf_classifier = RandomForestClassifier(     )

# Define the F1 scorer for cross-validation
f1_scorer = make_scorer(
    f1_score, average="binary"
)  # Use binary average for two classes

# Monte Carlo Cross-Validation
monte_carlo_f1_scores = cross_val_score(rf_classifier, X, y, cv=5, scoring=f1_scorer)

# Leave P-Out Cross-Validation
p_out = 15  # You can choose any value for P
leave_p_out = KFold(n_splits=len(X) - p_out)
p_out_f1_scores = cross_val_score(
    rf_classifier, X, y, cv=leave_p_out, scoring=f1_scorer
)

print("Monte Carlo Cross-Validation F1 Scores:", monte_carlo_f1_scores)

print("Leave P-Out Cross-Validation F1 Scores:", p_out_f1_scores)

