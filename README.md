# Image Classification with PyTorch and TIMM

A simple Python application that classifies images using pre-trained deep learning models. This project uses PyTorch and the TIMM (PyTorch Image Models) library to perform image classification with ImageNet classes.

## Features

- 🖼️ **Local Image Classification**: Classify any local image file
- 🧠 **Pre-trained Models**: Uses MobileNetV3 model trained on ImageNet
- 📊 **Top-K Results**: Shows top 5 predictions with confidence scores
- 🔧 **No Internet Required**: Works completely offline once set up
- 📋 **Full ImageNet Classes**: Supports all 1000 ImageNet categories
- 📱 **Mobile Optimized**: Lightweight model perfect for edge devices

## Requirements

- Python 3.8 or higher
- Windows, macOS, or Linux

## Installation

### Step 1: Clone or Download
Download this project to your local machine or clone it:
```bash
git clone <your-repo-url>
cd newTest
```

### Step 2: Create Virtual Environment
Create a Python virtual environment to isolate dependencies:

**Windows (PowerShell):**
```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Required Packages
Install all necessary Python packages:
```bash
pip install torch torchvision timm pillow
```

**Package Details:**
- `torch` - PyTorch deep learning framework
- `torchvision` - Computer vision utilities for PyTorch
- `timm` - PyTorch Image Models library with pre-trained models
- `pillow` - Python Imaging Library for image processing

### Step 4: Download ImageNet Classes (Optional)
The ImageNet classes file is included in the project. If you need to re-download it:
```python
python -c "import urllib.request; urllib.request.urlretrieve('https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt', 'imagenet_classes.txt')"
```

## Usage

### Basic Usage
1. **Place your image** in the project directory or note its full path
2. **Update the image path** in `text.py`:
   ```python
   img = Image.open(r"path\to\your\image.jpg").convert('RGB')
   ```
3. **Run the classification**:
   ```bash
   python text.py
   ```

### Example Output
```
torch.Size([1000])
Loaded 1000 ImageNet categories from local file
bull mastiff 0.16561302542686462
Saint Bernard 0.11810302734375
boxer 0.0917702317237854
French bulldog 0.051590368151664734
pug 0.040158968418836594
```

## File Structure
```
newTest/
│
├── text.py                    # Main classification script
├── imagenet_classes.txt       # ImageNet class names
├── README.md                  # This file
├── .venv/                     # Virtual environment (created after setup)
└── your_image.jpg            # Your image file(s)
```

## Configuration

### Changing the Model
You can use different pre-trained models by modifying this line in `text.py`:
```python
model = timm.create_model('mobilenetv3_large_100', pretrained=True)
```

**Popular alternatives:**
- `'mobilenetv3_small_100'` - Even smaller MobileNetV3 variant
- `'resnet18'` - Fast and lightweight ResNet
- `'resnet50'` - Larger, more accurate ResNet
- `'efficientnet_b0'` - Efficient and accurate
- `'vit_base_patch16_224'` - Vision Transformer

### Changing Input Image
Update the image path in `text.py`:
```python
# For Windows paths
img = Image.open(r"C:\path\to\your\image.jpg").convert('RGB')

# For relative paths
img = Image.open("your_image.jpg").convert('RGB')
```

### Supported Image Formats
- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- And most other common image formats

## Troubleshooting

### Common Issues

**1. ModuleNotFoundError: No module named 'timm'**
- Make sure you've activated your virtual environment
- Install packages: `pip install timm torch torchvision pillow`

**2. FileNotFoundError: [Errno 2] No such file or directory: 'your_image.jpg'**
- Check that your image path is correct
- Use absolute paths if relative paths don't work
- Make sure the image file exists

**3. Virtual Environment Issues**
- **Windows**: Use `& .venv\Scripts\Activate.ps1` in PowerShell
- **macOS/Linux**: Use `source .venv/bin/activate`

**4. Memory Issues**
- Try using a smaller model like `mobilenetv3_small_100` instead of larger models
- Reduce image size if very large

### Running Commands

**Windows PowerShell:**
```powershell
# Activate environment
& .venv\Scripts\Activate.ps1

# Run script
python text.py

# Or run directly with full path
C:\path\to\newTest\.venv\Scripts\python.exe text.py
```

**macOS/Linux:**
```bash
# Activate environment
source .venv/bin/activate

# Run script
python text.py
```

## Model Information

- **Architecture**: MobileNetV3-Large
- **Training Dataset**: ImageNet (1.2M images, 1000 classes)
- **Model Size**: ~22 MB (lightweight and mobile-optimized)
- **Input Size**: 224x224 pixels
- **Output**: 1000 class probabilities
- **Optimization**: Designed for mobile and edge devices with efficient inference
