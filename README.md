# OCR Auto Typer

A Python automation project that extracts text from images using OCR and automatically types the extracted text.

---

## Features

- OCR text extraction from images
- Automatic typing functionality
- Fast and lightweight automation
- Simple Python implementation

---

## Technologies Used

- Python
- OpenCV
- PyTesseract
- PyAutoGUI
- Pillow

---

## Files

```bash
Myfile.py
requirements.txt
README.md
```

---

## Installation

Install required libraries:

```bash
pip install -r requirements.txt
```

---

## Install Tesseract OCR

Download Tesseract OCR:

https://github.com/UB-Mannheim/tesseract/wiki

After installation, update the Tesseract path inside the Python file.

Example:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## Run the Project

```bash
python Myfile.py
```

Steps:
1. Add image path in the script
2. Run the Python file
3. Focus on the typing area
4. Auto typing will start after 5 seconds

---

## Future Improvements

- GUI support
- Adjustable typing speed
- Hotkey controls
- Multi-language OCR support

---

## Author

Garima Agrawal
