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

## Performance Metrics — Detection

| Metric | Value |
|--------|-------|
| Precision | 0.798 |
| Recall | 0.672 |
| mAP50 | 0.870 |
| mAP50-95 | 0.633 |

## Performance Metrics — Segmentation

| Metric | Value |
|--------|-------|
| Precision | 0.761 |
| Recall | 0.657 |
| mAP50 | 0.838 |
| mAP50-95 | 0.571 |

*Validated on coco8-seg dataset (YOLO26n-seg at 640px)*

## Observed Inference Speed

| Metric | Value |
|--------|-------|
| Avg inference time | ~115ms per frame |
| Avg preprocess | ~2.5ms |
| Avg postprocess | ~2.5ms |
| Total per frame | ~120ms |
| Input resolution | 384x640 |
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
| `input_video.mp4` | Downloaded Shibuya crossing video (640x360, 40s) |
| `final_stacked_output.mp4` | Final vstacked video (640x1080, 3fps) with new audio |

## Task 2 — Stacked Detection & Segmentation Video

### Goal
Download a busy-street video with COCO-detectable objects, extract 120 frames, run YOLO detection and segmentation in parallel, then vertically stack the three video streams (raw → detected → segmented) with a new audio track.

### Steps
1. Downloaded 40s Shibuya crossing YouTube video at 640x360 using `yt-dlp`
2. Extracted 120 frames (every 10th from ~30fps → 3fps output)
3. Ran YOLO26n detection on extracted frames → bounding boxes + labels
4. Ran YOLO26n-seg segmentation on extracted frames → pixel-level masks
5. Created three separate 640x360 videos (raw, detected, segmented) at 3fps
6. Vertically stacked all three via FFmpeg `vstack` → 640x1080
7. Merged `new_audio.mp3` as the soundtrack

### Output
- `final_stacked_output.mp4` — 640x1080, 3fps, 40s, H.264 + AAC, ~12MB
- Top row: raw frames, Middle: object-detected frames, Bottom: segmented frames
