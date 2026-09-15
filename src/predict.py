from pathlib import Path

import torch
import torch.nn as nn
from PIL import Image
from torchvision import transforms, models


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "efficientnet_b0.pth"


# ============================================================
# Device
# ============================================================

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")


# ============================================================
# Model
# ============================================================

model = models.efficientnet_b0(weights=None)

num_features = model.classifier[1].in_features

model.classifier[1] = nn.Linear(
    num_features,
    2
)

model.load_state_dict(
    torch.load(
        MODEL_PATH,
        map_location=device
    )
)

model = model.to(device)

model.eval()


# ============================================================
# Image preprocessing
# IMPORTANT:
# Must match the preprocessing used during training.
# ============================================================

transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


# ============================================================
# Prediction Function
# ============================================================

def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    image = image.to(device)


    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        predicted_class = torch.argmax(
            probabilities,
            dim=1
        ).item()


    confidence = probabilities[0][predicted_class].item()


    # ImageFolder mapping:
    # FAKE = 0
    # REAL = 1

    if predicted_class == 0:
        label = "AI-generated"
    else:
        label = "Real"


    return label, confidence


# ============================================================
# Test
# ============================================================

if __name__ == "__main__":

    image_path = input("Enter image path: ")

    label, confidence = predict_image(image_path)

    print("\nPrediction:", label)
    print("Confidence:", f"{confidence * 100:.2f}%")