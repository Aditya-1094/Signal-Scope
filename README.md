# 🔍 Signal-Scope

### Telling Real From Synthetic in the Age of Generative Media

Signal-Scope is an AI-powered image classification system that predicts whether an uploaded image is **likely real or likely AI-generated**.

The project uses **EfficientNet-B0 with transfer learning** to classify images into two categories:

- 🤖 AI-generated
- 📷 Real

> **Note:** Signal-Scope provides a model-estimated likelihood and should not be treated as definitive proof of an image's origin.

> **⚠️ Alert:** Please use Python 3.11, 3.12, or any other Python version which is compatible with PyTorch.

---

## 🚀 Features

- Real vs AI-generated image classification
- Confidence score for predictions
- EfficientNet-B0 transfer learning
- Streamlit web interface
- Command-line prediction support
- Held-out test evaluation
- ROC-AUC and Macro-F1 evaluation
- Supports JPG, JPEG, PNG and WEBP images
- Responsible-AI wording using "Likely AI-generated" instead of absolute claims

---

## 🧠 Model

Signal-Scope uses **EfficientNet-B0**, a pretrained convolutional neural network, with transfer learning.

### Model Configuration

| Parameter | Value |
|---|---|
| Model | EfficientNet-B0 |
| Pretrained Weights | ImageNet |
| Input Size | 224 × 224 |
| Classes | 2 |
| Loss Function | CrossEntropyLoss |
| Optimizer | Adam |
| Learning Rate | 0.0001 |
| Batch Size | 64 |
| Epochs | 3 |
| Threshold | 0.50 |
| Data Augmentation | None |
| Calibration | None |

The original EfficientNet-B0 classifier was replaced with a two-class classification layer.

```text
Input Image
     ↓
Resize 224 × 224
     ↓
EfficientNet-B0
     ↓
Feature Extraction
     ↓
Classification Layer
     ↓
 ┌───────────────┐
 │               │
AI-generated    Real
