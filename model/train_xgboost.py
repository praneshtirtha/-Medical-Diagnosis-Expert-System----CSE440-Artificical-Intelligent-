# train_xgboost.py

import os
import pandas as pd
import joblib

from xgboost import XGBClassifier

from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# ===============================
# 1. File Paths
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

TRAIN_DATA_PATH = os.path.join(PROJECT_DIR, "dataset", "train_processed.csv")
TEST_DATA_PATH = os.path.join(PROJECT_DIR, "dataset", "test_processed.csv")

MODEL_FOLDER = os.path.join(PROJECT_DIR, "model")
MODEL_PATH = os.path.join(MODEL_FOLDER, "xgboost_model.pkl")
LABEL_ENCODER_PATH = os.path.join(MODEL_FOLDER, "label_encoder.pkl")
SYMPTOM_COLUMNS_PATH = os.path.join(MODEL_FOLDER, "symptom_columns.pkl")

print("Train Path :", TRAIN_DATA_PATH)
print("Test Path  :", TEST_DATA_PATH)
print("Train Exists:", os.path.exists(TRAIN_DATA_PATH))
print("Test Exists :", os.path.exists(TEST_DATA_PATH))

# ===============================
# 2. Create Model Folder
# ===============================

os.makedirs(MODEL_FOLDER, exist_ok=True)

# ===============================
# 3. Load Dataset
# ===============================

print("\nLoading datasets...")

train_data = pd.read_csv(TRAIN_DATA_PATH)
test_data = pd.read_csv(TEST_DATA_PATH)

print("Training data shape:", train_data.shape)
print("Testing data shape :", test_data.shape)

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
# 5. Encode Disease Labels
# ===============================

label_encoder = LabelEncoder()

y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# ===============================
# 6. Train XGBoost Model
# ===============================

print("\nTraining XGBoost model...")

xgb_model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.1,
    objective="multi:softmax",
    eval_metric="mlogloss",
    random_state=42
)

xgb_model.fit(X_train, y_train_encoded)

print("Model training completed.")

# ===============================
# 7. Test Model
# ===============================

print("\nTesting model...")

y_pred_encoded = xgb_model.predict(X_test)

accuracy = accuracy_score(y_test_encoded, y_pred_encoded)

print("\nXGBoost Accuracy:")
print(f"{accuracy * 100:.2f}%")

# Convert predictions back to disease names
y_pred = label_encoder.inverse_transform(y_pred_encoded)

# ===============================
# 8. Classification Report
# ===============================

print("\nClassification Report:\n")

print(classification_report(y_test, y_pred))

# ===============================
# 9. Confusion Matrix
# ===============================

print("\nConfusion Matrix:\n")

print(confusion_matrix(y_test, y_pred))

# ===============================
# 10. Save Model
# ===============================

joblib.dump(xgb_model, MODEL_PATH)
joblib.dump(label_encoder, LABEL_ENCODER_PATH)
joblib.dump(symptom_columns, SYMPTOM_COLUMNS_PATH)

print("\nModel saved successfully.")
print("Model Path:", MODEL_PATH)
print("Label Encoder Path:", LABEL_ENCODER_PATH)
print("Symptom Columns Path:", SYMPTOM_COLUMNS_PATH)

# ===============================
# 11. Single Sample Prediction
# ===============================

sample = X_test.iloc[[0]]

actual_disease = y_test.iloc[0]

predicted_encoded = xgb_model.predict(sample)[0]

predicted_disease = label_encoder.inverse_transform([predicted_encoded])[0]

if hasattr(xgb_model, "predict_proba"):
    probability = xgb_model.predict_proba(sample)[0]
    confidence = max(probability) * 100
else:
    confidence = None

print("\n========== Sample Prediction ==========")
print("Actual Disease   :", actual_disease)
print("Predicted Disease:", predicted_disease)

if confidence is not None:
    print(f"Confidence Score : {confidence:.2f}%")