# Chess Board Keypoint Detection (Synthetic)

This project focuses on detecting the four corner keypoints of a chessboard in synthetic images. The model is trained using PyTorch and a custom dataset generated from randomly placed board images on various background textures.

## 📌 Project Goal

The goal is to predict the exact pixel locations (as normalized coordinates) of the four chessboard corners using a convolutional neural network (CNN).

## 🧠 Approach

- A custom CNN architecture is used to regress 8 keypoint coordinates: (x1, y1, ..., x4, y4)
- Input images are synthetic: chessboards composited on random backgrounds
- Model is trained using `MSELoss` for precise keypoint localization

## 🗃️ Dataset

- Synthetic dataset generated using OpenCV
- Each image is 480x480 and contains one board
- Corresponding labels include normalized (x, y) coordinates for all 4 corners

## 🚀 Training Details

- Optimizer: Adam
- Loss: MSELoss
- Trained on my own laptop with RTX 3050 6GB Laptop GPU with optional multiprocessing data loading

## 🔧 Requirements

- Python 3.11.7
- PyTorch
- torchvision
- OpenCV
- pandas
- python-dotenv

