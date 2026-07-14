# train_naive_bayes.py

import os
import pandas as pd
import joblib

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ===============================
# 1. File Paths
# ===============================

TRAIN_DATA_PATH = "dataset/train_processed.csv"
TEST_DATA_PATH = "dataset/test_processed.csv"
MODEL_FOLDER = "model"

MODEL_PATH = os.path.join(MODEL_FOLDER, "naive_bayes_model.pkl")
SYMPTOM_COLUMNS_PATH = os.path.join(MODEL_FOLDER, "symptom_columns.pkl")


# ===============================
# 2. Create model folder if missing
# ===============================

if not os.path.exists(MODEL_FOLDER):
    os.makedirs(MODEL_FOLDER)


# ===============================
# 3. Load Dataset
# ===============================

print("Loading datasets...")

train_data = pd.read_csv(TRAIN_DATA_PATH)
test_data = pd.read_csv(TEST_DATA_PATH)

print("Training data shape:", train_data.shape)
print("Testing data shape:", test_data.shape)


# ===============================
# 4. Separate Features and Target
# ===============================

TARGET_COLUMN = "Disease"

X_train = train_data.drop(TARGET_COLUMN, axis=1)
y_train = train_data[TARGET_COLUMN]

X_test = test_data.drop(TARGET_COLUMN, axis=1)
y_test = test_data[TARGET_COLUMN]

symptom_columns = list(X_train.columns)


# ===============================
# 5. Train Naive Bayes Model
# ===============================

print("\nTraining Naive Bayes model...")

nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)

print("Model training completed.")


# ===============================
# 6. Test Model
# ===============================

print("\nTesting model...")

y_pred = nb_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nNaive Bayes Model Accuracy:")
print(f"{accuracy * 100:.2f}%")


# ===============================
# 7. Classification Report
# ===============================

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ===============================
# 8. Confusion Matrix
# ===============================

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ===============================
# 9. Save Model and Symptom Columns
# ===============================

joblib.dump(nb_model, MODEL_PATH)
joblib.dump(symptom_columns, SYMPTOM_COLUMNS_PATH)

print("\nModel saved successfully.")
print("Saved model path:", MODEL_PATH)
print("Saved symptom columns path:", SYMPTOM_COLUMNS_PATH)


# ===============================
# 10. Test Single Sample Prediction
# ===============================

sample = X_test.iloc[0:1]
actual_disease = y_test.iloc[0]

predicted_disease = nb_model.predict(sample)[0]
prediction_probability = nb_model.predict_proba(sample)[0]
confidence_score = max(prediction_probability) * 100

print("\nSample Prediction Test:")
print("Actual Disease:", actual_disease)
print("Predicted Disease:", predicted_disease)
print(f"Confidence Score: {confidence_score:.2f}%")