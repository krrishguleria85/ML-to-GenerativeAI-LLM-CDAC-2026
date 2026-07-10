# Low-Light Image Enhancement Framework Using Stable Diffusion

## Project Overview

This project enhances low-light images using a pretrained Stable Diffusion Image-to-Image model. The application is built using Python, PyTorch, Hugging Face Diffusers, and Streamlit.

The user uploads a low-light image, and the model generates an enhanced version while displaying image quality metrics such as PSNR and SSIM.

---

## Features

- Low-light image enhancement
- Stable Diffusion Image-to-Image model
- Streamlit web interface
- PSNR and SSIM evaluation
- Image upload and download support

---

## Technologies Used

- Python 3.10
- PyTorch
- Hugging Face Diffusers
- Streamlit
- Pillow
- NumPy
- OpenCV
- scikit-image

---

## Dataset

LOL (Low-Light) Dataset

Dataset Structure:

dataset/
└── lol_dataset/
    ├── eval15/
    │   ├── low/
    │   └── high/

---

## Project Structure

CDAC_PROJECT_2026/

├── dataset/

├── models/

│   └── model_loader.py

├── outputs/

├── utils/

│   ├── preprocessing.py

│   ├── metrics.py

│   └── helper.py

├── app.py

├── inference.py

├── requirements.txt

├── test_preprocessing.py

├── test_metrics.py

├── test_inference.py

└── README.md

---

## Installation

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Output

The application provides:

- Original Image
- Enhanced Image
- PSNR
- SSIM
- Processing Time
- Download Enhanced Image

---

## Notes

- The project uses a pretrained Stable Diffusion Image-to-Image model.
- The first execution downloads the model from Hugging Face (approximately 5–6 GB).
- Subsequent executions use the locally cached model.
