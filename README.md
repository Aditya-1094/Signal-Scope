# 🔍 Signal-Scope
### Telling Real From Synthetic in the Age of Generative Media

Signal-Scope is a computer vision system that analyzes an image and estimates whether it is **likely real or AI-generated**.

The project uses transfer learning with **EfficientNet-B0** and provides a simple Streamlit interface where users can upload an image and receive a predicted label along with the model's confidence.

> ⚠️ The prediction is a model-estimated likelihood, not definitive proof of an image's origin.

---

## 🎯 Problem

Generative AI models can now create highly realistic images that are difficult to distinguish from photographs.

Signal-Scope addresses the problem of detecting synthetic imagery by building a binary image classifier:

**Input Image → Preprocessing → EfficientNet-B0 → Classification → Confidence → Responsible Verdict**

The system focuses on general real-vs-synthetic image detection and does not attempt to identify or profile real individuals.

---

## 🚀 Features

- 🖼️ Upload JPG, JPEG, PNG, or WEBP images
- 🤖 Real vs AI-generated image classification
- 📊 Confidence score
- ⚡ Simple Streamlit web interface
- 🧠 Transfer learning using EfficientNet-B0
- 📈 ROC-AUC and Macro-F1 evaluation
- 📋 Classification report
- 🔍 Responsible likelihood-based output
- 💻 Command-line prediction interface
- 📓 Jupyter notebook containing model development and evaluation

---

## 🧩 Implemented Modules

### Core Module — Real vs AI Classification

The mandatory core task is implemented.

The model accepts a single image and outputs:

- `AI-generated`
- `Real`
- Confidence score

The project also includes a trained model, an honest train/validation/test split, evaluation metrics, and a usable interface.

### Deployment / Real-Time Interface

A Streamlit application provides a drag-and-drop interface for testing new images.

### Bonus Modules

The current implementation does **not** claim full implementation of:

- Generator attribution
- C2PA / Content Credentials
- Multimodal image-text consistency
- Adversarial robustness analysis
- Faithful Grad-CAM explanations
- Calibrated confidence

These can be added as future improvements.

---

# 🏗️ Architecture

```text
                Input Image
                     │
                     ▼
             Image Preprocessing
               Resize → 224×224
                     │
                     ▼
          EfficientNet-B0 Backbone
             Pretrained on ImageNet
                     │
                     ▼
             Classification Layer
                  2 Classes
                     │
                     ▼
              Softmax Probability
                     │
              ┌──────┴──────┐
              ▼             ▼
          AI-generated      Real
              │             │
              └──────┬──────┘
                     ▼
              Confidence Score
                     │
                     ▼
             Responsible UI
## 🎯 Problem

Generative AI models can now create highly realistic images that are difficult to distinguish from photographs.

Signal-Scope addresses the problem of detecting synthetic imagery by building a binary image classifier:

**Input Image → Preprocessing → EfficientNet-B0 → Classification → Confidence → Responsible Verdict**

The system focuses on general real-vs-synthetic image detection and does not attempt to identify or profile real individuals.

---

## 🚀 Features

- 🖼️ Upload JPG, JPEG, PNG, or WEBP images
- 🤖 Real vs AI-generated image classification
- 📊 Confidence score
- ⚡ Simple Streamlit web interface
- 🧠 Transfer learning using EfficientNet-B0
- 📈 ROC-AUC and Macro-F1 evaluation
- 📋 Classification report
- 🔍 Responsible likelihood-based output
- 💻 Command-line prediction interface
- 📓 Jupyter notebook containing model development and evaluation

---

## 🧩 Implemented Modules

### Core Module — Real vs AI Classification

The mandatory core task is implemented.

The model accepts a single image and outputs:

- `AI-generated`
- `Real`
- Confidence score

The project also includes a trained model, an honest train/validation/test split, evaluation metrics, and a usable interface.

### Deployment / Real-Time Interface

A Streamlit application provides a drag-and-drop interface for testing new images.

### Bonus Modules

The current implementation does **not** claim full implementation of:

- Generator attribution
- C2PA / Content Credentials
- Multimodal image-text consistency
- Adversarial robustness analysis
- Faithful Grad-CAM explanations
- Calibrated confidence

These can be added as future improvements.

---

# 🏗️ Architecture

```text
                Input Image
                     │
                     ▼
             Image Preprocessing
               Resize → 224×224
                     │
                     ▼
          EfficientNet-B0 Backbone
             Pretrained on ImageNet
                     │
                     ▼
             Classification Layer
                  2 Classes
                     │
                     ▼
              Softmax Probability
                     │
              ┌──────┴──────┐
              ▼             ▼
          AI-generated      Real
              │             │
              └──────┬──────┘
                     ▼
              Confidence Score
                     │
                     ▼
             Responsible UI