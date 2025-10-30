# Legal-Document-Classification

This project implements an **AI-powered Legal Document Classification System** using transformer-based models like **Legal-BERT**.  
It automatically classifies legal texts such as court judgments, case reports, and statutes into relevant issue areas (e.g., Civil Rights, Criminal Law, Tax Law).  
The model is trained using the **LexGLUE – SCOTUS** dataset and fine-tuned to understand complex legal language.

## Introduction

The legal sector produces enormous amounts of unstructured data daily — court rulings, case summaries, contracts, and legal filings.  
Manual classification of these documents is slow and error-prone.  

With the rise of **Natural Language Processing (NLP)** and transformer architectures like **BERT**, we can now understand legal language contextually.  
This project fine-tunes **Legal-BERT**, a BERT model pre-trained on legal corpora, to classify legal documents efficiently using the **SCOTUS dataset**.

---

## Abstract

This project aims to automate the classification of legal texts using **Legal-BERT**, a domain-adapted variant of BERT specialized for legal language.  
The model is trained on the **LexGLUE SCOTUS** dataset, which contains Supreme Court opinions categorized by issue area.

By fine-tuning Legal-BERT, we enable automated document tagging and organization, reducing human effort while improving accuracy and accessibility in legal research.

---

##  Why Choose This Project

| Aspect | Description |
|:-------|:-------------|
| **Practical Importance** | Helps legal professionals automate classification of vast document sets |
| **Emerging Domain** | Integrates Artificial Intelligence with Legal Studies |
| **Technical Challenge** | Handles long, domain-specific, and complex legal documents |
| **Advanced Model** | Uses Legal-BERT for contextual understanding of legal text |
| **Social Impact** | Improves access to justice and efficiency in legal document retrieval |

---

##  Technologies and Tools Used

| Category | Tool / Library | Purpose |
|:----------|:---------------|:--------|
| Programming Language | **Python** | Core implementation language |
| NLP Framework | **Hugging Face Transformers** | For Legal-BERT fine-tuning and model handling |
| Dataset Handling | **Hugging Face Datasets (load_dataset)** | For LexGLUE / SCOTUS dataset management |
| Model Training | **Trainer, TrainingArguments** | Simplifies model training and evaluation |
| Deep Learning Backend | **PyTorch (torch)** | Provides GPU-accelerated deep learning support |
| Evaluation Metrics | **Scikit-learn (accuracy, F1, precision, recall)** | Model performance evaluation |
| Numerical Computation | **NumPy** | Supports efficient data manipulation |
| Development Environment | **Google Colab / Jupyter Notebook** | For training and visualization |

---

##  Dataset Access

Due to GitHub’s file size limitations, the **LexGLUE – SCOTUS dataset** is not directly uploaded here.  
You can access it in two ways — via Hugging Face or Google Drive.

---

###  Option 1 — Load Dataset Directly from Hugging Face

#### Install required library
!pip install datasets -q

#### Import and load the SCOTUS dataset (LexGLUE subset)
from datasets import load_dataset

##### Load the dataset
dataset = load_dataset("coastalcph/lex_glue", "scotus")

#### View structure
print(dataset)
print(dataset["train"][0])

---

### Option 2 — Load Dataset Directly from Google Drive

Because the dataset is large (>100 MB), it’s stored externally.

- [Download SCOTUS Dataset (Google Drive)][(https://drive.google.com/file/d/1P6bZN6vRhghBxUlC_dkdGyzkmTG5uxZd/view?usp=sharing)]

--- 

## License

This project is intended for academic and research purposes only.
The datasets are governed by their respective licenses under LexGLUE and Hugging Face.

---

## Contributors

Jeet Patel (22000388)

Ravalji Maitryba (22000410)

Department of Computer Science and Engineering,
School of Engineering and Technology,
Academic Year 2025–26.
