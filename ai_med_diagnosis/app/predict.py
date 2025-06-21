import numpy as np
from PIL import Image
import tensorflow as tf
import os

MODEL_PATH = "ai_med_diagnosis\\app\\model\\brain_mri_resnet50.h5"
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image_file):
    image = Image.open(image_file).convert('RGB')
    image = image.resize((224, 224))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def predict_image(image_file, body_part="brain"):
    image = preprocess_image(image_file)
    prediction = model.predict(image)[0][0]
    if prediction > 0.5:
        return {"prediction": "Tumor", "confidence": round(float(prediction), 2)}
    else:
        return {"prediction": "Normal", "confidence": round(1 - float(prediction), 2)}
