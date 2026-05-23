# YOLO26 Dataset Configuration Files — A Technical Overview

## 1. Dataset YAML — The Blueprint

Every Ultralytics dataset is defined by a YAML file (e.g., `coco8-seg.yaml`). It acts as the dataset's manifest:

| Field | Purpose | Example |
|-------|---------|---------|
| `path` | Root directory for the dataset (relative to the Ultralytics datasets folder) | `coco8-seg` |
| `train` | Path to training images, relative to `path` | `images/train` |
| `val` | Path to validation images | `images/val` |
| `test` | Optional test set path | (empty) |
| `names` | Class ID to class name mapping (0-indexed) | `0: person`, `1: bicycle`, ... `79: toothbrush` |
| `download` | URL or script to auto-download the dataset | GitHub release `.zip` URL |

The `train`/`val` fields also accept a `.txt` file listing absolute image paths (used by full `coco.yaml` for its 118K training images via `train2017.txt`).

### Variants by Task

- **Detection** (`coco8.yaml`): maps images → labels with bounding-box coordinates
- **Segmentation** (`coco8-seg.yaml`): identical structure, but labels contain polygon vertices instead of boxes
- **Pose** (`coco8-pose.yaml`): adds `kpt_shape: [17, 3]`, `flip_idx`, and `kpt_names` for 17 keypoints
- **Grayscale/Multispectral**: adds `channels: 1` or `channels: 10`
- **Semantic Segmentation** (`cityscapes.yaml`): adds `masks_dir: masks` and a `label_mapping` section

## 2. Directory Structure

```
coco8-seg/
├── images/
│   ├── train/       (4 images: .jpg)
│   └── val/         (4 images: .jpg)
├── labels/
│   ├── train/       (4 label files: .txt)
│   ├── val/         (4 label files: .txt)
│   └── val.cache    (binary cache of label validation)
├── README.md
└── LICENSE
```

Image and label files share the same base filename (e.g., `000000000009.jpg` ↔ `000000000009.txt`).

## 3. Label File Format (Segmentation)

Each `.txt` file contains one object per line:

```
<class_id> <x1> <y1> <x2> <y2> ... <xn> <yn>
```

- `<class_id>`: integer (0–79 for COCO) mapped via `names` in the YAML
- `<x_i>`, `<y_i>`: polygon vertex coordinates, **normalized** to [0, 1] relative to image width/height
- The polygon defines the precise pixel-level mask of the object

### Example — `labels/train/000000000009.txt` (8 objects):

| Line | Class | Description |
|------|-------|-------------|
| 1 | 45 (bowl) | ~13 polygon vertices |
| 2 | 45 (bowl) | ~14 vertices |
| 3 | 50 (broccoli) | ~60 vertices (detailed) |
| 4 | 45 (bowl) | ~85 vertices (very detailed) |
| 5–8 | 49 (orange) | ~12–18 vertices each (4 instances) |

### Detection Format

The (optional) detection format stores bounding boxes instead:

```
<class_id> <x_center> <y_center> <width> <height>
```

All values are normalized [0, 1]. One box per line, one line per object.

## 4. Training Configuration (`default.yaml`)

Separate from dataset configs, `ultralytics/cfg/default.yaml` holds 134 hyperparameters:
- **Optimizer**: `lr0: 0.01`, `momentum: 0.937`, `weight_decay: 0.0005`
- **Loss weights**: `box: 7.5`, `cls: 0.5`, `dfl: 1.5`
- **Augmentations**: `hsv_h: 0.015`, `scale: 0.5`, `fliplr: 0.5`, `mosaic: 1.0`, `mixup: 0.0`
- **Inference**: `conf: 0.25`, `iou: 0.7`, `max_det: 300`

## 5. References

- **Dataset YAML guide**: https://docs.ultralytics.com/datasets/
- **COCO8-seg dataset page**: https://docs.ultralytics.com/datasets/segment/coco8-seg/
- **COCO dataset structure**: https://docs.ultralytics.com/datasets/detect/coco/
- **Ultralytics default config**: https://docs.ultralytics.com/usage/cfg/
- **Label format specification**: https://docs.ultralytics.com/datasets/detect/#ultralytics-yolo-format
- **Training hyperparameters**: https://docs.ultralytics.com/modes/train/#train-settings
