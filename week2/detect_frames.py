from ultralytics import YOLO
import os
import glob

FRAMES_DIR = r"C:\Users\rabee\Desktop\intership\video_project_task2\task2_frames"
OUTPUT_DIR = r"C:\Users\rabee\Desktop\intership\video_project_task2\annotated_frames"

os.makedirs(OUTPUT_DIR, exist_ok=True)

model = YOLO("yolo26n.pt")

frame_paths = sorted(glob.glob(os.path.join(FRAMES_DIR, "frame_*.jpg")))
selected = frame_paths[::10]
print(f"Processing {len(selected)} frames (every 10th)...")

for i, path in enumerate(selected):
    results = model(path)
    filename = os.path.basename(path)
    save_path = os.path.join(OUTPUT_DIR, filename)
    results[0].save(save_path)
    if (i + 1) % 20 == 0:
        print(f"  Done {i + 1}/{len(selected)}")

print("All selected frames annotated!")
