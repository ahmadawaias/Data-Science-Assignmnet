import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the dataset
file_path = "gender-prediction3.csv"
df = pd.read_csv(file_path)

# Encode categorical variables
label_encoder = LabelEncoder()
categorical_cols = ["beard", "hair_length", "scarf", "eye_color"]
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

# Split the dataset
X = df.iloc[:, :-1]  # Features
y = df.iloc[:, -1]  # Target variable

# Train-test split, using all instances except the last 10 for training
X_train, X_test, y_train, y_test = train_test_split(
    X.iloc[:-10, :], y.iloc[:-10], test_size=10, random_state=42
)

# Create Gaussian Naïve Bayes model
model = GaussianNB()

# Train the model
model.fit(X_train, y_train)

# Test the model on the last 10 instances
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, pos_label="male")
recall = recall_score(y_test, y_pred, pos_label="male")

# Report the scores
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
