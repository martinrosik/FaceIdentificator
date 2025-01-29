# Face Identifier 🎭📸

This is a simple Face Identifier built using OpenCV and Python. It detects faces, eyes, and smiles from a webcam feed in real-time. 😃👀

## 🚀 Features

- ✅ Detects faces in real-time 👤
- ✅ Identifies left and right eyes separately 👁️👁️
- ✅ Detects smiles 😁
- ✅ Displays bounding boxes with labels for detected features 🖍️

## 🛠️ Technologies Used

- 🐍 Python
- 🎨 OpenCV
- 💡 NumPy

## 📦 Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/martinrosik/FaceIdentificator.git
   cd FaceIdentificator
   ```

2. Install dependencies:

   ```sh
   pip install opencv-python numpy
   ```

## 📜 Usage

Run the script to start the webcam face identifier:

```sh
python main.py
```

Press `q` to quit the program.

## 🔍 How It Works

1. 🎥 Captures video from the webcam.
2. 🏗️ Converts frames to grayscale for better detection.
3. 🏆 Uses Haar cascades to detect:
   - 👤 Faces
   - 👀 Left Eye
   - 👀 Right Eye
   - 😃 Smiles
4. 📏 Draws rectangles around detected features and labels them.
5. 🖼️ Displays the output in a window.

## 🖼️ Example Output

When a face is detected, the bounding boxes are drawn with labels:

- 🔵 Blue box for Face
- 🔴 Red box for Eyes
- 🟢 Green box for Smile

## 🤝 Contributing

Feel free to fork and improve the project. PRs are welcome! 🙌

