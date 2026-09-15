# 🔍 Signal-Scope

### Telling Real From Synthetic in the Age of Generative Media

Signal-Scope is an AI-powered image classification system that predicts whether an uploaded image is **likely real or likely AI-generated**.

The project uses **EfficientNet-B0 with transfer learning** to classify images into two categories:

- 🤖 AI-generated
- 📷 Real

> **🛑 CRITICAL LIMITATION:** **This model ONLY works on 32x32 resolution images.** Passing images of different resolutions or aspect ratios will result in errors or severely degraded, inaccurate predictions.

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
| Input Size | **32 × 32** |
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
Resize 32 × 32
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
<<<<<<< HEAD
```
=======

## 📜 License

### Source Code

The original source code of Signal-Scope is licensed under the
**MIT License**.

See the [LICENSE](LICENSE) file for the complete license text.
>>>>>>> 1369cd3 (Readme updated)

The MIT License applies to the **original source code created for this project**.

<<<<<<< HEAD
## 📊 Dataset

This project uses the **CIFAKE: Real and AI-Generated Synthetic Images** dataset. It contains 100,000 labelled images for training (50,000 FAKE + 50,000 REAL). 

* **Dataset Name:** CIFAKE: Real and AI-Generated Synthetic Images
* **Kaggle Link:** [Click here to view the dataset on Kaggle](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images)
=======
### Dataset

The MIT License **does not apply to the dataset**.
>>>>>>> 1369cd3 (Readme updated)

The dataset was obtained from an external source and remains subject to
its original license, terms of use, and attribution requirements.

<<<<<<< HEAD
## 📜 License

### Source Code

The original source code of Signal-Scope is licensed under the
**MIT License**.

See the [LICENSE](LICENSE) file for the complete license text.

The MIT License applies to the **original source code created for this project**.

### Dataset

The MIT License **does not apply to the dataset**.

The dataset was obtained from an external source and remains subject to
its original license, terms of use, and attribution requirements.

### Pretrained Model

The project uses pretrained EfficientNet-B0 weights provided through
the PyTorch/Torchvision ecosystem. These pretrained weights remain
subject to their respective licenses and terms.

### Third-Party Libraries

Third-party libraries used by this project remain subject to their
respective licenses.
=======
### Pretrained Model

The project uses pretrained EfficientNet-B0 weights provided through
the PyTorch/Torchvision ecosystem. These pretrained weights remain
subject to their respective licenses and terms.

### Third-Party Libraries

Third-party libraries used by this project remain subject to their
respective licenses.
>>>>>>> 1369cd3 (Readme updated)
