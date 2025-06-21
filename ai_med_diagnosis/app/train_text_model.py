# train_text_model.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Sample data (expand as needed)
data = {
    "report": [
        "MRI shows a mass in the frontal lobe",
        "No abnormal findings in chest X-ray",
        "Evidence of pneumonia in the left lung",
        "Tumor detected in cerebellum region",
        "Spinal vertebrae appear normal",
        "Pleural effusion noted in chest scan"
    ],
    "label": ["Tumor", "Normal", "Pneumonia", "Tumor", "Normal", "Pneumonia"]
}

df = pd.DataFrame(data)

# Create pipeline
text_model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train model
text_model.fit(df["report"], df["label"])

# Save model
joblib.dump(text_model, "model/text_classifier.pkl")
