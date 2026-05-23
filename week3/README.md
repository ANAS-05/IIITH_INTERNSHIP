# Week 3 — Image Segmentation with YOLO26

## Task
Run semantic/instance segmentation on video frames using YOLO26, stitch segmented frames into a video, and add new music.

## Steps
1. Loaded pretrained `yolo26n-seg.pt` (YOLO26 nano segmentation model)
2. Processed every 10th frame (181 frames) from the Week 1 video
3. Each frame gets pixel-level segmentation masks with transparent colored overlays
4. Stitched segmented frames into video at 3 fps
5. Merged new audio track (`new_audio.mp3`)

## Performance Metrics

| Metric | Value |
|--------|-------|
| Model | `yolo26n-seg.pt` (pretrained on COCO) |
| Avg inference time | ~115ms per frame |
| Avg preprocess | ~2.5ms |
| Avg postprocess | ~2.5ms |
| Total per frame | ~120ms |
| Frames processed | 181 (every 10th of 1801) |
| Frames with detections | ~120 (66%) |
| Output duration | 60.3 seconds at 3 fps |

## Classes Detected
car, truck, person, airplane, bus, sports ball, bottle, traffic light, fire hydrant, train, cell phone, chair, suitcase, vase, refrigerator

## Files
| File | Description |
|------|-------------|
| `segment_frames.py` | Script to run YOLO26 segmentation on frames |
| `segmented_video.mp4` | Segmented frames stitched into video (no audio) |
| `final_segmented_output.mp4` | Final video with segmentation masks and music |
| `new_audio.mp3` | New music track for this task |
