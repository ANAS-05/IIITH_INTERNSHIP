from ultralytics import YOLO
import os
import glob

FRAMES_DIR = r"C:\Users\rabee\Desktop\intership\video_project_task2\task2_frames"
OUTPUT_DIR = r"C:\Users\rabee\Desktop\intership\week_2_tasks\week3\segmented_frames"

os.makedirs(OUTPUT_DIR, exist_ok=True)

model = YOLO("yolo26n-seg.pt")

frame_paths = sorted(glob.glob(os.path.join(FRAMES_DIR, "frame_*.jpg")))
selected = frame_paths[::10]
print(f"Processing {len(selected)} frames with YOLO26 segmentation...")

for i, path in enumerate(selected):
    results = model(path)
    filename = f"seg_{i+1:04d}.jpg"
    save_path = os.path.join(OUTPUT_DIR, filename)
    results[0].save(save_path)
    if (i + 1) % 20 == 0:
        print(f"  Done {i + 1}/{len(selected)}")

print("All frames segmented!")
