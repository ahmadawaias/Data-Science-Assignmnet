import pandas as pd

# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

# Specify the path to your CSV file
file_path = "gender-prediction.csv" 


# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Map categorical variables to numerical values
df["beard"] = df["beard"].map({"yes": 1, "no": 0})
# labels = preprocessing.LabelEncoder()
# b_encoded = labels.fit_transform(df["beard"])
# print(df["beard"])

df["hair_length"] = df["hair_length"].map(
    {"short": 0, "bald": 1, "medium": 2, "long": 3}
)

# h_encoded = labels.fit_transform(df["hair_length"])
# print(h_encoded)
df["scarf"] = df["scarf"].map({"no": 0, "yes": 1})

# s_encoded = labels.fit_transform(df["scarf"])
# print(s_encoded)
df["eye_color"] = df["eye_color"].astype("category").cat.codes

# e_encoded = labels.fit_transform(df["eye_color"])
# print(df["eye_color"])
# Convert categorical eye color to numerical

# Split the data into features (X) and target variable (y)
X = df.drop("gender", axis=1)
y = df["gender"]

# Split the data into training and testing sets (2/3 train, 1/3 test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.22, random_state=42
)

# Model 1: Logistic Regression
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)

# Model 2: Support Vector Machines
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)

# Model 3: Multilayer Perceptron
mlp_model = MLPClassifier()
mlp_model.fit(X_train, y_train)
mlp_predictions = mlp_model.predict(X_test)

# Calculate accuracy
lr_accuracy = accuracy_score(y_test, lr_predictions)
svm_accuracy = accuracy_score(y_test, svm_predictions)
mlp_accuracy = accuracy_score(y_test, mlp_predictions)

# Print accuracies
# print(f"Logistic Regression Accuracy: {lr_accuracy}")
# print(f"Support Vector Machines Accuracy: {svm_accuracy}")
# print(f"Multilayer Perceptron Accuracy: {mlp_accuracy}")
print("\n\t...................ACCURACY,.....................\n ")
print("Logistic Regression Accuracy:", lr_accuracy)
print("Support Vector Machines Accuracy:", svm_accuracy)
print("Multilayer Perceptron Accuracy: ", mlp_accuracy)

# Calculate the number of instances incorrectly classified
print(
    "\n\t...................NUMBER OF INSTANCES INCORRECTLY CLASSIFIED.....................\n "
)
lr_incorrect = (lr_predictions != y_test).sum()
svm_incorrect = (svm_predictions != y_test).sum()
mlp_incorrect = (mlp_predictions != y_test).sum()

print(f"Logistic Regression Incorrectly Classified Instances: {lr_incorrect}")
print(f"Support Vector Machines Incorrectly Classified Instances: {svm_incorrect}")
print(f"Multilayer Perceptron Incorrectly Classified Instances: {mlp_incorrect}")
