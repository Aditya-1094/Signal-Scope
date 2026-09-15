import os
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms, models


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "train"
MODEL_DIR = BASE_DIR / "model"

MODEL_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# Device
# ============================================================

if torch.cuda.is_available():
    device = torch.device("cuda")
elif torch.backends.mps.is_available():
    device = torch.device("mps")
else:
    device = torch.device("cpu")

print("Using device:", device)


# ============================================================
# Transform
# IMPORTANT:
# This matches the preprocessing used for your trained model.
# ============================================================

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])


# ============================================================
# Dataset
# ============================================================

dataset = datasets.ImageFolder(
    DATA_DIR,
    transform=transform
)

print("Classes:", dataset.class_to_idx)
print("Total images:", len(dataset))


# ============================================================
# Train / Validation Split
# 80% Train
# 20% Validation
# ============================================================

train_size = int(0.8 * len(dataset))
val_size = len(dataset) - train_size

train_dataset, val_dataset = random_split(
    dataset,
    [train_size, val_size],
    generator=torch.Generator().manual_seed(42)
)

print("Training samples:", len(train_dataset))
print("Validation samples:", len(val_dataset))


# ============================================================
# DataLoaders
# ============================================================

if device.type == "cuda":
    num_workers = min(4, os.cpu_count() or 1)
    pin_memory = True
else:
    num_workers = 0
    pin_memory = False


train_loader = DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True,
    num_workers=num_workers,
    pin_memory=pin_memory
)

val_loader = DataLoader(
    val_dataset,
    batch_size=64,
    shuffle=False,
    num_workers=num_workers,
    pin_memory=pin_memory
)


# ============================================================
# Model - EfficientNet-B0
# ============================================================

weights = models.EfficientNet_B0_Weights.DEFAULT

model = models.efficientnet_b0(weights=weights)

num_features = model.classifier[1].in_features

model.classifier[1] = nn.Linear(
    num_features,
    2
)

model = model.to(device)


# ============================================================
# Loss & Optimizer
# ============================================================

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=1e-4
)


# ============================================================
# Training
# ============================================================

epochs = 3

for epoch in range(epochs):

    # ----------------------------
    # Training
    # ----------------------------

    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:

        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item() * images.size(0)

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_loss = running_loss / total
    train_acc = correct / total


    # ----------------------------
    # Validation
    # ----------------------------

    model.eval()

    val_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():

        for images, labels in val_loader:

            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)

            loss = criterion(outputs, labels)

            val_loss += loss.item() * images.size(0)

            _, predicted = torch.max(outputs, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    val_loss = val_loss / total
    val_acc = correct / total


    print(
        f"Epoch [{epoch + 1}/{epochs}] "
        f"Train Loss: {train_loss:.4f} "
        f"Train Acc: {train_acc:.4f} "
        f"Val Loss: {val_loss:.4f} "
        f"Val Acc: {val_acc:.4f}"
    )


# ============================================================
# Save Model
# ============================================================

model_path = MODEL_DIR / "efficientnet_b0.pth"

torch.save(
    model.state_dict(),
    model_path
)

print("\nModel saved to:")
print(model_path)