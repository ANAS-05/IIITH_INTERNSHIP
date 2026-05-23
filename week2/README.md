# Week 2 Tasks

## Tasks Completed

### (a) Virtual Environment Setup
- Created a Python virtual environment using `venv`
- Environment directory: `summer_env/`

### (b) Ultralytics Installation
- Activated the virtual environment
- Installed `ultralytics` package via `pip install -U ultralytics`
- Dependencies installed: PyTorch, torchvision, OpenCV, matplotlib, etc.

### (c) YOLO26 Object Detection (Single Image)
- Loaded the pretrained YOLO26n model (`yolo26n.pt`)
- Ran inference on `bus.jpg` (downloaded from Ultralytics sample images)
- **Detections:** 4 persons, 1 bus
- **Inference time:** 124.9ms
- Output saved as `output.jpg` with bounding boxes

### (d) YOLO26 Object Detection on Video Frames
- Took 1801 frames from Week 1 Task 2 video (`input_task2.mp4`)
- Processed every 10th frame (181 frames total) through YOLO26n
- Stitched annotated frames back into a video at 3 fps
- Merged audio track from Week 1 (`audio.mp3`) with the detected video
- **Final video:** `final_output.mp4` (~60 seconds)

## Files
- `detect.py` - Object detection script for single image
- `detect_frames.py` - Object detection script for batch frame processing
- `bus.jpg` - Input image for single detection
- `output.jpg` - Single image output with detections
- `final_output.mp4` - Final video with YOLO26 detections and audio
