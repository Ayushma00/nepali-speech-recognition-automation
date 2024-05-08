# Nepali Speech Automation for Home Applications

## Overview

This project aims to leverage Nepali speech recognition technology to automate home applications, drawing inspiration from popular platforms like Siri and Alexa. The research work is divided into two main components: speech recognition and predictive text implementation into IoT devices/sensors.

### Speech Recognition

The speech recognition aspect utilizes mathematical techniques such as time domain conversion and Short-time Fourier Transform (STFT) for feature extraction. These extracted features are then fed into hybrid CNN-LSTM neural networks for training. The ultimate goal is to convert Nepali speech into predicted text in English language, enabling seamless interaction with home automation systems. This is present in the `notebook/model_training.ipynb` file

### Predictive Text Implementation

The second part of the project focuses on implementing predictive text functionality into IoT devices/sensors. This is achieved through MQTT (Message Queuing Telemetry Transport) protocols, facilitating bidirectional communications between databases and sensors. By integrating predictive text capabilities, IoT devices become more intuitive and responsive to user inputs, enhancing the overall automation experience. This part is not included here but the general web site implementation for prediotion is shown in the django web app.

## Research Paper
This project is based on the research paper titled "[Nepali Voice-Controlled Home Automation System](https://www.researchgate.net/publication/369107292_Nepali_Voice-Controlled_Home_Automation_System)", which serves as the foundation for our work.


<div align="center">
  <h3>System Architecture</h3>
  <img src="https://github.com/Ayushma00/test_speech/assets/34135400/e18966c5-0946-4eb3-986f-3df8150da535" width="800" />
</div>
<br>
<div  align="center">
    <h3>Model Architecture</h3>
    <img src="https://github.com/Ayushma00/test_speech/assets/34135400/fc4cf4e8-1d4e-42a3-801d-5a48a4ad8c64" width="800" />
</div><br>
<div align="center">
  <h3>Results</h3>
  <img src="https://github.com/Ayushma00/test_speech/assets/34135400/b50f5203-121f-4639-a8ce-c5d2ab69cf70" width="400" />
  <img src="https://github.com/Ayushma00/test_speech/assets/34135400/a7b0f7d9-1536-4277-ab61-bfc9eb9c9a4c" width="400" />
</div>

## Usage

### Speech Recognition Module

To use the speech recognition module:

1. Ensure the necessary dependencies are installed.
2. Train the hybrid CNN-LSTM neural network model using the provided dataset.
3. Run the speech recognition script, providing input in Nepali language.
4. The script will output the predicted text in English language.



