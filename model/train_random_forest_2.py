# train_random_forest_v2.py

import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

# ===============================
# 1. File Paths
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

TRAIN_DATA_PATH = os.path.join(PROJECT_DIR, "dataset", "train_processed.csv")
TEST_DATA_PATH = os.path.join(PROJECT_DIR, "dataset", "test_processed.csv")

MODEL_FOLDER = os.path.join(PROJECT_DIR, "model")
OUTPUT_FOLDER = os.path.join(PROJECT_DIR, "outputs")

MODEL_PATH = os.path.join(MODEL_FOLDER, "random_forest_model.pkl")
SYMPTOM_COLUMNS_PATH = os.path.join(MODEL_FOLDER, "symptom_columns.pkl")
CONFUSION_MATRIX_PATH = os.path.join(
    OUTPUT_FOLDER,
    "random_forest_confusion_matrix.png"
)

print("Train Path :", TRAIN_DATA_PATH)
print("Test Path  :", TEST_DATA_PATH)
print("Train Exists:", os.path.exists(TRAIN_DATA_PATH))
print("Test Exists :", os.path.exists(TEST_DATA_PATH))

# ===============================
# 2. Create Folders
# ===============================

os.makedirs(MODEL_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

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
# 5. Train Model
# ===============================

print("\nTraining Random Forest model...")

rf_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

print("Model training completed.")

# ===============================
# 6. Test Model
# ===============================

print("\nTesting model...")

y_pred = rf_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)

print(f"Accuracy : {accuracy:.4f}")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ===============================
# 7. Confusion Matrix
# ===============================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:\n")
print(cm)

plt.figure(figsize=(12, 10))
plt.imshow(cm)
plt.title("Random Forest Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()
plt.tight_layout()

plt.savefig(CONFUSION_MATRIX_PATH)
plt.close()

print("\nConfusion Matrix saved.")
print(CONFUSION_MATRIX_PATH)

# ===============================
# 8. Save Model
# ===============================

joblib.dump(rf_model, MODEL_PATH)
joblib.dump(symptom_columns, SYMPTOM_COLUMNS_PATH)

print("\nModel saved successfully.")
print("Model Path:", MODEL_PATH)
print("Symptom Columns Path:", SYMPTOM_COLUMNS_PATH)

# ===============================
# 9. Single Sample Prediction
# ===============================

sample = X_test.iloc[[0]]
actual_disease = y_test.iloc[0]

predicted_disease = rf_model.predict(sample)[0]

if hasattr(rf_model, "predict_proba"):
    probability = rf_model.predict_proba(sample)[0]
    confidence = max(probability) * 100
else:
    confidence = None

print("\n========== Sample Prediction ==========")
print("Actual Disease   :", actual_disease)
print("Predicted Disease:", predicted_disease)

if confidence is not None:
    print(f"Confidence Score : {confidence:.2f}%")