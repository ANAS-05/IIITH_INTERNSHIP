# IITH Internship — Computer Vision with YOLO

End-to-end computer vision pipeline: video processing, object detection, segmentation, custom dataset creation, and YOLO training.

## Repository Structure

| Week | Topics | Key Files |
|------|--------|-----------|
| **week1/** | Video frame extraction, reconstruction, audio merging | `final_task3.mp4` |
| **week2/** | YOLO object detection on video frames | `detect_frames.py`, `final_output.mp4` |
| **week3/** | Segmentation (YOLO26n-seg) + stacked raw/detected/segmented video | `segment_frames.py`, `final_stacked_output.mp4` |
| **week4/** | Dataset YAML/label format analysis report | `report.md` |
| **week5/** | Custom dataset creation, YOLO training, inference | `best.pt`, `person_vehicle_detection_inference.mp4`, `output_1min.mp4` |

## Tools Used

- **YOLO26n** / **YOLO26n-seg** — Pretrained detection & segmentation models
- **FFmpeg** — Frame extraction, video stitching, scaling, audio merging
- **Label Studio** — Annotation tool (installed in separate venv)
- **OpenCV** — Image processing & video writing
- **Ultralytics** — YOLO training & inference framework

## Pipeline Summary

1. Download video → extract frames → annotate → train → infer → produce final video
2. All labels in YOLO format (normalized class_id + bounding box coordinates)
3. Aspect ratio preserved when scaling images (normalized labels remain valid)

## Deliverables

- Trained model weights (`best.pt`)
- Labeled datasets with YAML config + train/val split
- Inference videos with detection overlays and audio
- Documentation of dataset meta-configuration
