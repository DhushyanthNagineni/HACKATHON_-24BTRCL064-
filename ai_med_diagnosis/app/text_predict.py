import joblib

text_model = joblib.load("ai_med_diagnosis\\app\\model\\text_classifier.pkl")

def predict_text(report_text):
    if not report_text.strip():
        return {"text_prediction": "Unknown", "confidence": 0.0}
    prediction = text_model.predict([report_text])[0]
    probas = text_model.predict_proba([report_text])[0]
    confidence = max(probas)
    return {
        "text_prediction": prediction,
        "confidence": round(float(confidence), 2)
    }