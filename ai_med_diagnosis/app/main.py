from flask import Flask, render_template, request
from predict import predict_image
from text_predict import predict_text
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../uploads'

@app.route("/", methods=["GET", "POST"])
def index():
    prediction_result = None

    if request.method == "POST":
        image_file = request.files.get("image")
        report_text = request.form.get("report")
        body_part = request.form.get("body_part")

        result = {}

        if image_file:
            result.update(predict_image(image_file, body_part))

        if report_text:
            result.update(predict_text(report_text))

        prediction_result = result

    return render_template("index.html", result=prediction_result)

if __name__ == "__main__":
    os.makedirs('../uploads', exist_ok=True)
    app.run(debug=True)
