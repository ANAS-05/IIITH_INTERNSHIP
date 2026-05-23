import os
import subprocess

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_VIDEO = os.path.join(SCRIPT_DIR, "input_video.mp4")
FRAMES_DIR = os.path.join(SCRIPT_DIR, "raw_frames")
DETECT_DIR = os.path.join(SCRIPT_DIR, "detected_frames")
SEGMENT_DIR = os.path.join(SCRIPT_DIR, "segmented_frames")

for d in [FRAMES_DIR, DETECT_DIR, SEGMENT_DIR]:
    os.makedirs(d, exist_ok=True)

# Step 1: Extract 120 frames (every 10th frame at 30fps)
subprocess.run([
    "ffmpeg", "-y", "-i", INPUT_VIDEO,
    "-vf", "select='not(mod(n,10))',setpts=N/30/TB",
    "-vsync", "vfr",
    "-q:v", "2",
    os.path.join(FRAMES_DIR, "frame_%04d.jpg")
], check=True)

num_frames = len([f for f in os.listdir(FRAMES_DIR) if f.endswith(".jpg")])
print(f"Extracted {num_frames} frames")

# Step 2: Create raw video from frames
subprocess.run([
    "ffmpeg", "-y", "-framerate", "3",
    "-i", os.path.join(FRAMES_DIR, "frame_%04d.jpg"),
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    os.path.join(SCRIPT_DIR, "raw_video.mp4")
], check=True)
print("Raw video created")

# Step 3: Run detection
from ultralytics import YOLO

det_model = YOLO("yolo26n.pt")
frames = sorted([f for f in os.listdir(FRAMES_DIR) if f.endswith(".jpg")])
for i, fname in enumerate(frames):
    path = os.path.join(FRAMES_DIR, fname)
    results = det_model(path)
    out_name = f"det_{i+1:04d}.jpg"
    results[0].save(os.path.join(DETECT_DIR, out_name))
    if (i+1) % 30 == 0:
        print(f"  Detection: {i+1}/{len(frames)}")
print("Detection done")

subprocess.run([
    "ffmpeg", "-y", "-framerate", "3",
    "-i", os.path.join(DETECT_DIR, "det_%04d.jpg"),
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    os.path.join(SCRIPT_DIR, "detected_video.mp4")
], check=True)
print("Detected video created")

# Step 4: Run segmentation
seg_model = YOLO("yolo26n-seg.pt")
for i, fname in enumerate(frames):
    path = os.path.join(FRAMES_DIR, fname)
    results = seg_model(path)
    out_name = f"seg_{i+1:04d}.jpg"
    results[0].save(os.path.join(SEGMENT_DIR, out_name))
    if (i+1) % 30 == 0:
        print(f"  Segmentation: {i+1}/{len(frames)}")
print("Segmentation done")

subprocess.run([
    "ffmpeg", "-y", "-framerate", "3",
    "-i", os.path.join(SEGMENT_DIR, "seg_%04d.jpg"),
    "-c:v", "libx264", "-pix_fmt", "yuv420p",
    os.path.join(SCRIPT_DIR, "segmented_video.mp4")
], check=True)
print("Segmented video created")

# Step 5: vstack all three and add audio
subprocess.run([
    "ffmpeg", "-y",
    "-i", os.path.join(SCRIPT_DIR, "raw_video.mp4"),
    "-i", os.path.join(SCRIPT_DIR, "detected_video.mp4"),
    "-i", os.path.join(SCRIPT_DIR, "segmented_video.mp4"),
    "-filter_complex", "[0:v][1:v][2:v]vstack=inputs=3[v]",
    "-map", "[v]", "-an",
    os.path.join(SCRIPT_DIR, "stacked_noaudio.mp4")
], check=True)
print("Stacked video created (no audio)")

subprocess.run([
    "ffmpeg", "-y",
    "-i", os.path.join(SCRIPT_DIR, "stacked_noaudio.mp4"),
    "-i", os.path.join(SCRIPT_DIR, "new_audio.mp3"),
    "-c:v", "copy", "-c:a", "aac", "-shortest",
    os.path.join(SCRIPT_DIR, "final_stacked_output.mp4")
], check=True)
print("Final video with audio created!")

# Cleanup temp frames
import shutil
for d in [FRAMES_DIR, DETECT_DIR, SEGMENT_DIR]:
    shutil.rmtree(d, ignore_errors=True)
for f in ["raw_video.mp4", "detected_video.mp4", "segmented_video.mp4", "stacked_noaudio.mp4"]:
    os.remove(os.path.join(SCRIPT_DIR, f))
print("Temp files cleaned")
