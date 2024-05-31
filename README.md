# Image to CSV Converter for CNN

This project provides a graphical user interface (GUI) for converting a batch of images into a CSV file. Each image is represented as a flattened array of pixel values, making it suitable for training a Convolutional Neural Network (CNN).

## Features

- Select a folder containing images to process.
- Specify the destination for the resulting CSV file.
- Convert images to grayscale and flatten them into a single row of pixel values.
- Simple and user-friendly GUI built with `tkinter`.

## Requirements

- Python 3.x
- Pillow
- Pandas
- NumPy

## Installation

1. Clone the repository:
   
   git clone https://github.com/yourusername/image-to-csv-converter.git
   cd image-to-csv-converter 

2. Install the required libraries:
 
   pip install pillow pandas numpy


Usage
Run the script:
python image_to_csv_for_cnn_gui.py

Use the GUI to:
Select the folder containing your images.
Specify the name and location for the CSV file.
Click the "Start" button to process the images and create the CSV file.

Example
The resulting CSV file will have each row representing an image, with pixel values flattened into a single row.

Author
Made by Rishabh Kushawah

   

