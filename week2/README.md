# Week 2 Tasks

## Tasks Completed

### (a) Virtual Environment Setup
- Created a Python virtual environment using `venv`
- Environment directory: `summer_env/`

### (b) Ultralytics Installation
- Activated the virtual environment
- Installed `ultralytics` package via `pip install -U ultralytics`
- Dependencies installed: PyTorch, torchvision, OpenCV, matplotlib, etc.

### (c) YOLO26 Object Detection
- Loaded the pretrained YOLO26n model (`yolo26n.pt`)
- Ran inference on `bus.jpg` (downloaded from Ultralytics sample images)
- **Detections:** 4 persons, 1 bus
- **Inference time:** 124.9ms
- Output saved as `output.jpg` with bounding boxes

## Files
- `detect.py` - Object detection script
- `bus.jpg` - Input image
- `output.jpg` - Output with detections
