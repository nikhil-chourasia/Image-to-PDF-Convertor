# Image to PDF Converter 🖼️➡️📄

This project is a simple **Command-Line Interface (CLI) tool** for converting an image file to a PDF format using Python. It utilizes the `img2pdf` library to perform the conversion efficiently and outputs the result as a PDF file. 📑✨

## Features 🚀

- Converts an image (`.png`) to a PDF file with ease. 🔄
- User-friendly CLI prompts for seamless interaction. 💻
- Lightweight and efficient solution for quick conversions. ⚡

## Prerequisites ✅

Ensure you have the following installed on your system:

- Python (>= 3.6) 🐍
- Pip (Python package manager) 📦

## Installation 🛠️

1. Clone the repository or download the script.

    ```
    git clone https://github.com/nikhil-chourasia/Image-to-PDF-Converter.git
    cd Image-to-PDF-Converter
    ```

2. Install the required Python libraries:

    ```
    pip install img2pdf
    ```

## Usage 🖥️

1. Place the input image (named `input.png`) in the folder where the script is located.
2. Run the script using the command:

    ```
    python image_to_pdf_converter.py
    ```

3. When prompted, enter the full folder path where the image is located (ensure the image is named `input.png`):

    ```
    Enter the path of the file and name it as 'input.png': /path/to/folder
    ```

4. The script will process the image and save the output as `output.pdf` in the same folder. 🎉

## How It Works 🤔

1. The script reads the input image file using the `img2pdf` library. 🖼️
2. Converts the image data to a PDF format. 📄
3. Saves the converted file as `output.pdf` in the specified folder. 📂

## Notes 📝

- Make sure the input image is named `input.png`. 📂
- The output PDF will be saved as `output.pdf` in the same folder as the input image. 🖌️
- You can modify the script to customize input and output paths or add error handling as needed. 🛠️

## Contributing 🤝

Feel free to contribute to this project by submitting issues or pull requests. Let's make it better together! 🌟

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details. 🏷️
