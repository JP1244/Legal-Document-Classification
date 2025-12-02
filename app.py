from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import pdfplumber
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)



MODEL_PATH = os.path.join(os.path.dirname(__file__), "legalbert_scotus_model")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_PATH,
    local_files_only=True
)


label_names = [
    "Criminal Procedure",
    "Civil Rights",
    "First Amendment",
    "Due Process",
    "Privacy",
    "Attorneys",
    "Unions",
    "Economic Activity",
    "Judicial Power",
    "Federalism",
    "Interstate Relations",
    "Federal Taxation",
    "Miscellaneous"
]

print("\n Legal-BERT Model Loaded Successfully!\n")


def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                content = page.extract_text()
                if content:
                    text += "\n" + content
    except Exception as e:
        print("PDF extraction error:", e)
        return None

    return text.strip()


def predict_legal_category(text):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    with torch.no_grad():
        outputs = model(**inputs)

    pred_idx = torch.argmax(outputs.logits, dim=1).item()
    return label_names[pred_idx]

@app.route('/')
def home():
    return render_template("upload.html")   

import zipfile
import tempfile

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filename = secure_filename(file.filename)
    file_ext = filename.lower().split(".")[-1]

    if file_ext == "pdf":

        pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(pdf_path)

        text = extract_text_from_pdf(pdf_path)
        if not text:
            return jsonify({"error": "Could not extract text from PDF"}), 400

        category = predict_legal_category(text)

        return jsonify({
            "mode": "single",
            "filename": filename,
            "category": category
        })

    elif file_ext == "zip":
        temp_dir = tempfile.mkdtemp()

        zip_path = os.path.join(temp_dir, filename)
        file.save(zip_path)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)

        results = {}

        for root, dirs, files in os.walk(temp_dir):
            for f in files:
                if f.lower().endswith(".pdf"):
                    pdf_file_path = os.path.join(root, f)
                    text = extract_text_from_pdf(pdf_file_path)

                    if text:
                        category = predict_legal_category(text)
                    else:
                        category = "Unable to extract text"

                    results[f] = category

        return jsonify({
            "mode": "bulk",
            "count": len(results),
            "results": results
        })

    else:
        return jsonify({"error": "Only PDF or ZIP files allowed"}), 400

if __name__ == '__main__':
    app.run(debug=True)
