
Description

This project utilizes Convolutional Neural Networks (CNNs) to detect traffic signs from video feeds or images and provides voice alerts when a traffic sign is detected. The system is designed for real-time applications, making it suitable for driver assistance systems.

Features

Real-time traffic sign detection using a pre-trained CNN model.
Voice alerts corresponding to detected traffic signs.
User-friendly interface for easy setup and execution.

Requirements
Software,
Python 3.x,
OpenCV,
TensorFlow/Keras,
Scikit-learn,


Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/traffic-sign-detection.git
cd traffic-sign-detection
Install Required Packages: Create a virtual environment (optional but recommended)
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Download Pre-trained Model: Download the pre-trained CNN model and place it in the model/ directory. (Link to the model should be provided in the repository or documentation).

Troubleshooting

Camera Not Found: Ensure your camera is properly connected and recognized by your system.
Model Not Found Error: Check if the pre-trained model is correctly placed in the model/ directory.
Import Errors: Ensure all required libraries are installed as specified in requirements.txt.
