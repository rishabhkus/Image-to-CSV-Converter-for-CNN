import os
from PIL import Image
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

def convert_images_to_csv(image_folder, csv_file):
    data = []
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            filepath = os.path.join(image_folder, filename)
            try:
                with Image.open(filepath) as img:
                    img = img.convert('L')  # Convert to grayscale
                    img_array = np.array(img).flatten()  # Flatten the image
                    data.append(img_array)
            except Exception as e:
                print(f"Error processing file {filename}: {e}")

    df = pd.DataFrame(data)
    df.to_csv(csv_file, index=False)

def select_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)

def select_file():
    file_selected = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    file_path.set(file_selected)

def start_processing():
    directory = folder_path.get()
    csv_filename = file_path.get()
    if directory and csv_filename:
        convert_images_to_csv(directory, csv_filename)
        messagebox.showinfo("Success", f"CSV file '{csv_filename}' created successfully.")
    else:
        messagebox.showwarning("Input Error", "Please select both the image folder and the CSV file destination.")

root = tk.Tk()
root.title("Image to CSV Converter for CNN")

# Style configurations
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), padding=10)
style.configure("TButton", font=("Arial", 12), padding=10)

folder_path = tk.StringVar()
file_path = tk.StringVar()

# Adding a frame for better layout management
frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Select Image Folder:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
ttk.Entry(frame, textvariable=folder_path, width=50).grid(row=0, column=1, padx=10, pady=10)
ttk.Button(frame, text="Browse", command=select_folder).grid(row=0, column=2, padx=10, pady=10)

ttk.Label(frame, text="Select Destination CSV File:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
ttk.Entry(frame, textvariable=file_path, width=50).grid(row=1, column=1, padx=10, pady=10)
ttk.Button(frame, text="Browse", command=select_file).grid(row=1, column=2, padx=10, pady=10)

ttk.Button(frame, text="Start", command=start_processing).grid(row=2, column=1, padx=10, pady=20)

# Adding a footer label
footer_label = ttk.Label(root, text="Made by Rishabh Kushawah", font=("Arial", 10))
footer_label.grid(row=1, column=0, pady=(0, 10), sticky=tk.S)

root.mainloop()
